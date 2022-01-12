def add(a, b):
    c = a+b
    return c 
    
def my_function(a):
    if a < 0:
        return "Cannot do this on a negative number."
    x = a + 5
    y = a - 5
    return x,y 
    
#x = add(1,2)
x = my_function(1)
print(x)
print(x[0])
print(x[1])

first_answer, second_answer = my_function(1)
print(first_answer)
print(second_answer)
