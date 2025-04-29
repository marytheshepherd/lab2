def menu():
    print('displaying main menu')
    user = input("Enter some numbers separated by commas: ")
    numbers = [float(x) for x in user.split(",")]
    return numbers

def calculations(numbers):
    avg = sum(numbers)/len(numbers)
    
    numbers.sort()
    min = numbers[0]
    max = numbers[-1]
 
    middle = len(numbers)//2
    if len(numbers) % 2 == 1:
        median = numbers[middle]
    else:
        median = ((numbers[middle-1] + numbers[middle]) / 2)
        
    return avg, min, max, median


def main():
    numbers = menu()
    results = calculations(numbers)
    print("Average: ", results[0])
    print("Minimum: ", results[1])
    print("Maximum: ", results[2])
    print("Median: ", results[3])

if __name__ == "__main__":
    main()




