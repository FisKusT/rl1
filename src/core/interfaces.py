from abc import ABC, abstractmethod

class ICalculatorEngine(ABC):
    @abstractmethod
    def add_digit(self, digit: str):
        pass

    @abstractmethod
    def add_decimal(self):
        pass

    @abstractmethod
    def set_operator(self, operator: str):
        pass

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def all_clear(self):
        pass

    @abstractmethod
    def backspace(self):
        pass
