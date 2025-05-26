# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest
import time

@pytest.mark.usefixtures("class_time_logger")
class TestSample:

    def test_one(self, test_time_logger):
        # Имитация работы теста
        time.sleep(0.5)
        assert True

    def test_two(self, test_time_logger):
        # Имитация работы теста
        time.sleep(0.3)
        assert 1 + 1 == 2

    def test_skip(self, test_time_logger):
        # Тест, который пропускается
        pytest.skip("Пропущен специально")