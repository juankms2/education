# Write unit tests using the unittest module
import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print(f'Setting up test {self._testMethodName}\n')

    def test_sum_number_success(self):
        num = 10
        result = main.sum_number(num)
        expected_result = num + 5

        self.assertEqual(result, expected_result)

    def test_sum_number_fail(self):
        num = '123d'
        # result = main.sum_number(num)
        # self.assertIsInstance(result, ValueError)

        with self.assertRaises(ValueError):
            main.sum_number(num)

    def tearDown(self):
        print(f'Test {self._testMethodName}, completed\n')

if __name__ == '__main__':
    unittest.main()
