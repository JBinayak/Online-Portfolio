'use strict';
document.documentElement.classList.add('js');

// Progressive enhancement: the navigation remains visible without JavaScript.
const toggle = document.querySelector('.menu-toggle');
const menuLabel = toggle.querySelector('.menu-label');
const nav = document.querySelector('#main-nav');
const header = document.querySelector('.site-header');
const mobile = window.matchMedia('(max-width: 760px)');
toggle.hidden = false;

function closeMenu(returnFocus = false) {
  nav.classList.remove('is-open');
  toggle.setAttribute('aria-expanded', 'false');
  menuLabel.textContent = 'Menu';
  if (returnFocus) toggle.focus();
}

toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  menuLabel.textContent = open ? 'Close' : 'Menu';
  nav.classList.toggle('is-open', open);
});

document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') closeMenu(true);
});
document.addEventListener('click', event => {
  if (!event.target.closest('.site-header')) closeMenu();
});
document.addEventListener('focusin', event => {
  if (mobile.matches && !header.contains(event.target)) closeMenu();
});
mobile.addEventListener('change', () => closeMenu());

// Native anchors handle URL history and scrolling; focus follows the destination
// for keyboard users, including the skip link and desktop navigation.
document.addEventListener('click', event => {
  const link = event.target.closest('a[href^="#"]');
  if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
  const destination = document.getElementById(link.hash.slice(1));
  if (!destination) return;
  closeMenu();
  const focusTarget = destination.id === 'top'
    ? document.querySelector('.brand')
    : destination.querySelector('h1, h2') || destination;
  if (!focusTarget.hasAttribute('tabindex') && focusTarget.tagName !== 'A') {
    focusTarget.setAttribute('tabindex', '-1');
    focusTarget.addEventListener('blur', () => focusTarget.removeAttribute('tabindex'), { once: true });
  }
  // Run after the native fragment action so it cannot reset keyboard focus.
  requestAnimationFrame(() => focusTarget.focus({ preventScroll: true }));
});

// Recompute the current section in either scroll direction, including short
// sections near the end of the page. Batch geometry reads to one animation frame.
const sectionLinks = [...nav.querySelectorAll('a[href^="#"]')];
const sections = sectionLinks.map(link => document.querySelector(link.hash));
let pendingFrame = false;
function updateCurrentSection() {
  const threshold = header.getBoundingClientRect().height + Math.min(150, innerHeight * .2);
  let current = null;
  for (const section of sections) {
    if (section.getBoundingClientRect().top <= threshold) current = section.id;
  }
  if (window.scrollY + innerHeight >= document.documentElement.scrollHeight - 2) current = 'contact';
  sectionLinks.forEach(link => {
    if (link.hash === `#${current}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
  pendingFrame = false;
}
function scheduleSectionUpdate() {
  if (pendingFrame) return;
  pendingFrame = true;
  requestAnimationFrame(updateCurrentSection);
}
window.addEventListener('scroll', scheduleSectionUpdate, { passive: true });
window.addEventListener('resize', scheduleSectionUpdate);
window.addEventListener('hashchange', scheduleSectionUpdate);
document.querySelectorAll('details').forEach(detail => detail.addEventListener('toggle', scheduleSectionUpdate));
document.fonts?.ready.then(scheduleSectionUpdate);
updateCurrentSection();

const copyButton = document.querySelector('#copy-email');
const copyLabel = copyButton.querySelector('.copy-label');
const copyStatus = document.querySelector('#copy-status');
const emailLink = document.querySelector('.email-row a');
if (navigator.clipboard?.writeText) {
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    copyButton.disabled = true;
    copyButton.removeAttribute('data-copied');
    copyLabel.textContent = 'Copying…';
    copyStatus.textContent = '';
    try {
      await navigator.clipboard.writeText(emailLink.href.slice('mailto:'.length));
      copyLabel.textContent = 'Copied';
      copyButton.setAttribute('data-copied', 'true');
      copyStatus.textContent = 'Email address copied. Paste it into your email app.';
    } catch {
      copyLabel.textContent = 'Copy email';
      copyStatus.textContent = 'Couldn’t copy automatically. Select the address to copy it, or use the email link.';
    } finally {
      copyButton.disabled = false;
    }
  });
}
