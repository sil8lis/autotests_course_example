# Напишите функцию which_triangle(a, b, c),
# На вход поступают длины трёх сторон треугольника: a, b, c
# Программа выводит какой это треугольник type_triangle: "Равносторонний", "Равнобедренный", "Обычный".
# Либо "Не треугольник", если по переданным параметрам невозможно построить треугольник
# Например 1, 1, 1 --> "Равносторонний"

def which_triangle(a, b, c):
    type_triangle = None
    if a == b == c:
        type_triangle = 'Равносторонний'
    elif a != b != c != a and (a not in (1,0) and b not in (1,0) and c not in (1,0)):
        type_triangle ='Обычный'
    elif a != b != c != a and (a in (1,0) or b in (1,0) or c in (1,0)):
        type_triangle ='Не треугольник'
    else:
        type_triangle ='Равнобедренный'
    return type_triangle

data = [
    (3, 3, 3),
    (1, 2, 2),
    (3, 4, 5),
    (3, 2, 3),
    (1, 2, 3),
    (3, 2, 0)
]

test_data = [
    "Равносторонний", "Равнобедренный", "Обычный", "Равнобедренный", "Не треугольник", "Не треугольник"
]


for i, d in enumerate(data):
    assert which_triangle(*d) == test_data[i], f'С набором {d} есть ошибка, не проходит проверку'
    print(f'Тестовый набор {d} прошёл проверку')
print('Всё ок')