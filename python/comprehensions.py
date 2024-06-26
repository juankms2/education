# Something new: usage of comprehensions.
# May avoid these if readability gets affected.

# The traditional way
my_list = []
my_set = {}
my_dict = {}

for char in 'this is an iterable':
    my_list.append(char)
    
print(my_list)


# The same using Comprehensions
my_list = [char for char in 'this is an iterable']
my_set = {char for char in 'this is an iterable'}   # set keeps unique elements
my_dict = {key:value for key, value in enumerate('this is an iterable')}    # enumerate returns a pair, (index, value)

print(my_list)
print(my_set)
print(my_dict)


# Other examples (operations and conditions over variable)
my_list = [char.upper() for char in 'this is an iterable']
print(my_list)

my_list = [char.upper() for char in 'this is an iterable' if char != ' ']
print(my_list)


# Exercise: rewrite the below code to use comprehensions
my_list = ["a", "b", "c", "b", "d", "m", "n", "n"]

# duplicates = []
# print(f"\nExercise: Print the duplicates in the list. \n * Input: {my_list}")
# for item in my_list:
#     if my_list.count(item) > 1 and item not in duplicates:
#         duplicates.append(item)

duplicates = set([item for item in my_list if my_list.count(item) > 1])

print(f" * Output: The duplicate elements are {duplicates}\n")

