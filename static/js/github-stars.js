document.addEventListener('DOMContentLoaded', function () {
  try {
    var links = document.querySelectorAll('a.no-hover[href*="github.com/"]');
    links.forEach(function (link) {
      // Find or create a sibling span to display stars
      var span = link.parentElement.querySelector('.github-stars');
      if (!span) {
        span = document.createElement('span');
        span.className = 'github-stars';
        link.insertAdjacentElement('afterend', span);
      }
      // If already populated, skip
      if (span.dataset.loaded === '1') return;

      // Parse owner/repo from URL
      var href = link.getAttribute('href');
      var url;
      try {
        url = new URL(href);
      } catch (e) {
        return;
      }
      var parts = url.pathname.replace(/^\/+|\/+$/g, '').split('/');
      if (parts.length < 2) return;
      var owner = parts[0];
      var repo = parts[1];

      // Fetch stars
      fetch('https://api.github.com/repos/' + owner + '/' + repo)
        .then(function (res) { return res.ok ? res.json() : Promise.reject(res); })
        .then(function (data) {
          if (!data || typeof data.stargazers_count !== 'number') return;
          var stars = data.stargazers_count.toLocaleString();
          span.textContent = '⭐ ' + stars;
          span.setAttribute('title', stars + ' GitHub stars');
          span.dataset.loaded = '1';
        })
        .catch(function () {
          // Silently fail to avoid UI noise if rate-limited or offline
        });
    });
  } catch (_e) {
    // no-op
  }
});


