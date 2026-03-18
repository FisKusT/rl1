# Python GUI Calculator - Clean Architecture Implementation
# TEST CHANGE
## a. Objective
The goal of this project is to build a robust, desktop-based Graphical User Interface (GUI) calculator using Python. It demonstrates strict software engineering standards, including:
* **Clean Architecture:** Complete isolation between core math logic, SDK, and UI.
* **TDD (Test-Driven Development):** 100% logic coverage with high-precision arithmetic.
* **Config-Driven UI:** Zero hard-coding; all styles and constraints are managed via JSON.

---

## b. Installation

### Windows (PowerShell)
```powershell
# Clone or navigate to the project directory
cd C:\Users\sorte\Desktop\BIU\Recitation\RL_Course\rl1\

# Create a virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/main.py
```

### Linux & macOS
```bash
# Navigate to the project directory
cd /path/to/rl1/

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python3 src/main.py
```

---

## c. User Manual
1. **Basic Math:** Use digits (0-9) and operators (+, -, *, /) for standard calculations.
2. **Decimal:** Press `.` to add a decimal point (only one allowed per number).
3. **Actions:**
   * **AC (All Clear):** Resets the entire calculator state.
   * **C (Clear):** Clears only the current input field.
   * **DEL (Delete):** Removes the last character typed.
4. **Result:** Press `=` to execute the operation. Results exceeding 15 characters automatically switch to **Scientific Notation**.
5. **Errors:** Division by zero will display "Error".

---

## d. Config File Description (`config/settings.json`)
The application is fully customizable via `settings.json`:
* **window:** Set the title, dimensions, and resizability.
* **display:** Configure font family, size, background (`bg`), and text colors (`fg`).
* **buttons:** Define color palettes for `numbers`, `operators`, `actions`, and the `equals` button, including `hover` effects.
* **logic:** Set the floating-point `precision` (default: 10).

---

## e. File Structure
```text
rl1/
├── config/
│   └── settings.json       # UI strings, colors, window dimensions
├── src/
│   ├── core/
│   │   ├── engine.py       # Math logic & state management (Decimal module)
│   │   └── interfaces.py   # Abstract base classes
│   ├── ui/
│   │   ├── components.py   # Custom Tkinter widgets (HoverButton, etc.)
│   │   └── main_window.py  # Layout & Event binding
│   ├── sdk/
│   │   └── calculator_sdk.py # Wrapper for core communication & formatting
│   └── main.py             # Entry point
├── tests/
│   ├── test_engine.py      # Core logic unit tests (Pytest)
│   └── test_ui.py          # UI integration tests
├── .flake8                 # PEP 8 Linter configuration
├── requirements.txt        # pytest, coverage, flake8
└── README.md
```

---

## f. GUI Picture Examples
*(Note: Placeholder for visual description as images cannot be rendered in Markdown text here)*
* **Modern Grid:** A 4x5 grid with distinct color coding (Gray for numbers, Orange for operators).
* **Interactive Feedback:** Buttons subtly change color when hovered.
* **Clean Display:** Large, right-aligned text area at the top.

---

## g. Unit Test Explanation
The project uses `pytest` and the `coverage` library to ensure reliability:
* **Engine Tests:** 18+ tests covering addition, subtraction, multiplication, division, decimal handling, and complex state transitions.
* **Precision Check:** Tests verify that `0.1 + 0.2` exactly equals `0.3` using Python's `decimal` module.
* **Edge Cases:** Explicit tests for `ZeroDivisionError` and empty input handling.
* **Coverage:** Achieves **>90% code coverage** in the core engine.

To run tests:
```bash
pytest tests/test_engine.py
```

---

## h. Copyright & Course Info
**Student Name:** Tal Fiskus  
**Course:** BIU Reinforcement Learning (RL)  
**Course No.:** 896873  
**Institution:** Bar Ilan University (BIU)  
**Copyright © 2026**
