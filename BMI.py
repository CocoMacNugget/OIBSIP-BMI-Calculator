print("Hello user and welcome to my BMI calculator!")

while True:
    try:
        weight = float(input("Enter your weight in kg: "))
        if weight <= 0:
            print("Enter value more than 0. Try again.")
        else:
            print(f"Your weight is: {weight}")
            break
    except ValueError:
        print("The value entered is invalid.")

while True:
    try:
        height = float(input("Enter your height in m: "))
        if height <= 0:
            print("Enter value more than 0. Try again.")
        else:
            print(f"Your height is: {height}")
            break
    except ValueError:
        print("The value entered is invalid.")

# BMI calculation
bmi = weight / height ** 2
print(f"Your weight of {weight}kg and height of {height}m give the BMI of {bmi:.2f}.")

# BMI conditions
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 25:
    print("Your weight is normal.")
elif 25 <= bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
