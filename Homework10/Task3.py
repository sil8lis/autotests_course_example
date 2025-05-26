# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest

def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

@pytest.mark.parametrize(
    "args, expected",
    [
        pytest.param((100, 2, 5), 10, marks=pytest.mark.smoke),  # Тест с маркером smoke
        pytest.param((50, 5), 10),  # Обычный тест
        pytest.param((81, 3, 3), 9, marks=pytest.mark.skip(reason="Пропущен тест")),  # Тест пропущен
    ]
)
def test_all_division_parametrize(request, args, expected):
    skip_marker = request.node.get_closest_marker("skip")
    if skip_marker:
        pytest.skip(skip_marker.kwargs.get("reason", ""))
    smoke_marker = request.node.get_closest_marker("smoke")
    if smoke_marker:
        pass
    result = all_division(*args)
    assert result == expected

