import re


def summarise_text(title: str, text: str, max_sentences: int = 3) -> str:
    clean = " ".join(text.split())
    if not clean:
        return f"No visible page text was provided for {title or 'this page'}."

    sentences = [sentence.strip() for sentence in re.split(r"(?<=[.!?])\s+", clean) if sentence.strip()]
    selected = sentences[:max_sentences]
    if not selected:
        selected = [clean[:260]]
    summary = " ".join(selected)
    return summary[:700]
