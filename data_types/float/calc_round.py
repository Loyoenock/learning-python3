#Adding two floats and returning an integer

num1 = float(input("Enter num1 "))
num2 = float(input("Enter num2 "))

num3 = round(num1 + num2)

# format our res"ult for larger numbers
print(f"{num3:,}")
