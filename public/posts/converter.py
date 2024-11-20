# Read all html files in the current directory

import os
import json
from bs4 import BeautifulSoup

blog = json.load(open("blog.json"))

manuals = []

def make_name(title):
    # Turn ı into i, ç into c, etc.
    title = title.replace("ı", "i").replace("ç", "c").replace("ş", "s").replace("ğ", "g").replace("ü", "u").replace("ö", "o")
    # Remove all non-alphanumeric characters
    title = "".join(filter(lambda c: c.isalnum() or c == " ", title))
    # Replace spaces with dashes
    title = title.replace(" ", "-")
    # Lowercase
    title = title.lower()
    return title

for filename in os.listdir("."):
    if not filename.endswith(".html"):
        continue

    # Read the file
    with open(filename, "r") as file:
        content = file.read()

    # Try to identify the blog post
    post = next(filter(lambda post: post["title"] in content or post['id'] , blog), None)

    print(post)

    if post is None:
        manuals.append(filename)
    else:
        # Get the title
        title = post["title"]

        # Get the date
        date = post["date"]

        # Get the content
        print(content)
        content = content.split("<body>")[1].split("</body>")[0]

        # Write the content to a new filew
        sanitizedfilename = make_name(title)
        with open(f"{sanitizedfilename}.md", "w") as file:
            file.write(f"""+++
title = "{title}"
date = "{date}"
tags = "{post["tags"]}"
language = "{post["lang"]}"
+++\n\n""")
            soup = BeautifulSoup(content, "html.parser")
            file.write(soup.prettify())
        
        # Remove the old file
        os.remove(filename)

with open("manuals.txt", "w") as file:
    for manual in manuals:
        file.write(manual + "\n")




    # Get the title
    # title = content.split("<title>")[1].split("</title>")[0]
