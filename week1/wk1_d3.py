import random

# for loop
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

for i in range(1, 11):
    if i == 5:
        break  # continue
    print(i)

# enumarate() : gives both index and value of the list
for index, value in enumerate(fruits):
    print(index, value)

for index, value in enumerate(fruits, start=1):
    print(index, value)


# while loop
count = 1
while count <= 10:
    print(count)
    count += 1

password = int(input("Enter your password: "))

while password == 1234:
    print("Access granted")
    break

# random
number = random.randint(1, 10)  # random int
number1 = random.choice(fruits)  # random choice from list
number2 = random.random()  # random float between 0 and 1
number3 = random.uniform(1, 10)  # random float between 1 and 10
random.shuffle(fruits)  # shuffle the list in place
