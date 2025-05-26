# Напишите 5 тестов на функцию all_division. Обязательно должен быть тест деления на ноль.
# Промаркируйте часть тестов. Например, smoke.
# В консоли с помощью pytest сделайте вызов:
# 1) Всех тестов
# 2) Только с маркером smoke
# 3) По маске. Выберите такую маску, чтобы под неё подпадали не все тесты, но больше одного
# Пришлите на проверку файл с тестами и скрины с вызовами и их результаты

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

# 1. Тест деления без ошибок
@pytest.mark.smoke
def test_division_normal():
    assert all_division(100, 2, 5) == 10

# 2. Тест деления на 1
def test_division_by_one():
    assert all_division(42, 1, 1) == 42

# 3. Тест деления с отрицательными числами
@pytest.mark.smoke
def test_division_with_negatives():
    assert all_division(100, -2, 5) == -10

# 4. Тест деления на ноль
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        all_division(10, 0)

# 5. Тест деления с одним аргументом
def test_single_argument():
    assert all_division(7) == 7

#pytest Task2.py Запуск всех тестов
#pytest -m smoke Task2.py Запуск только тестов с маркером smoke
#pytest -k "test_division" Task2.py Запуск тестов по маске (например, все тесты, содержащие test_division)