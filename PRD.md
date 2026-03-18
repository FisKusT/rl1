# Product Requirements Document (PRD): GUI Calculator Application

**Document Version:** 1.0
**Product Name:** Python GUI Calculator
**Status:** Draft / Ready for Development

---

## 1. Product Overview
The goal of this project is to build a robust, desktop-based Graphical User Interface (GUI) calculator. The application will handle standard arithmetic operations while adhering to strict software engineering standards, including Test-Driven Development (TDD), Object-Oriented Programming (OOP), and Clean Architecture principles.

---

## 2. Technical & Architecture Requirements (Non-Functional)
The foundational codebase must strictly adhere to the following engineering standards:

* **Core Language:** Python.
* **Architecture Pattern:** Clean Architecture. The core domain logic (math engine) must be completely isolated from the UI, data layers, and external modules.
* **Development Methodology (TDD):** Test-Driven Development is mandatory. Failing tests must be written prior to feature implementation.
* **Object-Oriented Programming (OOP):** The codebase must utilize OOP principles. Strictly adhere to the DRY (Don't Repeat Yourself) principle. Code duplication is prohibited; shared logic must be abstracted.
* **Quality Assurance:** * Maintain a minimum of **85% code coverage** via comprehensive unit tests.
    * Integrate static code analysis (linter, e.g., Pylint, Flake8) to enforce PEP 8 standards, catch syntax errors, and maintain quality.
* **Configuration Management:** Zero hard-coding. All dynamic and static data (file names, dimensions, dates, UI strings, theme colors) must be read from an external configuration file (e.g., JSON, YAML, or `.ini`).
* **External Communication (SDK):** All business logic interfacing with the external world (GUI rendering, network, file systems) must be abstracted and executed via an internal SDK or dedicated wrapper classes.

---

## 3. User Interface (UI) & User Experience (UX)

### 3.1 Window & Layout
* **Window Constraints:** Fixed/constrained dimensions to prevent layout distortion upon resizing. Custom application title and app icon required.
* **Grid System:** Utilize a precise 4x5 or 5x5 grid layout for button placement.
* **Display Area:** * Read-only text field or label.
    * Positioned at the top of the window.
    * Right-aligned text with a large, highly readable font.

### 3.2 Button Mapping & Placement
* **Numbers (0-9):** Standard numpad layout (7-8-9 on the top row, 1-2-3 on the bottom row).
* **Operators (+, -, *, /):** Grouped logically, typically on the right side or top row.
* **Action Keys:** Equals (`=`), Decimal (`.`), Clear (`C`), All Clear (`AC`), and Backspace/Delete (`DEL`).

### 3.3 Styling & Feedback
* **Visual Hierarchy:** Apply distinct background colors to separate concerns (e.g., numbers = light gray, operators = accent color, equals = heavily highlighted).
* **Interactive Feedback:** Implement subtle hover effects (color change) when the cursor is over interactive buttons.

---

## 4. Functional Requirements

### 4.1 State Management
The application must track the following states to execute calculations correctly:

| State Variable | Type | Description |
| :--- | :--- | :--- |
| `current_input` | String | Holds the number currently being typed by the user. |
| `previous_input` | String/Float | Stores the first operand after an operator is pressed. |
| `active_operator` | String | Stores the currently selected mathematical operation. |
| `reset_flag` | Boolean | Determines if the display should clear upon next input (e.g., true after pressing `=`). |

### 4.2 Core Logic & Event Handling
* **Number Input:** Append the clicked digit to the `current_input` string and update the UI display. 
* **Decimal Input:** Verify if a decimal already exists in `current_input`. If false, append `.`. If true, ignore the input.
* **Operator Selection:**
    1.  Transfer `current_input` to `previous_input`.
    2.  Store the selected operator in `active_operator`.
    3.  Clear the display OR set the `reset_flag` to true to prepare for the second operand.
* **Calculation Execution (Equals `=`)**:
    1.  Parse `previous_input` and `current_input` into floats/decimals.
    2.  Execute the mathematical operation based on `active_operator`.
    3.  Convert the output back to a string and update the UI.
    4.  Set the `reset_flag` to true so the next numeric input starts a new calculation sequence.

---

## 5. Error Handling & Edge Cases

The application must gracefully handle the following scenarios without crashing:

* **ZeroDivisionError:** Catch division by zero and output `"Error"` or `"Undefined"` to the display.
* **Floating Point Precision:** Round outputs to a sensible decimal limit to prevent visual inaccuracies (e.g., `0.1 + 0.2` must equal `0.3`, not `0.30000000000000004`).
* **Display Overflow:** Impose a maximum character limit on user input to prevent text from pushing outside the UI display boundaries. Format excessively large calculation results into scientific notation.
* **Multiple Operator Inputs:** If a user presses multiple operators sequentially (e.g., `+` then immediately `*`), update the `active_operator` state to the most recent choice without breaking the input string.
* **Empty Equals/Operator Execution:** If `=` or an operator is pressed without sufficient operands, safely do nothing or return the current number.

---

## 6. Phase 2: Advanced Features (Optional Scope)

If core requirements are met, the following features are prioritized for V2:

1.  **Keyboard Integration:** Map physical keyboard keys (Numpad, Enter, Backspace, Escape) to trigger GUI buttons.
2.  **History Log:** Implement a collapsible side panel or dropdown menu to store and display past calculations.
3.  **Scientific Mode:** Add a UI toggle to reveal an extended grid with advanced mathematical operators (Square Root, Exponents, Pi, Percentages).
4.  **Theming:** Add a toggle to switch the global UI between Dark Mode and Light Mode, reading color palettes from the configuration file.
