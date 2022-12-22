from unittest.mock import patch
from click.testing import CliRunner
import random
from kitchen import bake, delivery, pickup
from pizza_class import Margharita, Pepperoni, Hawaiian
from click_pizza import order, menu


def test_bake():
    """тест верного результата функции bake()"""
    with patch.object(random, "randint", return_value=1):
        assert bake() == "🍕 Приготовили за 1с!"


def test_delivery():
    """тест верного результата функции delivery()"""
    with patch.object(random, "randint", return_value=2):
        assert delivery() == "🚴 Доставили за 2с!"


def test_pickup():
    """тест верного результата функции pickup()"""
    with patch.object(random, "randint", return_value=3):
        assert pickup() == "🏠 Забрали за 3с!"


def test_eq_size_without_reciept():
    """тест проверяющий, что ингридиенты для пицц не меняются в
    зависимости от их размера"""
    assert Pepperoni("L").__str__(0) == Pepperoni("XL").__str__(0)
    assert Margharita("L").__str__(0) == Margharita("XL").__str__(0)
    assert Hawaiian("L").__str__(0) == Hawaiian("XL").__str__(0)


def test_eq_size_with_reciept():
    """тест проверяющий, что состав пиццы и ингридиенты в граммах меняются в
    зависимости от размера пиццы"""
    assert Pepperoni("L").__str__(1) != Pepperoni("XL").__str__(1)
    assert Margharita("L").__str__(1) != Margharita("XL").__str__(1)
    assert Hawaiian("L").__str__(1) != Hawaiian("XL").__str__(1)


def test_2pizzas_equal():
    expected = False
    assert Pepperoni("L").__eq__(Margharita("L")) == expected


def test_order_with_delivery():
    """тест проверяет верность вывода функции order() с опцией --delivery
    и вводом названия пиццы разным регистром"""
    run = CliRunner()
    with patch.object(random, "randint", return_value=1):
        result = run.invoke(order, ["PePpeRoni", "--delivery"])
        actual = result.output
        expected = ("🍕 Приготовили за 1с!\n"
                    "🚴 Доставили за 1с!\n")
        assert actual == expected


def test_order_without_delivery():
    """тест проверяет верность вывода функции order() без опции --delivery
    и вводом названия пиццы разным регистром"""
    run = CliRunner()
    with patch.object(random, "randint", return_value=2):
        result = run.invoke(order, ["HawaiiaN"])
        actual = result.output
        expected = ("🍕 Приготовили за 2с!\n"
                    "🏠 Забрали за 2с!\n")
        assert actual == expected


def test_order_wrong_pizza():
    """тест проверяет, что выдается ошибка, если
    ввели неверное название пиццы"""
    run = CliRunner()
    with patch.object(random, "randint", return_value=2):
        result = run.invoke(order, ["4Cheese"])
        actual = result.output
        expected = ("Мы такую пиццу не готовим 😔\n")
        assert actual == expected


def test_menu_without_reciept():
    """Тест проверяет содержит ли меню без опции рецептов
    строку (L или XL), так как без рецепта размер пиццы
    не имеет значения для вывода"""
    run = CliRunner()
    result = run.invoke(menu)
    actual = result.output
    assert ("Pepperoni (L или XL)" in actual and
            "Margharita (L или XL)" in actual and
            "Hawaiian (L или XL)" in actual)


def test_menu_with_reciept():
    """Тест, проверяющий, что при опции рецептов и без указания размеров
    пиццы, по умолчанию, выдается состав в граммах для пиццы в размере L """
    run = CliRunner()
    result = run.invoke(menu, ["--reciept"])
    actual = result.output
    assert ("Pepperoni(L)" in actual
            and "г." in actual)


def test_menu_with_reciept_size():
    """Тест, проверяющий, что при опции рецептов и c указанием размера
    пиццы XL, по умолчанию, выдается состав в граммах для пиццы в размере XL"""
    run = CliRunner()
    result = run.invoke(menu, ["--reciept", "--size", "XL"])
    actual = result.output
    assert ("Pepperoni(XL)" in actual
            and "г." in actual)


def test_menu_with_reciept_sizeS():
    """Тест, проверяющий, что при опции рецептов и c указанием неверных
    размеров пиццы, выдается сообщение с ошибкой"""
    run = CliRunner()
    result = run.invoke(menu, ["--reciept", "--size", "S"])
    actual = result.output
    expected = "Мы не готовим пиццу в этом размере. Выберите размер L или XL\n"
    assert actual == expected
