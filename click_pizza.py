import click
from pizza_class import Margharita, Pepperoni, Hawaiian
import kitchen as k


@click.group()
def cli():
    pass


@cli.command()
@click.argument('pizza', nargs=1)
@click.option('--delivery', default=False, is_flag=True)
def order(pizza: str, delivery: bool):
    """Готовит и доставляет пиццу"""
    if pizza.lower() not in ['pepperoni', 'margharita', 'hawaiian']:
        print("Мы такую пиццу не готовим 😔")
    else:
        print(k.bake())
        if delivery:
            print(k.delivery())
        else:
            print(k.pickup())


@cli.command()
@click.option('--reciept', default=False, is_flag=True)
@click.option('--size', default='L')
def menu(reciept: bool, size: str) -> None:
    """Вывод меню"""
    size = size.upper()
    if size not in ['L', 'XL']:
        print("Мы не готовим пиццу в этом размере. Выберите размер L или XL")
    else:
        print("\033[1m{}{}{}".format("*"*23, "🍕 Наше меню 🍕", "*"*23))
        print("🧀", "\033[0m{}".format(Margharita(size).__str__(reciept)))
        print("🍕", Pepperoni(size).__str__(reciept))
        print("🍍", Hawaiian(size).__str__(reciept))


if __name__ == "__main__":
    cli()
