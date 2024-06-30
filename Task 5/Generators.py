def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)
print(next(counter)) 
print(next(counter)) 


squares = (x**2 for x in range(10))
print(next(squares))  
print(next(squares))  
