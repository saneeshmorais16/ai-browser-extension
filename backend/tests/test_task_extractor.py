from app.form_helper import suggest_form_answer
from app.task_extractor import extract_tasks


def test_task_extraction_finds_action_sentences():
    text = "Read this page. Submit the form after review. Download the guide."
    tasks = extract_tasks(text)
    assert tasks == ["Submit the form after review", "Download the guide"]


def test_form_suggestion_requires_review_language():
    suggestion = suggest_form_answer(label="Experience")
    assert suggestion.startswith("Draft for review")
