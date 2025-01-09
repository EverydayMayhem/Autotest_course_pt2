# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):
    global division
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division
@pytest.mark.usefixtures('time_for_class')
class TestDivision:

    def test_zerodiv(self, time_for_test):
        with pytest.raises(ZeroDivisionError):
            all_division(1, 0)

    def test_positive(self,):
        assert all_division(2, 1) == 2

    def test_floating(self,):
        assert all_division(1, 2) == 0.5

    def test_negative(self, time_for_test):
        assert all_division(1, -1) == -1

    def test_divletter(self, time_for_test):
        with pytest.raises(TypeError):
            all_division('a', 1)