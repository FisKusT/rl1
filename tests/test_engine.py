import pytest
from src.core.engine import CalculatorEngine

@pytest.fixture
def engine():
    return CalculatorEngine()

def test_add_digit(engine):
    engine.add_digit("1")
    assert engine.current_input == "1"
    engine.add_digit("2")
    assert engine.current_input == "12"

def test_add_decimal(engine):
    engine.add_digit("1")
    engine.add_decimal()
    assert engine.current_input == "1."
    engine.add_decimal()
    assert engine.current_input == "1."
    engine.add_digit("2")
    assert engine.current_input == "1.2"

def test_arithmetic_addition(engine):
    engine.add_digit("1")
    engine.add_digit("0")
    engine.set_operator("+")
    engine.add_digit("5")
    engine.calculate()
    assert engine.current_input == "15.0"

def test_arithmetic_subtraction(engine):
    engine.add_digit("1")
    engine.add_digit("0")
    engine.set_operator("-")
    engine.add_digit("4")
    engine.calculate()
    assert engine.current_input == "6.0"

def test_arithmetic_multiplication(engine):
    engine.add_digit("3")
    engine.set_operator("*")
    engine.add_digit("4")
    engine.calculate()
    assert engine.current_input == "12.0"

def test_arithmetic_division(engine):
    engine.add_digit("1")
    engine.add_digit("2")
    engine.set_operator("/")
    engine.add_digit("4")
    engine.calculate()
    assert engine.current_input == "3.0"

def test_division_by_zero(engine):
    engine.add_digit("5")
    engine.set_operator("/")
    engine.add_digit("0")
    engine.calculate()
    assert engine.current_input == "Error"

def test_clear(engine):
    engine.add_digit("5")
    engine.clear()
    assert engine.current_input == ""

def test_all_clear(engine):
    engine.add_digit("5")
    engine.set_operator("+")
    engine.add_digit("3")
    engine.all_clear()
    assert engine.current_input == ""
    assert engine.previous_input is None
    assert engine.active_operator is None

def test_reset_flag(engine):
    engine.add_digit("5")
    engine.set_operator("+")
    engine.add_digit("5")
    engine.calculate()
    assert engine.current_input == "10.0"
    engine.add_digit("2")
    assert engine.current_input == "2"

def test_sequential_operators(engine):
    engine.add_digit("5")
    engine.set_operator("+")
    engine.set_operator("*")
    engine.add_digit("2")
    engine.calculate()
    assert engine.current_input == "10.0"

def test_floating_point_precision(engine):
    engine.add_digit("0")
    engine.add_decimal()
    engine.add_digit("1")
    engine.set_operator("+")
    engine.add_digit("0")
    engine.add_decimal()
    engine.add_digit("2")
    engine.calculate()
    # 0.1 + 0.2 = 0.3
    assert engine.current_input == "0.3"

def test_backspace(engine):
    engine.add_digit("1")
    engine.add_digit("2")
    engine.backspace()
    assert engine.current_input == "1"
    engine.backspace()
    assert engine.current_input == ""
    engine.backspace()
    assert engine.current_input == ""

def test_set_operator_empty(engine):
    engine.set_operator("+")
    assert engine.active_operator is None

def test_chained_operations(engine):
    engine.add_digit("5")
    engine.set_operator("+")
    engine.add_digit("3")
    engine.set_operator("*")
    assert engine.previous_input == "8.0"
    assert engine.active_operator == "*"
    engine.add_digit("2")
    engine.calculate()
    assert engine.current_input == "16.0"

def test_calculate_no_operands(engine):
    engine.calculate()
    assert engine.current_input == ""
    engine.add_digit("5")
    engine.calculate()
    assert engine.current_input == "5"

def test_add_decimal_empty(engine):
    engine.add_decimal()
    assert engine.current_input == "0."

def test_add_decimal_after_calculate(engine):
    engine.add_digit("5")
    engine.set_operator("+")
    engine.add_digit("3")
    engine.calculate()
    engine.add_decimal()
    assert engine.current_input == "0."
