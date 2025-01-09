# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest
from contextlib import nullcontext

def all_division(*arg1):

    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division

# Вариант описаный в доке pytest
@pytest.mark.parametrize('prep_data', [
    pytest.param((2, 1, nullcontext(2)), marks=pytest.mark.smoke),
    (1, 2, nullcontext(0.5)),
    pytest.param((1, -1, nullcontext(-1)), marks=pytest.mark.skip('Не выполняем')),
    (1, 0, pytest.raises(ZeroDivisionError)),
    ('a', 1, pytest.raises(TypeError))
])
def test_suit(prep_data):
    a, b, result = prep_data
    with result as res:
        assert all_division(a, b) == res



# @pytest.mark.parametrize('prep_data', [
#     pytest.param((2, 1, 2), marks=pytest.mark.smoke),
#     (1, 2, 0.5),
#     pytest.param((1, -1, -1), marks=pytest.mark.skip('Не выполняем'))
#     ])
# def test_division(prep_data):
#     a, b, result = prep_data
#     assert all_division(a, b) == result
#
# @pytest.mark.parametrize('a, b, result', [
#     (1, 0, pytest.raises(ZeroDivisionError)),
#     ('a', 1, pytest.raises(TypeError))
#     ])
# def test_divex(a, b, result):
#     with pytest.raises(Exception):
#         assert all_division(a, b) == result