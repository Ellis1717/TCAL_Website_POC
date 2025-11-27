# TCAL_Website_POC
POC website for TCAL - Tami Callahan Small Business Website

Getting Started
- Open `index.html` in a browser to preview.
- Brand assets live in `assets/` (logo is `assets/logo.svg`).

Contact Form Options
- Netlify Forms (storage + email):
  - Deploy this repo to Netlify.
  - The form is already marked up with `data-netlify="true"`, `name="contact"`, and includes a honeypot. Submissions will appear in your Netlify dashboard. Optional: add email notifications in Netlify.
- Formspree (email):
  - Edit `index.html`, find `const FORM_ENDPOINT = null;` and replace with your endpoint, e.g. `const FORM_ENDPOINT = 'https://formspree.io/f/xxxxxx'`.
  - The form will submit via AJAX and show a success/fail message.
- Mail client fallback:
  - If neither option is configured, the form opens the user’s email client with a prefilled message.

SEO & Social
- Update `og:url`, `canonical`, and `og:image` to your live domain.
- Optional: add a real OpenGraph image at `assets/og-image.png` and ensure it’s an absolute URL in meta tags.

Analytics (optional)
- Choose one snippet in `index.html` and configure:
  - Plausible: replace `example.com` in the data-domain attribute.
  - Google Analytics 4: replace `G-XXXXXXX` with your measurement ID.

Accessibility
- Skip link, proper labels, focus-visible styles, and ARIA live region are enabled by default.
