def calc_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        print("You are Underweight")
        return -1
    elif bmi < 25.0:
        print("You are Healthy")
        return 0
    else:
        print("You are Overweight")
        return 1

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = calc_bmi(weight,height)
    print("Your BMI: ", bmi)
    classify_bmi(bmi)
    


if __name__ == "__main__":
    main()