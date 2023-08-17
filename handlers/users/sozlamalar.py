from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.menu import AdminMain_menu, Main_menu
from loader import dp, db
@dp.message_handler(text="🛠 Sozlamalar")
async def bot_start_new_ism(message: types.Message, state: FSMContext):
    await message.answer("yangi ismingizni kriting")
    await state.set_state("new_ism")

@dp.message_handler(state="new_ism")
async def enter_new_ism(message: types.Message, state: FSMContext):
    new_name = message.text.capitalize()
    await db.update_user_FIO_state_username(fullname=new_name, telegram_id=message.from_user.id)
    if message.from_user.id == 5419118871:
        await message.answer(f"Ismingiz yangilandi: {new_name}", reply_markup=AdminMain_menu)
    else:
        await message.answer(f"Ismingiz yangilandi: {new_name}", reply_markup=Main_menu)
    await state.finish()