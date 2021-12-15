from converter import Converter


class BMICalculator:
    __converter: Converter

    def __init__(self) -> None:
        self.__converter = Converter()
        pass

    def __calculate(self, height: float, weight: float) -> None:
        bmi = weight / (height * height)
        formated_bmi = "{:.2f}".format(bmi)

        print(f"\nYour BMI is: {formated_bmi}")

    def cm_lb(self, height: float, weight: float) -> None:
        meter_height = self.__converter.cm_to_meter(height)
        kg_weight = self.__converter.lb_to_kg(weight)

        self.__calculate(meter_height, kg_weight)

    def inch_kg(self, height: float, weight: float) -> None:
        meter_height = self.__converter.inch_to_meter(height)

        self.__calculate(meter_height, weight)
