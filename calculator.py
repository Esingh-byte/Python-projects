a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

ch = input("Enter any of these characters for specific operations (+, -, *, /): ")

if ch == "+":
    print("Sum =", a + b)
elif ch == "-":
    print("Subtraction =", a - b)
elif ch == "*":
    print("Multiplication =", a * b)
elif ch == "/":
    if b == 0:
        print("Division by zero is not allowed!")
    else:
        print("Division =", a / b)
else:
    print("Invalid operator!")