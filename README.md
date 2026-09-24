# LIGHTNOVEL.EXE — Complete Static Parody Novel Site

This is a complete static reading site. Python is used only at build time to generate the novel JSON files.

## Generate the novels

From the `generator` directory:

```bash
python generate.py
```

The generator creates 8 complete novels, each with 520 chapters, in `novels/`.

## Run the static site locally

Because browsers normally block `fetch()` when an HTML file is opened directly with `file://`, serve the folder with any static-file server. The website itself contains no Python server.

Example:

```bash
python -m http.server 8080
```

Then open `http://localhost:8080/`.

## Runtime

- No database
- No login/signup
- No API
- No AI service
- No localStorage/sessionStorage
- No server-side application
- All novel data is shipped as static JSON
- Chapter navigation is encoded in the URL
