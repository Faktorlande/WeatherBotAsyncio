from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class MenuCallBack(CallbackData, prefix='menu'):
    level: int | None
    menu_name: str
    city_name: str | None = None


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        'Погода сейчас': 'weather_now',
        'Расписание прогнозов': 'manage_forecast'
    }
    for text, menu_name in btns.items():
        if menu_name == 'weather_now':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level + 1, menu_name=menu_name).pack()))
        elif menu_name == 'manage_forecast':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level + 3, menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_buttons_weather_now(*, level: int, sizes: tuple[int] = (2, 1)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        'Прогноз по геолокации': 'forecast_geo',
        'Прогноз по названию города': 'forecast_city',
        'Назад': 'one_step_back'
    }
    for text, menu_name in btns.items():
        if menu_name == 'forecast_geo':
            keyboard.add(InlineKeyboardButton(text=text,
                                          callback_data=MenuCallBack(level=None, menu_name=menu_name).pack()))
        elif menu_name == 'forecast_city':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=None, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level-1, menu_name='main').pack()))



    return keyboard.adjust(*sizes).as_markup()


def get_user_menu_pass_buttons(*, level: int, sizes: tuple[int] = (1,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        'В главное меню': 'back_main_menu'
    }
    for text, menu_name in btns.items():
        keyboard.add(InlineKeyboardButton(text=text,
                                          callback_data=MenuCallBack(level=0, menu_name='main').pack()))

    return keyboard.adjust(*sizes).as_markup()
