# Something new: This is an example of Generators. 
# A function which contains the yield keyword is a Generator.

def fibonacci(size):
    a = 0
    b = 1
    for num in range(size):
        yield a     # pauses the function and returns the value to the consumer of fibonacci, 
                    # but keeps the current state in order to be able to resume right after this yield
        
        old_a = a   # keep previous a
        a = b       # move to the next
        b = old_a + b


for x in fibonacci(5):
    print(x)
