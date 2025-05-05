# Программа получает на вход натуральное число num.
# Программа должна вывести другое натуральное число, удовлетворяющее условиям:
# Новое число должно отличаться от данного ровно одной цифрой
# Новое число должно столько же знаков как исходное
# Новое число должно делиться на 3
# Новое число должно быть максимально возможным из всех таких чисел
# Например (Ввод --> Вывод) :
#
# 379 --> 879
# 15 --> 75
# 4974 --> 7974

def max_division_by_3(num):
    num_str = str(num)
    max_num_str = None

    for i in range(len(num_str)):
        original_digit = num_str[i]
        for new_digit in map(str, range(9, -1, -1)):
            if new_digit == original_digit:
                continue
            candidate_list = list(num_str)
            candidate_list[i] = new_digit
            candidate_str = ''.join(candidate_list)

            if len(candidate_str) > 1 and candidate_str[0] == '0':
                continue

            candidate_num = int(candidate_str)
            if candidate_num % 3 == 0:
                if max_num_str is None or candidate_num > int(max_num_str):
                    max_num_str = candidate_str

    if max_num_str is not None:
        return int(max_num_str)
    return 0


data = [
    379, 810, 981, 4974, 996, 9000, 15, 0, 9881, 9984, 9876543210, 98795432109879543210
]

test_data = [
    879, 870, 987, 7974, 999, 9900, 75, 9, 9981, 9987, 9879543210, 98798432109879543210
]


for i, d in enumerate(data):
    assert max_division_by_3(d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')