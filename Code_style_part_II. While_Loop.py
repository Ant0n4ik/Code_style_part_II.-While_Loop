my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers = []
for i in range(len(my_list)):
    if my_list[i] < 0:
        break
    if my_list[i] > 0:
        positive_numbers.append(my_list[i])

print('Положительные числа: ', positive_numbers)