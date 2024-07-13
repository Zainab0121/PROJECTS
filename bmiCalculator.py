weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

def bmi_checker(height, weight):
    bmi = weight / height ** 2
    if bmi < 18.5:
        print("This person is underweight")
    elif 18.5 <= bmi < 24.9:
        print("This person is normal weight")
    elif 24.9 <= bmi < 29.9:
        print("This person is overweight")
    else:
        print("This person is obese")

bmi_checker(height, weight)
