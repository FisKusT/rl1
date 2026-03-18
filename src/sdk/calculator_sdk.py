import json
import os
from src.core.engine import CalculatorEngine

class CalculatorSDK:
    def __init__(self, config_path=None):
        if config_path is None:
            # Assume relative to project root
            config_path = os.path.join(os.path.dirname(__file__), "..", "..", "config", "settings.json")
        
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
        precision = self.config.get("logic", {}).get("precision", 10)
        self.engine = CalculatorEngine(precision=precision)
        self.max_chars = self.config.get("display", {}).get("max_chars", 15)

    def get_display_text(self):
        text = self.engine.current_input
        if text == "":
            return "0"
        
        if text == "Error":
            return text
        
        # Handle overflow/scientific notation
        if len(text) > self.max_chars:
            try:
                val = float(text)
                return "{:.2e}".format(val)
            except ValueError:
                return text[:self.max_chars]
        
        return text

    def press_digit(self, digit: str):
        self.engine.add_digit(digit)

    def press_decimal(self):
        self.engine.add_decimal()

    def press_operator(self, operator: str):
        self.engine.set_operator(operator)

    def press_equals(self):
        self.engine.calculate()

    def press_clear(self):
        self.engine.clear()

    def press_all_clear(self):
        self.engine.all_clear()

    def press_backspace(self):
        self.engine.backspace()

    def get_config(self):
        return self.config
