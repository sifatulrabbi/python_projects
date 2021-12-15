from typing import Literal
from converter import Converter


class Calculator:
    __converter = Converter()
    __height: float
    __weight: float
    __age: int
    __sex: str
    __mode: str

    def __init__(self):
        pass

    def set_mode(self, mode: str):
        if mode == "CM_KG" or mode == "INCH_LB":
            self.__mode = mode
            return

        raise "Mode should be either 'CM_KG' or 'INCH_LB'"

    def set_info(self, height: float, weight: float, age: int, sex: str):
        self.__height = height
        self.__weight = weight
        self.__age = age

        if sex == "MALE" or sex == "FEMALE":
            self.__sex = sex
        else:
            raise "Sex has to be 'MALE' or 'FEMALE'"

    def calc_bmi(self) -> float:
        height: float
        weight: float

        if self.__mode == "CM_KG":
            height = self.__converter.cm_to_meter(self.__height)
            weight = self.__weight
        elif self.__mode == "INCH_LB":
            height = self.__converter.inch_to_meter(self.__height)
            weight = self.__converter.lb_to_kg(self.__weight)

        bmi = "{:.2f}".format(weight / (height * height))
        print(f"\nYour BMI is: {bmi}\n")

    def calc_bmr(self) -> float:
        height: float
        weight: float
        age = self.__age
        deduction: int = 5 if self.__sex == "MALE" else (-161)

        if self.__mode == "CM_KG":
            height = self.__height
            weight = self.__weight
        elif self.__mode == "INCH_LB":
            height = self.__converter.inch_to_cm(self.__height)
            weight = self.__converter.lb_to_kg(self.__weight)

        bmr = (10 * weight + 6.25 * height - 5 * age + deduction).__floor__()

        print(f"Your BMR is: {bmr} cal\n")
        print(
            f"Your calories chart is:\n"
            f"If you are sedentary (little or no exercise) : {(bmr * 1.2).__floor__()} cal\n"
            f"If you are lightly active (light exercise/sports 1-3 days/week) : {(bmr * 1.375).__floor__()} cal\n"
            f"If you are moderately active (moderate exercise/sports 3-5 days/week) : {(bmr * 1.55).__floor__()} cal\n"
            f"If you are very active (hard exercise/sports 6-7 days a week) : {(bmr * 1.725).__floor__()} cal\n"
            f"If you are extra active (very hard exercise/sports & physical job or 2x training) : {(bmr * 1.9).__floor__()} cal\n"
        )
