# Usage of Decorators
from time import time

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('**********')
        func(*args, **kwargs)
        print('**********')
    return wrapper


def log_execution_time(func):
    def wrapper(*args, **kwargs):
        t1 = time() * 1000
        func(*args, **kwargs)
        t2 = time() * 1000
        
        print(f'execution took {t2 - t1} ms.')
    return wrapper

@my_decorator
def greet(greeting, name='Person'):
    print(f'{greeting} {name}')
    
    
@my_decorator
@log_execution_time
def say_goodbye():
    print('Good bye, you...')

@log_execution_time
def run_heavy_task():
    print('runnig a heavy task')
    for num in  range(100000000):
        num * 5
    
greet('Hello')
greet('Hello', 'Billie')
say_goodbye()

run_heavy_task()


# Exercise: 
# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
  'name': 'Sorna',
  'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # Code added
  def wrapper(*args, **kwargs):
    if args[0]['valid']:
      fn(*args, **kwargs)
    else:
      print('user is invalid')

  return wrapper
    

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
