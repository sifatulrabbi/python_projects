from converter import Converter


class BMICalculator:
    __converter: Converter

    def __init__(self) -> None:
        self.__converter = Converter()
        pass

    def __calculate(self, height: float, weight: float) -> float:
        bmi = weight / (height * height)
        formated_bmi = "{:.2f}".format(bmi)

        print(f"\nYour BMI is: {formated_bmi}")

    def cm_lb(self, height: float, weight: float):
        meter_height = self.__converter.cm_to_meter(height)
        kg_weight = self.__converter.lb_to_kg(weight)

        return self.__calculate(meter_height, kg_weight)

    def inch_kg(self, height: float, weight: float):
        meter_height = self.__converter.inch_to_meter(height)

        return self.__calculate(meter_height, weight)
