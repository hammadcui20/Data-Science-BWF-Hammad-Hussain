try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
    
try:
    result = 10 / "a"
except ZeroDivisionError:
    print("Cannot divide by zero")
except TypeError:
    print("Invalid type for division")