# Дано 2 числа a и b.
# Используя форматирование строк, вывести на экран их сумму и произведение в форматах 'a + b = c' и 'a * b = c'

a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
sum_result = a + b
product_result = a * b
print(f'{a} + {b} = {sum_result}')
print(f'{a} * {b} = {product_result}')