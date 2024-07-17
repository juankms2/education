# Examples of functional programming. Existing functions and  usage of lambdas. Continuation.

# print the square of each element in the list
my_list = [5, 4, 3]

print(list(map(lambda item: item * item, my_list)))


# sort the list asc, by the second element of each tuple
a = [(0, 2), (10, -1), (4, 3), (9, 9)]

print(a)
a.sort(key=lambda tup: tup[1])

print(a)
