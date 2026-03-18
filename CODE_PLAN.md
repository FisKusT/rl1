# Engineering Implementation Plan: Python GUI Calculator

This document outlines the technical strategy for building the Python GUI Calculator according to the PRD, adhering to Clean Architecture and TDD principles.

---

## 1. Architectural Design (Clean Architecture)
To ensure isolation of concerns, the project will be divided into the following layers:

1.  **Domain (Core):** Pure Python logic for mathematical operations and state management. No dependencies on external libraries or the UI.
2.  **Application (SDK/Use Cases):** Orchestrates flow between the UI and the Domain logic.
3.  **Infrastructure/UI:** Implementation details (Tkinter/PyQt for GUI, JSON/YAML for config).

---

## 2. Project Structure
```text
rl1/
├── config/
│   └── settings.json       # UI strings, colors, window dimensions
├── src/
│   ├── core/
│   │   ├── engine.py       # Math logic & state management
│   │   └── interfaces.py   # Abstract base classes
│   ├── ui/
│   │   ├── components.py   # Custom button/display widgets
│   │   └── main_window.py  # Layout & Event binding
│   ├── sdk/
│   │   └── calculator_sdk.py # Wrapper for core communication
│   └── main.py             # Entry point
├── tests/
│   ├── test_engine.py      # Core logic unit tests
│   └── test_ui.py          # UI integration tests
├── .flake8                 # Linter configuration
├── requirements.txt
├── PRD.md
└── CODE_PLAN.md
```

---

## 3. Configuration Management
An external `settings.json` will store:
*   **Window:** Title, default width/height, icon path.
*   **Styles:** Background colors for different button types, font sizes, hover effect colors.
*   **Constants:** Max character limit for display, rounding precision.

---

## 4. Technical Strategy

### 4.1 State Management (`core/engine.py`)
A `CalculatorEngine` class will manage the internal state:
*   `current_input`: `str`
*   `previous_input`: `float`
*   `active_operator`: `str`
*   `reset_flag`: `bool`

Methods will include `add_digit(d)`, `set_operator(op)`, `calculate()`, and `clear()`.

### 4.2 GUI Implementation (`ui/`)
*   **Framework:** `tkinter` (Standard library, fits "Zero hard-coding" via config).
*   **Layout:** `grid` manager for the 4x5 button matrix.
*   **SDK Pattern:** The UI will never call `CalculatorEngine` directly. It will interact through `CalculatorSDK`, which handles data conversion and error sanitization.

### 4.3 TDD Workflow
1.  **Write Test:** Define a failing test in `tests/test_engine.py` (e.g., `test_addition`).
2.  **Implement Logic:** Add the minimal code in `core/engine.py` to pass.
3.  **Refactor:** Ensure DRY principles and OOP standards.
4.  **Repeat:** For decimals, division by zero, and operator switching.

---

## 5. Development Milestones

### Phase 1: Setup & Engine (TDD)
*   Initialize repository and linter.
*   Implement `CalculatorEngine` using TDD (arithmetic, precision, error handling).
*   Achieve 85% coverage on core logic.

### Phase 2: Configuration & SDK
*   Create `settings.json` and a config loader.
*   Implement `CalculatorSDK` to wrap engine calls.

### Phase 3: GUI Development
*   Build the main window and grid layout based on config.
*   Bind button clicks to SDK methods.
*   Implement visual feedback (hover effects).

### Phase 4: Validation & Hardening
*   Verify `ZeroDivisionError` handling and display overflow.
*   Run `flake8` for PEP 8 compliance.
*   Final integration testing.

---

## 6. Error & Edge Case Handling Logic
*   **Floating Point:** Use Python's `decimal` module or `round(result, precision)` where `precision` is fetched from config.
*   **Display Overflow:** If `len(display_str) > limit`, switch to scientific notation using `"{:.2e}".format(val)`.
*   **Operator Logic:** If `active_operator` is set and a new operator is clicked before a second operand, update `active_operator` without calculating.
