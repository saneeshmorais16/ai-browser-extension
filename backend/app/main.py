from fastapi import FastAPI

from app.form_helper import suggest_form_answer
from app.schemas import FormSuggestionRequest, FormSuggestionResponse, PageRequest, SummaryResponse, TasksResponse
from app.summariser import summarise_text
from app.task_extractor import extract_tasks

app = FastAPI(title="AI Browser Extension Demo Backend", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "mode": "rule-based"}


@app.post("/summarise", response_model=SummaryResponse)
def summarise(request: PageRequest) -> SummaryResponse:
    return SummaryResponse(title=request.title, summary=summarise_text(request.title, request.text))


@app.post("/tasks", response_model=TasksResponse)
def tasks(request: PageRequest) -> TasksResponse:
    return TasksResponse(tasks=extract_tasks(request.text))


@app.post("/suggest-form-answer", response_model=FormSuggestionResponse)
def form_answer(request: FormSuggestionRequest) -> FormSuggestionResponse:
    return FormSuggestionResponse(
        suggestion=suggest_form_answer(
            label=request.label,
            name=request.name,
            placeholder=request.placeholder,
            field_type=request.field_type,
            page_context=request.page_context,
        )
    )
