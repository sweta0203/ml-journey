print("--------------BMI Calculator--------------")

weight = input("Enter your weight in kg: ").strip()
height = input("Enter your height in m: ").strip()

try:
    weight = float(weight)
    height = float(height)

    if height <= 0 and weight <= 0:
        print("Height and weight must be greater than zero.")
    else:
        bmi = weight / (height * height)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi >= 18.5 and bmi < 24.9:
            category = "Normal weight"
        elif bmi >= 25 and bmi < 29.9:
            pcategory = "Overweight"
        else:
            category = "Obesity"
    print(f"Your BMI is: {bmi:.2f}")
    print(f"BMI category: {category}")
except ValueError:
    print("Please enter valid numeric values for weight and height.")
