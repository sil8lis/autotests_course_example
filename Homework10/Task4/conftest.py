import pytest
import time


@pytest.fixture(scope="class")
def class_time_logger(request):
    print(f"\n[START] Тестовый класс: {request.cls.__name__} - запуск")
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"[END] Тестовый класс: {request.cls.__name__} - завершение. Время: {end_time - start_time:.2f} секунд")


@pytest.fixture
def test_time_logger():
    start_time = time.time()
    yield
    end_time = time.time()
    print(f"\n[INFO] Время выполнения теста: {end_time - start_time:.2f} секунд")