# ROLDA LT Website

Automotive diagnostics and programming services website for KAMSIMA.

## Setup Instructions

### 1. Download Images

The website uses local images. Run the image download script to fetch them:

```bash
python3 download_images.py
```

### 2. Run Local Development Server

You can run the website locally using Python's built-in HTTP server:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000 in your browser.

### 3. Folder Structure

- `/images/` - Contains all local images
  - `/flags/` - Country flags for language switching
  - `/hero/` - Hero banner images
  - `/services/` - Service-specific images
- `/partials/` - HTMX partial HTML files for dynamic loading
- `index.html` - Main website page

## Technologies

- HTML5, CSS3
- HTMX for dynamic content loading
- Multi-language support (Lithuanian and English)
