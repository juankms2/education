my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
item_sum = 0
for item in my_list:
    item_sum += item

print(
    f"Sample 1: Print the sum of all the elements in the list. \n * Input: {my_list}"
)
print(" * Output: Sum of items =", item_sum, "\n\n")

print(f"Sample 2: Print the index of 8. \n * Input: {my_list}")
for index, item in enumerate(my_list):
    if item == 8:
        print(f" * Output: The index of {item} is {index}\n")

picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0]]

print(
    f"Sample 3: Print the image represented by the multidimentional list. \n \
* Input: {picture}\n * Output: ")
for image in picture:
    for pixel in image:
        if pixel == 0:
            print(' ', end='')
        else:
            print('*', end='')
    print()

    # line_pic = ''
    # for pixel in image:
    #     if pixel == 0:
    #         line_pic += ' '
    #     else:
    #         line_pic += '*'
    # print(line_pic)

my_list = ["a", "b", "c", "b", "d", "m", "n", "n"]
values = []
duplicates = []

print(f"\nSample 4: Print the duplicates in the list. \n * Input: {my_list}")
for item in my_list:
    if item in values:
        duplicates.append(item)
        # print(f" * Output: {item} is a duplicate")
    values.append(item)

print(f" * Output: The duplicate elemetes are {duplicates}\n")

print(
    f"\nSample 5: New features - walrus operator (:=) in Python 3.8. \n * Input: {my_list}"
)
while (n := len(my_list)) > 1:
    my_list = my_list[:-1]  # sublist, from 0 to n(last) - 1

print(f" * Output: The reduced list has {n} elements {my_list}")
