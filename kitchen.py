import random
from typing import Callable


def log(template: str) -> Callable:
    """Параметрический декоратор, параметр шаблона:
    время выполнения"""
    def outer_wrapper(func: Callable) -> Callable:
        """Простой декоратор"""
        def inner_wrapper(*args, **kwargs) -> str:
            """Выводит строку, полученную после подстановки
            значений в шаблон декоратора"""
            random_time = random.randint(0, 60)
            return(template.format(random_time))
        return inner_wrapper
    return outer_wrapper


@log("🍕 Приготовили за {}с!")
def bake():
    """Готовит пиццу"""
    pass


@log("🚴 Доставили за {}с!")
def delivery():
    """Доставляет пиццу"""
    pass


@log("🏠 Забрали за {}с!")
def pickup():
    """Самовывоз"""
    pass
