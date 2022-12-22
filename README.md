# Exam_Pizza
Вывод меню пиццы:
>python click_pizza.py menu 

Вывод пиццы с ингридиентами в граммах:
>python click_pizza.py menu --reciept

Вывод большой пиццы (XL) с ингридиентами в граммах:
>python click_pizza.py menu --reciept --size XL

Вывод статуса заказа пиццы c доставкой:
>python click_pizza.py order pepperoni --delivery

Отчет о тестировании находится в файле test_results

Тестирование:
Запуск теста:
>python -m pytest -v tests.py 

Запуск test coverage:
>python -m pytest -q tests.py --cov

Сохранить отчет о покрытии в виде html файла:
>python -m pytest tests.py --cov . --cov-report html
