# Дано 2 строки. Напишите программу, которая объединит эти две строки в одну и разделит их пробелом,
# а также поменяет местами первые два символа первой строки на первые два символа второй строки и наоборот

# Ввод двух строк
string1 = input("Введите первую строку: ")
string2 = input("Введите вторую строку: ")

combined = f"{string1} {string2}"

if len(string1) >= 2 and len(string2) >= 2:
    new_string1 = string2[:2] + string1[2:]
    new_string2 = string1[:2] + string2[2:]
else:
    new_string1 = string1
    new_string2 = string2

# Вывод результатов
print("Объединенная строка:", combined)
print("Первая строка после обмена:", new_string1)
print("Вторая строка после обмена:", new_string2)