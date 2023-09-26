# To identify the maximum number in the list

numbers = [20,32,10,9,4,76,39]
max = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i];
print(f'The Max number in the list is {max}')