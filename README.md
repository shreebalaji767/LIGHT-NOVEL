# LIGHTNOVEL — Personal Light Novel Publishing Platform

A free, static light novel library and local-first author workspace designed for GitHub Pages.

## Features

- Responsive modern library with title/description search, genre filters and sorting.
- Existing generated novel catalogue and chapter reader are preserved.
- Browser-local favourites, reading progress, chapter bookmarks and reader preferences.
- Reader controls for font size, paper/dark themes, keyboard chapter navigation and progress indicator.
- Local Author Studio for drafting novels, adding chapters, autosaving to browser storage, importing/exporting backups, and exporting Markdown or JSON manuscripts.
- PWA install metadata and service-worker caching for the site shell and novels already opened online.
- No server, database, login, paid API, subscription or advertising.

## Publish with GitHub Pages

1. Open repository **Settings → Pages**.
2. Select **Deploy from a branch**.
3. Choose `main` and `/(root)`, then save.
4. Wait for the Pages deployment and open the published URL.

## Local preview

Because the site loads JSON with `fetch()`, do not open `index.html` directly with `file://`. Run any static file server from the repository root, for example:

```bash
python -m http.server 8080
```

Then open `http://localhost:8080/`.

## Authoring and publishing workflow

The Author Studio stores drafts in this browser's localStorage. Export a Markdown or JSON manuscript and add it to the repository to publish it. A static GitHub Pages site cannot securely commit directly to GitHub without an authenticated publishing integration.

## Data and offline notes

- Existing files in `novels/` remain the published catalogue.
- Favourites, bookmarks, reading progress, preferences and drafts are browser-local; they do not sync between devices.
- Novel JSON files are cached after being opened online, so previously opened novels can be read offline where the browser retains the cache.
- Export local drafts and reading data regularly. Clearing browser site data can erase local-only information.
- The generator in `generator/` is a build-time utility. Review its output before running it; do not run it over edited novel files without a backup.

## Technology

HTML5, CSS3, vanilla JavaScript, JSON, Markdown, localStorage, Cache API and Service Worker. No runtime dependencies.
