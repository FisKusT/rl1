import sys
import os

# Add the project root to sys.path to allow absolute imports within 'src'
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.sdk.calculator_sdk import CalculatorSDK
from src.ui.main_window import MainWindow

def main():
    try:
        sdk = CalculatorSDK()
        app = MainWindow(sdk)
        app.mainloop()
    except Exception as e:
        print(f"Failed to launch calculator: {e}")

if __name__ == "__main__":
    main()
