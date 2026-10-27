def display_menu():
    print("================================")
    print("         BMI CALCULATOR")
    print("================================")
    print("1. Calculate BMI")
    print("2. View BMI Categories")
    print("3. Exit")
    print("================================")


while True:
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("\nEnter your name: ")
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            print("\nInvalid input. Weight and height must be greater than zero.")
            continue

        bmi = weight / (height * height)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        print("\n================================")
        print("           BMI RESULT")
        print("================================")
        print(f"Name: {name}")
        print(f"Weight: {weight} kg")
        print(f"Height: {height} m")
        print(f"BMI: {bmi:.2f}")
        print(f"Category: {category}")
        print("================================")

    elif choice == "2":
        print("\nBMI CATEGORIES")
        print("Below 18.5       : Underweight")
        print("18.5 to below 25 : Normal weight")
        print("25 to below 30   : Overweight")
        print("30 and above     : Obesity")

    elif choice == "3":
        print("\nThank you for using the BMI Calculator!")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")
