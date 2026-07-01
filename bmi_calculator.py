# BMI Calculation
# input weight in kg and height in m
weight = round(float(input("Enter your weight in kg: ")), 2)
height = round(float(input("Enter your height in m: ")), 2)

# BMI formula
bmi = weight / (height**2)

# Print BMI value
print(f"Your BMI value is: {round(bmi,2)}")  # you can do {bmi:.2f}

# category status based on BMI value
if bmi < 18.5:
    print("You are underweight.")
elif bmi >= 18.5 and bmi < 24.9:
    print("You are normal weight.")
elif bmi >= 25 and bmi < 29.9:
    print("You are overweight.")
elif bmi >= 30:
    print("You are obese.")
else:
    print("Invalid BMI value.")
