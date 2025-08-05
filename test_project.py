from project import load_data, save_data, handle_task
import json

def test_load_data():
    data = load_data()
    assert isinstance(data, dict)
    assert "tasks" in data
    assert "habits" in data


def test_save_data(tmp_path):

    test_file = tmp_path / "test_data.json"
    test_data = {
        "tasks": ["task1", "task2"],
        "habits": [{"name": "Exercise", "log": ["2025-07-22"]}]
    }

    save_data(test_data, filename=test_file)

    with open(test_file, "r") as file:
        result = json.load(file)
    assert result == test_data

def test_handle_task(tmp_path):
    data = {"tasks": [], "habits": []}
    data["tasks"].append("Test Task")
    assert "Test Task" in data["tasks"]

    test_file = tmp_path / "test_tasks.json"
    save_data(data, filename=test_file)

    data["tasks"].remove("Test Task")
    save_data(data, filename=test_file)

    with open(test_file, "r") as file:
        result = json.load(file)
    assert result["tasks"] == []
