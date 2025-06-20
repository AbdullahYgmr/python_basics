print("Division operation")

try:
    numerator = float(input("Please enter the first number: "))
    denominator = float(input("Please enter the second number: "))
    result = numerator / denominator
    print("The result of the division is:", result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("A number cannot be divided by zero.")
