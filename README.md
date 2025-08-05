# 📈 Productivity Manager

**Productivity Manager** is a command-line Python application designed to help users stay organized and build better daily routines. It consists of two key features:

- **Task List:** Add, view, and remove daily tasks.
- **Habit Tracker:** Track your habits, log entries by date, and monitor consistency over time.

The interface uses the [`rich`](https://github.com/Textualize/rich) library for a visually enhanced experience with styled tables, input prompts, and clean console output.

---

## 🗂️ Project Structure

- `project.py` – Core logic for the task and habit manager with an interactive menu system.
- `project_data.json` – Stores the user’s tasks and habit logs persistently.
- `test_project.py` – Contains tests for key functions like `load_data()` and `save_data()` using `pytest`.

---

## 🧪 Testing

Unit tests are written using `pytest`. Temporary files are used (`tmp_path`) during testing to avoid modifying the original data.

---

## 💡 Design Decisions

- Focused scope limited to tasks and habits for clarity and usability.
- Styled, clean CLI using `rich` for enhanced user interaction.
- JSON for persistent, human-readable data storage.
- Modular functions and isolated logic for easy testing and maintenance.

---

## ✅ Requirements

- Python 3.8+
- `rich==14.0.0`
- `pytest` (for testing)

Install dependencies:

```bash
pip install -r requirements.txt

