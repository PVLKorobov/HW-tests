from task1 import main
from task2 import main as YDmain


def test_task_1():
    res = main.run_task_1()
    expected = [
    {'visit1': ['Москва', 'Россия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
    ]
    assert res == expected

def test_task_2():
    res = main.run_task_2()
    expected = [213, 15, 54, 119, 98, 35]
    assert res == expected

def test_task_3():
    res = main.run_task_3()
    expected = 'yandex'
    assert res == expected

def test_yandex_api():
    res = YDmain.run_YD_API()
    expected = 201 # В Yandex REST API вместо кода 200 в случае успеха возвращается код 201
    assert res == expected