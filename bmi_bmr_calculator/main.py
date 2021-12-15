from calculator import Calculator


def main():
    calculator = Calculator()
    print("💪 Calculate your BMI or BMR 💪")

    done = False

    while not done:
        mode = int(input("Choose your format (1) cm/kg or (2) inch/lb: "))

        if mode == 1:
            calculator.set_mode("CM_KG")
            break
        elif mode == 2:
            calculator.set_mode("INCH_LB")
            break
        else:
            print("\nPlease input a valid mode 1 or 2!")

    while not done:
        height = float(input("Your height is: "))
        weight = float(input("Your weight is: "))
        age = int(input("Your age is: "))
        sex = input("Your sex is (male/female): ").upper()

        if sex == "MALE" or sex == "FEMALE":
            calculator.set_info(height=height, weight=weight, age=age, sex=sex)
            break

    calculator.calc_bmi()
    calculator.calc_bmr()


main()
