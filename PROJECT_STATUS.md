# Project Status

## Current Build Status

Working starter version for local portfolio review. The extension runs in demo mode without an LLM API key, and the optional backend exposes rule-based helper endpoints.

## Completed Features

- Manifest V3 browser extension scaffold
- Extension popup
- Content script for visible page text
- Page title and text extraction
- Rule-based summarisation
- Rule-based task checklist extraction
- Form field detection
- Reviewed form draft suggestions
- Human-in-the-loop insertion flow
- Privacy and safety notice
- Optional FastAPI backend
- Backend endpoints for health, summarise, tasks and form suggestions
- Demo HTML page with safe fake content
- pytest backend tests
- GitHub Actions workflow

## Remaining Improvements

- Add JavaScript unit tests for popup/content script logic.
- Add screenshots after manual local browser review.
- Add optional LLM integration with explicit user-controlled credentials.
- Add richer text extraction and page readability heuristics.
- Add more detailed permission review before making public.

## Testing Status

Backend tests cover text extraction, summary fallback, task extraction and API endpoints.

Run:

```bash
cd backend
pytest
```

## What Must Be Checked Before Making Public

- No `.env` files or credentials are present.
- No real browsing history or private page data is present.
- No generated CV PDFs, job applications or application packets are committed.
- README does not claim production use, Chrome Web Store publication or real users.
- Extension permissions are reviewed and explained.

## Files That Must Never Be Committed

- `.env` or `.env.*`
- API keys, tokens, credentials or passwords
- database files
- logs
- generated CV PDFs
- application packets
- generated outputs
- private data
- browser history
- uploads
- local data
