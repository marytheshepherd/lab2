def menu():
    print('displaying main menu')
    user = input("Enter some numbers separated by commas: ")
    numbers = [float(x) for x in user.split(",")]
    return numbers

def calculations(numbers):
    avg = sum(numbers)/len(numbers)
    print("Average: ", avg)
    numbers.sort()
    min = numbers[0]
    print("Minimum: ", min)
    max = numbers[-1]
    print("Maximum: ", max)
    middle = len(numbers)//2
    if len(numbers) % 2 == 1:
        median = numbers[middle]
    else:
        median = ((numbers[middle-1] + numbers[middle]) / 2)
    print("Median: ", median)
    return 

def main():
    numbers = menu()
    calculations(numbers)

if __name__ == "__main__":
    main()




