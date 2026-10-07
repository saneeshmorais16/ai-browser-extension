from typing import Literal

from pydantic import BaseModel, Field


SupportedFieldType = Literal["text", "email", "search", "url", "tel", "textarea"]


class PageRequest(BaseModel):
    title: str = Field("", max_length=300)
    url: str = Field("", max_length=2000)
    text: str = Field(default="", max_length=20000)


class SummaryResponse(BaseModel):
    title: str
    summary: str
    mode: str = "rule-based"


class TasksResponse(BaseModel):
    tasks: list[str]
    mode: str = "rule-based"


class FormSuggestionRequest(BaseModel):
    label: str = Field("", max_length=300)
    name: str = Field("", max_length=120)
    placeholder: str = Field("", max_length=300)
    # Only accept editable text-like fields. Passwords and hidden fields stay out of scope.
    field_type: SupportedFieldType = "text"
    page_context: str = Field("", max_length=20000)


class FormSuggestionResponse(BaseModel):
    suggestion: str
    requires_review: bool = True
    auto_submit: bool = False
