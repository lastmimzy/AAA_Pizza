class Pizza:
    """Базовый класс для всех пицц"""
    base_ingredients = {"mozzarella": 100, "tomato sause": 150}

    def __init__(self, size, ingredients):
        self.__dict__.update(**self.base_ingredients, **ingredients)
        self.size = size
        if size == "XL":
            for key in self.dict():
                self.__dict__[key] = 2 * self.__dict__[key]

    def dict(self) -> dict:
        """Функция, возвращающая рецепт пиццы в виде словаря,
        исключив размер пиццы из него"""
        dict_without_size = self.__dict__.copy()
        del dict_without_size["size"]
        return dict_without_size

    def __eq__(self, other) -> bool:
        """Функция, сравнивающая пиццы"""
        return self.dict() == other.dict()

    def __str__(self, reciept: bool) -> str:
        """Вывод в заданном формате"""
        ingred_in_gr = ["{}: {}г.".format(key, value)
                        for key, value in self.dict().items()]
        class_name = self.__class__.__name__
        if reciept:
            return f'{class_name}({self.size}): {", ".join(ingred_in_gr)}'
        else:
            return f'{class_name} (L или XL): {", ".join(self.dict().keys())}'


class Margharita(Pizza):
    """Класс для пиццы Маргарита"""
    ingredients = {"tomatoes": 140, "basil": 20}

    def __init__(self, size):
        super().__init__(size, self.ingredients)


class Pepperoni(Pizza):
    """Класс для пиццы Пепперони"""
    ingredients = {"pepperoni": 90, "garlic": 10}

    def __init__(self, size):
        super().__init__(size, self.ingredients)


class Hawaiian(Pizza):
    """Класс для гавайской пиццы"""
    ingredients = {"chicken": 220, "pineapples": 170}

    def __init__(self, size):
        super().__init__(size, self.ingredients)
