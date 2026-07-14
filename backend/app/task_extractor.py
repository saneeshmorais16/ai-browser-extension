import re

ACTION_KEYWORDS = {
    "apply",
    "submit",
    "review",
    "prepare",
    "download",
    "contact",
    "complete",
    "compare",
    "schedule",
    "upload",
}


def extract_tasks(text: str, limit: int = 6) -> list[str]:
    sentences = [item.strip(" .") for item in re.split(r"(?<=[.!?])\s+", text) if item.strip()]
    tasks = []
    for sentence in sentences:
        lower = sentence.lower()
        if any(keyword in lower for keyword in ACTION_KEYWORDS):
            tasks.append(sentence)
    if not tasks:
        tasks = ["Review the page content", "Confirm whether any action is required", "Check details before submitting anything"]
    return tasks[:limit]
