def greet(name):
    return f"Hello, {name}"

say_hello = greet
print(say_hello("Alice"))  

def call_function(func, arg):
    return func(arg)

result = call_function(greet, "Bob")
print(result)  
