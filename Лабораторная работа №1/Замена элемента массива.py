numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

summa = 0
index = 0

for i in range(len(numbers)):
    if numbers[i] != None:
        summa += numbers[i]
    else:
        index = i

SA = summa/len(numbers)

numbers[index] = SA

print("Измененный список:", numbers)
