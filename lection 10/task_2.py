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

@pytest.mark.smoke
def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        all_division(1,0)

@pytest.mark.smoke
def test_positive():
    assert all_division(2,1) == 2


def test_floating():
    assert all_division(1,2) == 0.5


def test_negative():
    assert all_division(1,-1) == -1


def test_divletter():
    with pytest.raises(TypeError):
        all_division('a', 1)


# 1. Запуск всех тестов через терминал: pytest "C:\Users\Professional\PycharmProjects\pythonProject\autotests_homework\lection 10\task_2.py"
# 2. Запуск тестов из консоли, промаркированных как smoke: pytest "C:\Users\Professional\PycharmProjects\pythonProject\autotests_homework\lection 10\task_2.py" -m smoke
# 3. Запуск тестов из консоли по маске (div): pytest "C:\Users\Professional\PycharmProjects\pythonProject\autotests_homework\lection 10\task_2.py" -k div