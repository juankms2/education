# Examples of exception handling
def get_age():
    attempt = 1
    while True:
        try:
            age = int(input('what is yuor age? '))
            
            if age > 100 or age < 0:    # Handle 0 division separately
                raise ValueError('age shoulde be < 100!!')
            
            div = 100 / age
            print(f'you said your age is {age}')
                        
            break # or else
        except ZeroDivisionError:
            print('please enter a number higher than 0')
        # except:
        #     print('please enter a valid number')
        # else:
        #     print('thank you')
        #     break
        finally:
            print(f'attempt {attempt}')
            attempt += 1
    
get_age()


def sum(a, b):
    try:
        return a + b
    except TypeError as err:
        print(f'something happened: {err}')

# print(sum(1, 'b'))
