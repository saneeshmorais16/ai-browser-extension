from app.summariser import summarise_text
from app.text_utils import extract_text_from_html


def test_summary_fallback_uses_first_sentences():
    text = "First useful sentence. Second useful sentence. Third useful sentence. Fourth sentence."
    summary = summarise_text("Demo", text, max_sentences=2)
    assert summary == "First useful sentence. Second useful sentence."


def test_text_extraction_helper_ignores_script_content():
    html = "<main><h1>Visible title</h1><p>Useful text.</p><script>ignored()</script></main>"
    assert extract_text_from_html(html) == "Visible title Useful text."
