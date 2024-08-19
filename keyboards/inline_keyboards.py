from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        'Погода сейчас': 'weather_now',
        'Расписание прогнозов': 'manage_forecast'
    }
    for text, menu_name in btns.items():
        if level == 0:
            keyboard.add(InlineKeyboardButton(text=text, callback_data=menu_name))

    return keyboard.adjust(*sizes).as_markup()
