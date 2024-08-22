from aiogram import Router, types, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keyboards.inline_keyboards import MenuCallBack

from handlers.menu_processing import get_menu_content
from utils.work_with_API import get_forecast

user_router = Router()


class GetForecastCityName(StatesGroup):
    city_name = State()


@user_router.message(CommandStart())
async def cmd_start(message: Message):
    media, reply_markup = await get_menu_content(level=0, menu_name='main')
    await message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)


@user_router.message(GetForecastCityName.city_name)
async def get_forecast_city(message: Message, state: FSMContext):
    await state.clear()
    data_forecast = get_forecast(message.text)
    forecast_str = ''
    for data in data_forecast:
        forecast_str += f"{data}: {data_forecast[data]}\n"
    await message.answer(f"Город: {message.text}"+'\n'+forecast_str)


@user_router.callback_query(MenuCallBack.filter(F.menu_name == 'forecast_city'))
async def user_forecast_city(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(f"Введите название города")
    await callback.answer()
    await state.set_state(GetForecastCityName.city_name)


@user_router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack):
    media, reply_markup = await get_menu_content(
        level=callback_data.level,  # level задается из inline_keyboards в get_user_main_btns с помощью callback_data
        menu_name=callback_data.menu_name,  # menu_name (имя кнопки) задается из inline_keyboards
        # в get_user_main_btns с помощью callback_data
    )
    await callback.message.edit_media(media=media, reply_markup=reply_markup)
