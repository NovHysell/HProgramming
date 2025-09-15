# Create a lambda function
add = lambda x, y: x + y

# Create subtract, multiply, divide
# Create a countermeasure for divide if y = 0
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Error: division by zero"

# Create a list of tuples
inputs = [(1, 3), (9, 7), (10, 8)]
for x, y in inputs:
    print(f"Inputs: {x}, {y}")
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")
    print(f"Multiply: {multiply(x, y)}")
    print(f"Divide: {divide(x, y)}")