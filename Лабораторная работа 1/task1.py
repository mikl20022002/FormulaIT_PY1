numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)

numbers_temp = numbers[:none_index] + numbers[none_index + 1:]

numbers[none_index] = sum(numbers_temp) / (len(numbers_temp) + 1)

print("Измененный список:", numbers)