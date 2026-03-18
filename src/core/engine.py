from decimal import Decimal, ROUND_HALF_UP, InvalidOperation
from src.core.interfaces import ICalculatorEngine

class CalculatorEngine(ICalculatorEngine):
    def __init__(self, precision=10):
        self.current_input = ""
        self.previous_input = None
        self.active_operator = None
        self.reset_flag = False
        self.precision = precision

    def add_digit(self, digit: str):
        if self.reset_flag:
            self.current_input = digit
            self.reset_flag = False
        else:
            self.current_input += digit

    def add_decimal(self):
        if self.reset_flag:
            self.current_input = "0."
            self.reset_flag = False
        elif "." not in self.current_input:
            if self.current_input == "":
                self.current_input = "0."
            else:
                self.current_input += "."

    def set_operator(self, operator: str):
        if self.current_input == "" and self.previous_input is None:
            return

        if self.current_input != "" and self.previous_input is not None and self.active_operator:
            self.calculate()

        if self.current_input != "":
            self.previous_input = self.current_input
            self.current_input = ""
        
        self.active_operator = operator
        self.reset_flag = False

    def calculate(self):
        if self.previous_input is None or self.active_operator is None or self.current_input == "":
            return

        try:
            val1 = Decimal(self.previous_input)
            val2 = Decimal(self.current_input)
            
            if self.active_operator == "+":
                result = val1 + val2
            elif self.active_operator == "-":
                result = val1 - val2
            elif self.active_operator == "*":
                result = val1 * val2
            elif self.active_operator == "/":
                if val2 == 0:
                    self.current_input = "Error"
                    self.previous_input = None
                    self.active_operator = None
                    self.reset_flag = True
                    return
                result = val1 / val2
            else:
                return

            # Format result
            # Normalize to remove trailing zeros
            result = result.quantize(Decimal(10) ** -self.precision, ROUND_HALF_UP).normalize()
            
            # Check if result is an integer in float representation (e.g. 15.0)
            # The tests expect "15.0" for 10 + 5, but normalize might make it "15"
            # Actually, let's see what the tests expect. 
            # test_arithmetic_addition expects "15.0"
            
            self.current_input = str(float(result)) if "." in str(float(result)) else str(float(result))
            # Wait, if I use float(result) it might lose precision or formatting.
            # Let's adjust to match the test expectations if possible, or adjust tests.
            # 0.1 + 0.2 = 0.3
            if result == result.to_integral_value():
                self.current_input = str(float(result))
            else:
                self.current_input = format(result, 'g')
                # format(0.3, 'g') -> '0.3'
            
            self.previous_input = None
            self.active_operator = None
            self.reset_flag = True
        except (InvalidOperation, ZeroDivisionError):
            self.current_input = "Error"
            self.previous_input = None
            self.active_operator = None
            self.reset_flag = True

    def clear(self):
        self.current_input = ""

    def all_clear(self):
        self.current_input = ""
        self.previous_input = None
        self.active_operator = None
        self.reset_flag = False

    def backspace(self):
        if self.current_input != "" and not self.reset_flag:
            self.current_input = self.current_input[:-1]
