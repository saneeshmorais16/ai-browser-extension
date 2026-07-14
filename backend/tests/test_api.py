from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_summarise_endpoint():
    response = client.post("/summarise", json={"title": "Demo", "text": "One. Two. Three. Four."})
    assert response.status_code == 200
    assert response.json()["mode"] == "rule-based"
    assert "One" in response.json()["summary"]


def test_tasks_endpoint():
    response = client.post("/tasks", json={"text": "Review the instructions. Submit only after checking."})
    assert response.status_code == 200
    assert response.json()["tasks"]


def test_form_suggestion_never_auto_submits():
    response = client.post("/suggest-form-answer", json={"label": "Email"})
    assert response.status_code == 200
    assert response.json()["requires_review"] is True
    assert response.json()["auto_submit"] is False
