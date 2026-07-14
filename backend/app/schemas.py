from pydantic import BaseModel, Field


class PageRequest(BaseModel):
    title: str = ""
    url: str = ""
    text: str = Field(default="", max_length=20000)


class SummaryResponse(BaseModel):
    title: str
    summary: str
    mode: str = "rule-based"


class TasksResponse(BaseModel):
    tasks: list[str]
    mode: str = "rule-based"


class FormSuggestionRequest(BaseModel):
    label: str = ""
    name: str = ""
    placeholder: str = ""
    field_type: str = "text"
    page_context: str = ""


class FormSuggestionResponse(BaseModel):
    suggestion: str
    requires_review: bool = True
    auto_submit: bool = False
