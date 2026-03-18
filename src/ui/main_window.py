import tkinter as tk
from .components import CalculatorButton, DisplayLabel
from ..sdk.calculator_sdk import CalculatorSDK

class MainWindow(tk.Tk):
    def __init__(self, sdk: CalculatorSDK):
        super().__init__()
        self.sdk = sdk
        self.config_data = sdk.get_config()
        
        self.title(self.config_data["window"]["title"])
        self.geometry(f"{self.config_data['window']['width']}x{self.config_data['window']['height']}")
        self.resizable(self.config_data["window"]["resizable"], self.config_data["window"]["resizable"])
        
        self.configure(bg="#ffffff")
        self._setup_ui()

    def _setup_ui(self):
        # Display Area
        display_cfg = self.config_data["display"]
        self.display = DisplayLabel(
            self, 
            bg=display_cfg["bg"], 
            fg=display_cfg["fg"], 
            font=tuple(display_cfg["font"]),
            text=self.sdk.get_display_text()
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=10)
        
        # Grid Configuration
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.grid_rowconfigure(i, weight=1)
        self.grid_rowconfigure(0, weight=0)

        # Button Layout
        buttons_cfg = self.config_data["buttons"]
        
        # Helper to create buttons
        def create_btn(text, row, col, cmd, category="numbers", colspan=1):
            cfg = buttons_cfg.get(category, buttons_cfg["numbers"])
            btn = CalculatorButton(
                self, 
                text=text, 
                command=cmd, 
                bg=cfg["bg"], 
                fg=cfg["fg"], 
                hover_bg=cfg["hover"],
                font=("Arial", 14, "bold")
            )
            btn.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
            return btn

        # Row 1: Actions & Division
        create_btn("AC", 1, 0, self._on_ac, "actions")
        create_btn("C", 1, 1, self._on_clear, "actions")
        create_btn("DEL", 1, 2, self._on_del, "actions")
        create_btn("/", 1, 3, lambda: self._on_op("/"), "operators")

        # Row 2: 7, 8, 9, *
        create_btn("7", 2, 0, lambda: self._on_digit("7"))
        create_btn("8", 2, 1, lambda: self._on_digit("8"))
        create_btn("9", 2, 2, lambda: self._on_digit("9"))
        create_btn("*", 2, 3, lambda: self._on_op("*"), "operators")

        # Row 3: 4, 5, 6, -
        create_btn("4", 3, 0, lambda: self._on_digit("4"))
        create_btn("5", 3, 1, lambda: self._on_digit("5"))
        create_btn("6", 3, 2, lambda: self._on_digit("6"))
        create_btn("-", 3, 3, lambda: self._on_op("-"), "operators")

        # Row 4: 1, 2, 3, +
        create_btn("1", 4, 0, lambda: self._on_digit("1"))
        create_btn("2", 4, 1, lambda: self._on_digit("2"))
        create_btn("3", 4, 2, lambda: self._on_digit("3"))
        create_btn("+", 4, 3, lambda: self._on_op("+"), "operators")

        # Row 5: 0, ., =
        create_btn("0", 5, 0, lambda: self._on_digit("0"), colspan=2)
        create_btn(".", 5, 2, self._on_decimal)
        create_btn("=", 5, 3, self._on_equals, "equals")

    def _update_display(self):
        self.display.config(text=self.sdk.get_display_text())

    def _on_digit(self, d):
        self.sdk.press_digit(d)
        self._update_display()

    def _on_decimal(self):
        self.sdk.press_decimal()
        self._update_display()

    def _on_op(self, op):
        self.sdk.press_operator(op)
        self._update_display()

    def _on_equals(self):
        self.sdk.press_equals()
        self._update_display()

    def _on_ac(self):
        self.sdk.press_all_clear()
        self._update_display()

    def _on_clear(self):
        self.sdk.press_clear()
        self._update_display()

    def _on_del(self):
        self.sdk.press_backspace()
        self._update_display()
