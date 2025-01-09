import pytest
import datetime

@pytest.fixture(scope='class')
def time_for_class():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'Начало класса тестов: {start},\nОкончание: {end}')


@pytest.fixture()
def time_for_test():
    start = datetime.datetime.now()
    yield
    end = datetime.datetime.now()
    print(f'Время выполнения теста: {end-start}')


def pytest_collection_modifyitems(items):
    for item in items:
        # Ищем маркер 'id_check' у каждого теста
        marker = item.get_closest_marker("id_check")
        if marker:
            # Если маркер найден, выводим его аргументы
            print(f"Arguments for @pytest.mark.id_check: {marker.args}")
