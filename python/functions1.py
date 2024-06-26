# Examples of functional programming. Existing functions and  usage of lambdas.

from functools import reduce

my_list = [1,2,3,4,5]

def multiply_by(item):
    return item * 3

def is_odd(item):
    return item % 2 != 0

def add_item(accumulator, item):
    return accumulator + item

# print(list(map(multiply_by, my_list)))
print(list(map(lambda item: item * 3, my_list)))

# print(list(filter(is_odd, my_list)))
print(list(filter(lambda item: item % 2 != 0, my_list)))

# print(reduce(add_item, my_list, 0))
print(reduce(lambda accumulator, item: accumulator + item, my_list, 0))


#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(str.upper, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
# my_numbers.sort()
# my_numbers[::-1] # actually reverts, does not sort
print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_over50(score):
    return score > 50

# print(list(filter(is_over50, scores)))
print(list(filter(lambda score: score > 50, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
# print(reduce(add_item, my_numbers, reduce(add_item, scores, 0)))
# print(reduce(add_item, (my_numbers + scores)))
print(reduce(lambda accumulator, item: accumulator + item, (my_numbers + scores)))
