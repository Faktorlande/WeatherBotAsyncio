from keyboards.inline_keyboards import get_user_main_btns
from aiogram.types import InputMediaPhoto

from common.data_for_menu import banners

async def main_menu(level: int, menu_name: str):
    if menu_name == 'main':
        media = banners['main']
        keyboards = get_user_main_btns(level=level)
        return media, keyboards


async def get_menu_content(
        level: int,
        menu_name: str,
):
    if level == 0:
        return await main_menu(level, menu_name)
