def calc_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    else:
        return "Overweight"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = calc_bmi(weight,height)
    print("Your BMI: ", bmi)
    print("You are "+classify_bmi(bmi))


if __name__ == "__main__":
    main()