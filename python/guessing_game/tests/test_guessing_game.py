# import sys
# sys.path.append('../guessing_game')

import unittest
import guessing_game


class TestGuessingGame(unittest.TestCase):
    def test_get_game_params_with_invalid_args(self):
        params = guessing_game.get_game_params([])
        
        self.assertEqual(params, {})


    def test_get_game_params_with_invalid_numbers(self):
        args = ['script_name', 1, '123d']
        
        with self.assertRaises(ValueError) as err:
            params = guessing_game.get_game_params(args)
            
        self.assertTrue('Please enter two valid numbers between 1 and 100' in str(err.exception))


    def test_get_game_params_with_invalid_range(self):
        args = ['script_name', 0, 200]
        params = guessing_game.get_game_params(args)
        
        self.assertEqual(params, {'num1': 0, 'num2': 200})


    def test_guess_number_success(self):
        guess_params = {'num1': 1, 'num2': 10, 'guess': 3}
        result = guessing_game.guess_number(3, guess_params)
        
        self.assertTrue(result)


    def test_guess_number_fail(self):
        guess_params = {'num1': 1, 'num2': 10, 'guess': 3}
        result = guessing_game.guess_number(5, guess_params)
        
        self.assertFalse(result)


    def test_guess_number_invalid_number(self):
        guess_params = {'num1': 1, 'num2': 10, 'guess': 3}
        
        with self.assertRaises(ValueError) as err:
            guessing_game.guess_number('rd', guess_params)
            
        self.assertTrue('it looks like you entered an invalid number' in str(err.exception))


if __name__ == '__main__':
    unittest.main()
