# Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)


n = int(input('Введите количество чисел в массиве: '))
list_1 = []

for i in range(n):
    a = int(input(f'Введите {i+1} число: '))
    list_1.append(a)
    n -= 1

range_1 = int(input('Введите минимальное число диапозона: '))
range_2 = int(input('Введите ммаксимальное число диапозона: '))

res = []

for i in range(0,len(list_1)):
    if list_1[i] >= range_1 and list_1[i] <= range_2:
        res.append(i)\
        
print(res)



