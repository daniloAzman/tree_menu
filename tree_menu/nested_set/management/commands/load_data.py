import random
from string import ascii_letters, digits

from nested_set.models import Menu, MenuItem
from django.core.management import BaseCommand
from django.db import IntegrityError

from .utils import info

ALPHABET = ascii_letters + digits


class Command(BaseCommand):
    _class = Menu
    name = 'MENU'
    menu_size: int = 4
    menu_depth: int = 4

    def __create_menu_items(
        self,
        level_name: str,
        menu: Menu,
        parent: MenuItem = None,
        depth: int = 0,
    ) -> None:
        if depth >= self.menu_depth:
            return
        for i in range(self.menu_size):
            unique_id = ''.join(random.choice(ALPHABET) for i in range(4))
            menu_item_title = (
                f'{level_name}: level-{depth+1} item-{i+1}')
            menu_item = MenuItem.objects.create(
                title=menu_item_title,
                menu=menu,
                parent=parent,
            )
            self.__create_menu_items(level_name, menu, menu_item, depth + 1)

    def __create_menu(self, menu_title: str) -> None:
        menu = Menu.objects.create(title=menu_title)
        self.__create_menu_items(level_name=menu.title, menu=menu)

    @info
    def handle(self, *args, **kwargs):
        for menu_title in (
            'main_menu',
        ):
            self.__create_menu(menu_title)
