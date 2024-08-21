from keyboards.inline_keyboards import (get_user_main_btns,
                                        get_user_menu_pass_buttons,
                                        get_user_buttons_weather_now,
                                        )

from aiogram.types import InputMediaPhoto

from common.data_for_menu import banners, text_for_dummy


async def main_menu(level: int, menu_name: str):
    banner = banners[menu_name]
    image = InputMediaPhoto(media=banner, caption='Главное меню')
    keyboards = get_user_main_btns(level=level)
    return image, keyboards


async def menu_pass(level: int, menu_name: str):
    banner = banners['main']
    image = InputMediaPhoto(media=banner, caption=text_for_dummy)
    keyboards = get_user_menu_pass_buttons(level=level)
    return image, keyboards


async def menu_for_weather_now(level: int, menu_name: str):
    banner = banners[menu_name]
    image = InputMediaPhoto(media=banner, caption='Выберите опцию')
    keyboards = get_user_buttons_weather_now(level=level)
    return image, keyboards


async def get_forecast_city():
    return f"Введите название города"


# Отдельная функция для опеределния какое меню выводить
# Вызывается в user_roter при команде /start. При команде старт уже заданы level=0 menu='main'#
async def get_menu_content(
        level: int,
        menu_name: str
):
    if level == 0:
        return await main_menu(level, menu_name)
    elif level == 1:
        return await menu_for_weather_now(level, menu_name)
    elif level == 3:
        return await menu_pass(level, menu_name)
    else:
        if menu_name == 'forecast_geo':
            return await menu_pass(level, menu_name)
        elif menu_name == 'forecast_city':
            return await get_forecast_city()
