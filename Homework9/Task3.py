# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases


with open('test_file/prices.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

purchases = []
current_sum = 0

for line in lines:
    line = line.strip()
    if line == '':
        if current_sum > 0:
            purchases.append(current_sum)
            current_sum = 0
    else:
        current_sum += int(line)

if current_sum > 0:
    purchases.append(current_sum)

most_expensive = sorted(purchases, reverse=True)[:3]

three_most_expensive_purchases = sum(most_expensive)

print(three_most_expensive_purchases)

assert three_most_expensive_purchases == 202346