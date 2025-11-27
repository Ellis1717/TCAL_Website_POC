agent.md – Repository Guidelines

These guidelines ensure the project remains clean, consistent, and easy to maintain for a small-business static website.

1. Project Structure

Primary files

index.html — single-page site; HTML/CSS/JS may remain inline for simplicity.

assets/ — all static assets:

Logos, icons, and images.

If adding larger dependencies:

JavaScript → assets/js/

CSS → assets/css/

README.md — quick-start guide, deployment notes, and form/analytics configuration.

General rules

Keep the project lightweight and static—no build pipeline required.

Store all new media inside assets/.

2. Local Development & Preview

Run a lightweight local server:

Python

python3 -m http.server 8080


Then open: http://localhost:8080/

Node.js (optional)

npx serve .
# or
npx http-server .

3. Form Configuration

Netlify (recommended)

Works automatically using data-netlify and a hidden form field.

Ideal for small business contact forms.

Formspree

In index.html, update:

const FORM_ENDPOINT = "https://formspree.io/f/xxxxxx";


Deployment notes

Deploy via Netlify or any static host.

After deployment, ensure:

<link rel="canonical"> points to the live URL.

OpenGraph og:url and og:image use absolute URLs.

4. Coding Style & Naming Conventions

HTML

Use semantic tags (header, main, section, footer).

Ensure labels are accessible; use ARIA only when required.

CSS

2-space indentation.

Class/ID format: lowercase, hyphen-separated
(e.g., nav-inner, contact-title).

Avoid inline styles; use class-based rules.

JavaScript

Stick to vanilla JS.

Keep scripts inside index.html unless large—then move to assets/js/main.js.

Prefer clear, single-purpose functions.

5. Testing Checklist

Functional

Required fields validated.

Email field uses proper regex.

Honeypot spam protection present.

Test both success and error form states.

Accessibility

Full keyboard navigation.

Proper focus-visible behavior.

Adequate color contrast.

Every form field has a proper label.

SEO & Meta

Correct canonical URL.

Proper og:url, og:title, and og:image tags.

All external URLs are absolute.

Optional Tools

Lighthouse audit (Performance/Accessibility/SEO).

HTML validator before merging changes.

6. Commit & Pull Request Standards

Commits

Use imperative mood.

Subject line ≤72 characters.

Add a detailed body when needed.

Examples:

Fix email validation regex

Optimize mobile spacing

Update OG tags after domain change

Pull Requests

Provide a clear description and reasoning.

Include screenshots for visual/layout updates.

Note any SEO, analytics, or form-related changes.

Keep PRs focused—avoid unrelated refactoring.

Update README.md if behavior or setup changes.

7. Security & Configuration

Do not commit secrets, API keys, tokens, or analytics IDs.

Double-check form endpoints (Netlify or Formspree) before deploying.

Keep anti-spam measures enabled (honeypot + required fields).

Use HTTPS everywhere.