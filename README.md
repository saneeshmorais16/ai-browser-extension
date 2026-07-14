# AI Browser Extension

A portfolio-ready Browser Extension Manifest V3 project that demonstrates AI-assisted page analysis, visible text extraction, rule-based summarisation, task assistance, reviewed form suggestions and a human-in-the-loop safety flow.

## What This Project Does

The extension reads visible page text on the active tab, generates a short demo-mode summary, builds a checklist of likely actions and detects editable form fields. It suggests draft responses but requires the user to review and click before anything is inserted.

## Why It Matters

AI assistants can help people understand pages and prepare responses, but browser tooling needs strong privacy and safety boundaries. This project demonstrates useful assistance without hidden collection, credential capture or automatic form submission.

## Problem Statement

Web pages often contain long instructions, calls to action and forms. Users need help summarising the content and preparing safe draft responses while staying in control of what gets inserted or submitted.

## Tech Stack

- JavaScript, HTML and CSS
- Browser Extension Manifest V3
- FastAPI optional backend
- Pydantic
- pytest
- GitHub Actions

## Core Features

- Browser extension popup
- Content script for visible text extraction
- Page title and main text extraction
- Rule-based summary fallback
- Rule-based task checklist extraction
- Form field detection
- Reviewed draft form suggestions
- Privacy and safety notice
- Optional FastAPI backend endpoints
- Demo mode with no paid LLM API key

## Browser Extension Architecture

- `extension/manifest.json` defines the Manifest V3 extension.
- `extension/content.js` runs on pages and responds to popup requests for visible text and form fields.
- `extension/popup.js` handles user actions and rule-based demo output.
- `extension/options.html` stores an optional backend URL.
- `backend/app/` provides optional API endpoints for the same rule-based workflows.

## Human-In-The-Loop Safety Design

- The extension never auto-submits forms.
- Draft answers are displayed first.
- Insertion requires a user click for each field.
- Password and hidden fields are ignored.
- The README and popup explain that only visible page text is used.

## Setup Steps

```bash
cd backend
pip install -r requirements.txt
```

## Load The Extension Locally

1. Open Chrome or Edge extensions.
2. Enable Developer Mode.
3. Choose "Load unpacked".
4. Select the `extension/` folder.
5. Open `examples/demo_page.html` or another safe page and click the extension icon.

## Run The Optional Backend

```bash
cd backend
uvicorn app.main:app --reload
```

You can also run:

```bash
python run_backend.py
```

## Run Tests

```bash
cd backend
pytest
```

## Privacy And Limitations

This starter uses demo-safe rule-based logic and does not require API keys. It does not claim production use, Chrome Web Store publication or real users. It does not collect private browsing history, capture credentials, scrape sites or submit forms. Browser permissions should be reviewed before any public release.

## Future Improvements

- Add optional LLM provider integration with explicit user configuration.
- Add frontend unit tests with a lightweight JavaScript test runner.
- Add storage for reviewed local history using a user-controlled backend.
- Add stronger page-readability extraction.
- Add screenshots after local extension review.

## No-Secrets Note

Do not commit `.env` files, API keys, tokens, credentials, passwords, private browsing data, real job applications, generated CV PDFs, logs, application packets or local exports.
