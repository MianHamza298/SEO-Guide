/* =========================================================
   SEO 0 to Hero — Master Guide
   main.js — mobile sidebar toggle + scrollspy active-link
   No external dependencies.
   ========================================================= */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Mobile sidebar toggle ---------- */
  var toggleBtn = document.getElementById('navToggle');
  var side = document.getElementById('side');

  if (toggleBtn && side) {
    toggleBtn.addEventListener('click', function () {
      side.classList.toggle('open');
      toggleBtn.textContent = side.classList.contains('open') ? '✕ Close' : '☰ Modules';
    });

    // Close sidebar automatically after tapping a link (mobile UX)
    side.querySelectorAll('nav a').forEach(function (link) {
      link.addEventListener('click', function () {
        if (window.innerWidth <= 800) {
          side.classList.remove('open');
          toggleBtn.textContent = '☰ Modules';
        }
      });
    });
  }

  /* ---------- Scrollspy: highlight active module in sidebar ---------- */
  var sections = Array.prototype.slice.call(document.querySelectorAll('section.module'));
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.side nav a'));

  if (sections.length && navLinks.length && 'IntersectionObserver' in window) {
    var linkById = {};
    navLinks.forEach(function (link) {
      var id = link.getAttribute('href').replace('#', '');
      linkById[id] = link;
    });

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var id = entry.target.id;
        var link = linkById[id];
        if (!link) return;
        if (entry.isIntersecting) {
          navLinks.forEach(function (l) { l.classList.remove('active'); });
          link.classList.add('active');
        }
      });
    }, { rootMargin: '-15% 0px -70% 0px', threshold: 0 });

    sections.forEach(function (sec) { observer.observe(sec); });
  }
});
