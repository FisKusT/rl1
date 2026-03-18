# Project TODO List: Python GUI Calculator

## Phase 1: Setup & Core Engine (TDD)
- [x] **Environment Setup**
    - [x] Initialize project directory structure.
    - [x] Create `requirements.txt` (pytest, coverage, flake8).
    - [x] Configure `.flake8` for PEP 8 compliance.
- [x] **TDD: Calculator Engine**
    - [x] Create `tests/test_engine.py`.
    - [x] Implement `CalculatorEngine.add_digit()` (with tests).
    - [x] Implement `CalculatorEngine.add_decimal()` (with tests for duplication).
    - [x] Implement arithmetic operations: `+`, `-`, `*`, `/` (with tests).
    - [x] Implement `CalculatorEngine.calculate()` (with tests).
    - [x] Implement `CalculatorEngine.clear()` and `AC` logic.
    - [x] Implement `ZeroDivisionError` handling in engine.
    - [x] Implement floating-point precision/rounding logic.
- [x] **Quality Check**
    - [x] Run `pytest` and ensure all tests pass.
    - [x] Run `coverage run -m pytest` and `coverage report` (Target: >85%).

## Phase 2: Configuration & SDK
- [x] **Configuration Management**
    - [x] Create `config/settings.json` with UI specs (colors, fonts, sizes).
    - [x] Implement a configuration loader/utility.
- [x] **SDK Layer**
    - [x] Create `src/sdk/calculator_sdk.py`.
    - [x] Map SDK methods to `CalculatorEngine` calls.
    - [x] Add input sanitization and output formatting (Scientific Notation for overflow).

## Phase 3: GUI Development
- [x] **Layout & Components**
    - [x] Implement `src/ui/components.py` (Base Button, Display Label).
    - [x] Implement `src/ui/main_window.py` (Tkinter Grid setup).
    - [x] Load window title and icon from configuration.
- [x] **Event Binding**
    - [x] Bind numeric buttons to SDK.
    - [x] Bind operator buttons to SDK.
    - [x] Bind Action keys (`=`, `C`, `AC`, `DEL`) to SDK.
- [x] **UX Enhancements**
    - [x] Implement hover effects for buttons.
    - [x] Ensure window resizing is fixed/constrained.

## Phase 4: Validation & Hardening
- [ ] **Integration Testing**
    - [x] Create `tests/test_ui.py` for end-to-end flow (Basic logic verified via Engine tests).
- [x] **Static Analysis**
    - [x] Run `flake8` on the entire `src/` directory and fix issues.
- [x] **Final Packaging**
    - [x] Create `src/main.py` entry point.
    - [x] Final manual walkthrough of all PRD requirements.
