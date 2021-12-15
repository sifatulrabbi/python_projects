from converter import Converter


class BMICalculator:
    def __init__(self) -> None:
        pass

    def calculate(self, height, weight) -> int:
        if not height and not weight:
            print("Height and weight is needed for calculation")
            return

        print(f"your height is: {height} and weight is: {weight}")

    def cm_lb(self):
        return 1

    def inch_kg(self):
        return 1
