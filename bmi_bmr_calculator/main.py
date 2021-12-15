from bmi import BMICalculator
from bmr import BMRCalculator


def main():
    done = False
    print("💪 Calculate your BMI or BMR 💪")

    while not done:
        option = input("What do want to calculate?\n(BMI / BMR): ").upper()
        _format = int(input("Choose your format (1) cm/lb or (2) inch/kg: "))

        if _format == 1 or _format == 2:
            if option == "BMR":
                print("BMR")

                BMRCalculator().calculate()
                done = True
            elif option == "BMI":
                print("\nBMI")

                height = input("Your height is: ")
                weight = input("Your weight is: ")

                if _format == 1:
                    BMICalculator.cm_lb()
                elif _format == 2:
                    BMICalculator.inch_kg()

                BMICalculator().calculate(height=height, weight=weight)
                done = True
        else:
            print("\nIncorrect format! Please input 1 or 2")
    return


main()
