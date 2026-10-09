from fastapi.testclient import TestClient
import main
import os
import pytest

client = TestClient(main.app)


@pytest.fixture
def test_database(monkeypatch):
    monkeypatch.setattr(main, "DATABASE", "test_learning_tracker.db")
    if os.path.exists("test_learning_tracker.db"):
        os.remove("test_learning_tracker.db")
    main.create_table()
    yield
    if os.path.exists("test_learning_tracker.db"):
        os.remove("test_learning_tracker.db")


def test_get_goals(test_database):
    response = client.get("/goals")
    assert response.status_code == 200


def test_create_goal(test_database):
    response = client.post(
        "/goals", json={"title": "Learn FastAPI", "status": "In progress"}
    )

    assert response.status_code == 200

    data = response.json()
    assert data["title"] == "Learn FastAPI"
    get_response = client.get("/goals")
    goals = get_response.json()

    assert len(goals) == 1
    assert goals[0]["title"] == "Learn FastAPI"


def test_get_missing_goal(test_database):
    response = client.get("/goals/999")
    assert response.status_code == 404


def test_update_goal(test_database):
    response = client.post(
        "/goals", json={"title": "Learn Python", "status": "In progress"}
    )
    data = response.json()
    goal_id = data["id"]
    update_response = client.patch(f"/goals/{goal_id}", json={"status": "completed"})

    assert update_response.status_code == 200
    updated_data = update_response.json()
    assert updated_data["status"] == "completed"
    assert updated_data["title"] == "Learn Python"

    get_response = client.get(f"/goals/{goal_id}")

    saved_data = get_response.json()

    assert saved_data["status"] == "completed"


def test_delete_goal(test_database):
    response = client.post(
        "/goals", json={"title": "Learn SQL", "status": "In progress"}
    )
    data = response.json()
    goal_id = data["id"]

    delete_response = client.delete(f"/goals/{goal_id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/goals/{goal_id}")

    assert get_response.status_code == 404


def test_create_invalid_goal(test_database):
    response = client.post("/goals", json={"title": "Learn Python"})

    assert response.status_code == 422
