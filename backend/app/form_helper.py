def suggest_form_answer(label: str = "", name: str = "", placeholder: str = "", field_type: str = "text", page_context: str = "") -> str:
    joined = f"{label} {name} {placeholder} {field_type}".lower()
    context = page_context[:160].strip()
    if "email" in joined:
        return "demo@example.com"
    if "name" in joined:
        return "Demo User"
    if "message" in joined or "cover" in joined or "summary" in joined:
        return "Draft for review: I am interested in this opportunity and can provide relevant project examples."
    if "experience" in joined:
        return "Draft for review: I have practical experience with Python, automation and AI-assisted workflows."
    if context:
        return f"Draft for review based on page context: {context}"
    return "Draft for review. Edit this text before inserting it into the form."
