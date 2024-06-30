x = "global"

def my_function():
    x = "local"
    print(x)  

my_function()
print(x) 
def outer_function():
    def inner_function():
        print("This is the inner function")
    inner_function()

outer_function()  
