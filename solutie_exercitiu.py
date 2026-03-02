a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

print(a > b)

operation == "+" and (result := a + b)
operation == "-" and (result := a - b)
operation == "*" and (result := a * b)
operation == "/" and (result := a / b)

operation == "+" and print(f"Result: {a + b}")
operation == "-" and print(f"Result: {a - b}")
operation == "*" and print(f"Result: {a * b}")
operation == "/" and print(f"Result: {a / b}")

print(f"Result: {result}")
