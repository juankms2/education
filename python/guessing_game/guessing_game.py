'''A simple guessing game'''
import sys
import random


def get_game_params(args):
    params = {}
    if len(args) < 3 or len(args) > 3:
        return params

    try:
        params['num1'] = int(args[1])
        params['num2'] = int(args[2])
        
        if 0 < params['num1'] <= 100 and 0 < params['num2'] <= 100:
            if params['num1'] > params['num2']:
                higher = params['num1']
                params['num1'] = params['num2']
                params['num2'] = higher
            
            params['guess'] = random.randint(params['num1'], params['num2'])
            
        # else: Should return something else when an invalid range is provided. Maybe throw a personalized exception.
    except ValueError:
        raise ValueError('Please enter two valid numbers between 1 and 100.\n' +
            f'The provided values were: {args[1]} and {args[2]}\n')
        
    return params


# A class wrapping the params/behavior would be better. Used this way only for testing/teaching purposes.
def guess_number(user_guess, guess_params):
    '''
    Verifies the given user_guess has the required value present in guess_params['guess'].
    ''' 
    try:
        guess = int(user_guess)
        return guess == guess_params["guess"]
    except ValueError:
        raise ValueError('Mmmm, it looks like you entered an invalid number ' +
                         f'between {guess_params["num1"]} and {guess_params["num2"]}'
                         '\n\nTry again!')
    
    return False


def start_playing():
    params = {}
    args_error = ''
    continue_game = True
    
    try:
        params = get_game_params(sys.argv)
    except ValueError as e:
        args_error = e
    
    if args_error:
        print(f'Invalid arguments. \n{args_error}')
        continue_game = False
    elif len(params) == 0:
        print('Invalid arguments. \n' +
              'Please provide two numbers between 1 and 100.\n Example:\n' +
              '> guessing_game 1 24\n')
        continue_game = False
    elif len(params) == 2:
        print(
            f'''Provided numbers can not be lower than 1 or higher than 100.
            Example:
            > python guessing_number 1 24\n
            The provided values were: {params["num1"]} and {params["num2"]}\n''')
        continue_game = False
    
    while continue_game:
        try:
            user_guess = input(f'Guess the number between {params["num1"]} and {params["num2"]}:  ')
            
            if guess_number(user_guess, params):
                print(f'Cool! {user_guess} is the right number.\n')
                continue_game = False
            else:
                print(f'Nooop! {user_guess} is NOT the right number.\n\nTry again.')
        except ValueError as e:
            print(e)
    else:
        print('Game Over!\n')


if __name__ == '__main__':
    start_playing()
