#!/usr/bin/env python3
"""Generate citation markdown files for all blog posts."""

import hashlib
import os
import re
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
import json
from pathlib import Path

# Resolve paths relative to repo root
REPO_ROOT = Path(__file__).resolve().parent.parent
CONTENT_POSTS = REPO_ROOT / "content" / "posts"
CONTENT_CITE = REPO_ROOT / "content" / "cite"
CONFIG_TOML = REPO_ROOT / "config.toml"


def parse_config():
    """Extract base_url and author from config.toml."""
    text = CONFIG_TOML.read_text()
    base_url = re.search(r'^base_url\s*=\s*"([^"]+)"', text, re.MULTILINE)
    author = re.search(r'^author\s*=\s*"([^"]+)"', text, re.MULTILINE)
    return (
        base_url.group(1).rstrip("/") if base_url else "https://alperenkeles.com",
        author.group(1) if author else "Alperen Keles",
    )


def parse_front_matter(path):
    """Extract title and date from a markdown file's TOML front matter."""
    text = path.read_text()
    m = re.match(r"^\+\+\+\s*\n(.*?)\n\+\+\+", text, re.DOTALL)
    if not m:
        return None, None
    fm = m.group(1)
    title_m = re.search(r'^title\s*=\s*"([^"]+)"', fm, re.MULTILINE)
    date_m = re.search(r'^date\s*=\s*"([^"]+)"', fm, re.MULTILINE)
    title = title_m.group(1) if title_m else None
    date = date_m.group(1) if date_m else None
    return title, date


def discover_posts():
    """Find all posts as (slug, title, date, post_path) tuples."""
    posts = []
    if not CONTENT_POSTS.exists():
        return posts

    for entry in sorted(CONTENT_POSTS.iterdir()):
        if entry.name.startswith("_") or entry.name.startswith("."):
            continue

        if entry.is_file() and entry.suffix == ".md":
            slug = entry.stem
            title, date = parse_front_matter(entry)
            if title and date:
                posts.append((slug, title, date, entry))
        elif entry.is_dir():
            index = entry / "index.md"
            if index.exists():
                slug = entry.name
                title, date = parse_front_matter(index)
                if title and date:
                    posts.append((slug, title, date, index))

    return posts


def hash_post(post_path):
    """Compute a SHA-256 hash of the post file contents."""
    return hashlib.sha256(post_path.read_bytes()).hexdigest()


def read_existing_hash(slug):
    """Read post_hash from an existing citation file, or return None."""
    cite_file = CONTENT_CITE / f"{slug}.md"
    if not cite_file.exists():
        return None
    text = cite_file.read_text()
    m = re.search(r'^post_hash\s*=\s*"([^"]+)"', text, re.MULTILINE)
    return m.group(1) if m else None


def get_wayback_url(post_url):
    """Check for existing Wayback Machine snapshot, or request archival."""
    encoded_url = urllib.parse.quote(post_url, safe="")
    # Check for existing snapshot
    check_url = f"https://archive.org/wayback/available?url={encoded_url}"
    try:
        req = urllib.request.Request(check_url)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
            snapshots = data.get("archived_snapshots", {})
            closest = snapshots.get("closest", {})
            if closest.get("available"):
                return closest["url"]
    except (urllib.error.URLError, json.JSONDecodeError, OSError) as e:
        print(f"  Warning: Wayback check failed for {post_url}: {e}", file=sys.stderr)

    # Try to save
    save_url = f"https://web.archive.org/save/{urllib.parse.quote(post_url, safe='/:')}"
    try:
        req = urllib.request.Request(save_url, method="POST")
        req.add_header("User-Agent", "citation-generator/1.0")
        with urllib.request.urlopen(req, timeout=30) as resp:
            # The save endpoint returns a redirect or header with the archived URL
            location = resp.headers.get("Content-Location") or resp.headers.get("Location")
            if location:
                return f"https://web.archive.org{location}"
    except (urllib.error.URLError, OSError) as e:
        print(f"  Warning: Wayback save failed for {post_url}: {e}", file=sys.stderr)

    # Fallback: construct a generic Wayback URL
    return f"https://web.archive.org/web/{post_url}"


def make_bibtex_key(author, year, title):
    """Generate BibTeX key: keles<year><first-word> (lowercase, alphanumeric)."""
    last_name = author.split()[-1].lower()
    first_word = re.sub(r"[^a-z0-9]", "", title.split()[0].lower()) if title.split() else "untitled"
    return f"{last_name}{year}{first_word}"


def format_bibtex(author, title, year, post_url, wayback_url):
    key = make_bibtex_key(author, year, title)
    return (
        f"@online{{{key},\n"
        f"  author = {{{author}}},\n"
        f"  title = {{{title}}},\n"
        f"  year = {{{year}}},\n"
        f"  url = {{{post_url}}},\n"
        f"  note = {{Archived at \\url{{{wayback_url}}}}}\n"
        f"}}"
    )


def format_apa(author, title, date_str, post_url, site_name, wayback_url):
    """Format APA citation."""
    parts = date_str.split("-")
    year = parts[0]
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    month = months[int(parts[1]) - 1] if len(parts) >= 2 else ""
    day = str(int(parts[2])) if len(parts) >= 3 else ""

    # Last, F.
    name_parts = author.split()
    last = name_parts[-1]
    initials = ". ".join(n[0] for n in name_parts[:-1]) + "." if len(name_parts) > 1 else ""

    date_part = f"{year}, {month} {day}" if month and day else year
    return f"{last}, {initials} ({date_part}). {title}. {site_name}. {post_url}. Archived at {wayback_url}"


def escape_toml(s):
    """Escape a string for use in a TOML quoted value."""
    return s.replace("\\", "\\\\").replace('"', '\\"')


def escape_toml_multiline(s):
    """Escape a string for use in a TOML triple-quoted value."""
    # In triple-quoted strings, we only need to escape backslashes
    return s.replace("\\", "\\\\")


def write_citation_files(slug, title, date_str, author, base_url, site_name, post_hash):
    """Generate the 3 citation markdown files for a post."""
    year = date_str.split("-")[0]
    post_url = f"{base_url}/posts/{slug}/"

    print(f"  Checking Wayback Machine for {post_url}...")
    wayback_url = get_wayback_url(post_url)

    bibtex = format_bibtex(author, title, year, post_url, wayback_url)
    apa = format_apa(author, title, date_str, post_url, site_name, wayback_url)

    escaped_title = escape_toml(title)

    # Main citation page — use triple-quoted strings for multiline bibtex
    main_md = (
        f'+++\n'
        f'title = "Cite: {escaped_title}"\n'
        f'path = "posts/{slug}/cite"\n'
        f'template = "citation.html"\n'
        f'\n'
        f'[extra]\n'
        f'bibtex = """\n{escape_toml_multiline(bibtex)}"""\n'
        f'apa = "{escape_toml(apa)}"\n'
        f'original_title = "{escaped_title}"\n'
        f'original_url = "{post_url}"\n'
        f'original_date = "{date_str}"\n'
        f'post_hash = "{post_hash}"\n'
        f'+++\n'
    )
    (CONTENT_CITE / f"{slug}.md").write_text(main_md)

    # BibTeX raw endpoint
    bibtex_md = (
        f'+++\n'
        f'title = "BibTeX: {escaped_title}"\n'
        f'path = "posts/{slug}/cite/bibtex"\n'
        f'template = "citation-raw.html"\n'
        f'\n'
        f'[extra]\n'
        f'citation_text = """\n{escape_toml_multiline(bibtex)}"""\n'
        f'+++\n'
    )
    (CONTENT_CITE / f"{slug}-bibtex.md").write_text(bibtex_md)

    # APA raw endpoint
    apa_md = (
        f'+++\n'
        f'title = "APA: {escaped_title}"\n'
        f'path = "posts/{slug}/cite/apa"\n'
        f'template = "citation-raw.html"\n'
        f'\n'
        f'[extra]\n'
        f'citation_text = "{escape_toml(apa)}"\n'
        f'+++\n'
    )
    (CONTENT_CITE / f"{slug}-apa.md").write_text(apa_md)


def main():
    base_url, author = parse_config()
    site_name = author  # Use author name as site name for APA

    print(f"Base URL: {base_url}")
    print(f"Author: {author}")

    CONTENT_CITE.mkdir(parents=True, exist_ok=True)

    posts = discover_posts()
    print(f"Found {len(posts)} posts")

    # Build set of valid slugs to clean up stale citation files after
    valid_slugs = set()
    skipped = 0

    for slug, title, date, post_path in posts:
        valid_slugs.add(slug)
        current_hash = hash_post(post_path)
        existing_hash = read_existing_hash(slug)

        if current_hash == existing_hash:
            skipped += 1
            continue

        print(f"Processing: {slug}")
        write_citation_files(slug, title, date, author, base_url, site_name, current_hash)
        time.sleep(1)  # Be polite to Wayback Machine

    # Remove citation files for posts that no longer exist
    for f in CONTENT_CITE.iterdir():
        if f.name == "_index.md" or f.suffix != ".md":
            continue
        # Derive slug from filename (strip -bibtex/-apa suffix)
        stem = f.stem
        if stem.endswith("-bibtex"):
            file_slug = stem[: -len("-bibtex")]
        elif stem.endswith("-apa"):
            file_slug = stem[: -len("-apa")]
        else:
            file_slug = stem
        if file_slug not in valid_slugs:
            print(f"Removing stale: {f.name}")
            f.unlink()

    print(f"\nGenerated citation files in {CONTENT_CITE}")
    print(f"Skipped {skipped} unchanged posts")


if __name__ == "__main__":
    main()
