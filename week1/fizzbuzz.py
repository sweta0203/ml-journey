print("-------------------Fizzbuzz-------------------")
try:
    num = int(input("Enter a number: ").strip())
    # Loop
    for i in range(1, num + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
except ValueError:
    print("Please enter a valid integer.")
