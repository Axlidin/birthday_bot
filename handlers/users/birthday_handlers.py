import sqlite3
from _datetime import datetime
import asyncpg
import pytz
from aiogram.types import Message, CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from keyboards.default.menu import Main_menu, AdminMain_menu
from loader import bot, db
from states.birthday_states import Birthday, del_birthday

# /form komandasi uchun handler yaratamiz. Bu yerda foydalanuvchi hech qanday holatda emas, state=None
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup
from loader import dp


@dp.message_handler(text="Add birthday", state=None)
async def enter_test(message: types.Message):
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")
    await message.answer("Ism kiriting", reply_markup=Mk)
    await Birthday.FullName.set()

@dp.message_handler(text="🛑 To'xtatish", state=Birthday)
async def cancel_see_fan(message: types.Message, state: FSMContext):
    tg_id = message.from_user.id
    if tg_id == 5419118871:
        await message.answer("Siz Tug'ilgan kun qo'shishni bekor qildingiz", reply_markup=AdminMain_menu)
    else:
        await message.answer("Siz Tug'ilgan kun qo'shishni bekor qildingiz", reply_markup=Main_menu)
    await state.reset_state()


@dp.message_handler(state=Birthday.FullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text.upper()

    await state.update_data(
        {"name": fullname}
    )
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")
    await message.answer("Tug'ilgan yil kiriting! (<b>1996</b>)", reply_markup=Mk)

    await Birthday.next()
@dp.message_handler(lambda message: not message.text.isdigit(), state=Birthday.Year)
async def process_year(message: types.Message):
    """
    If year is invalid
    """
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")
    return await message.answer("yil faqat raqamlarda kiritilishi kerak!!<b>1996</b>", reply_markup=Mk)
@dp.message_handler(state=Birthday.Year)
async def answer_year(message: types.Message, state: FSMContext):
    year = str(message.text)
    if len(year) ==  4:
        await state.update_data(
            {"year": int(year)}
        )
        Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        Mk.add("🛑 To'xtatish")
        await message.answer("Tug'ilgan oyingizni kiriting (<b>12</b>)", reply_markup=Mk)
        await Birthday.next()
    else:
        Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        Mk.add("🛑 To'xtatish")
        await message.answer("Tug'ilgan yil 4 ta raqamdan iborat bo'ladi (<b>xxxx</b>)", reply_markup=Mk)
        await Birthday.Year.set()

@dp.message_handler(lambda message: not message.text.isdigit(), state=Birthday.Month)
async def process_month(message: types.Message):
    """
    If month is invalid
    """
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")
    return await message.answer("oy faqat raqamlarda kiritilishi kerak!!<b>12</b>", reply_markup=Mk)
@dp.message_handler(lambda message: int(message.text) not in range(1, 13), state=Birthday.Month)
async def process_month_invalid(message: types.Message):
    """
    Foydalanuvchining tug'ilgan oyini oladi
    """
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")
    return await message.answer("Kechirasz, bunday oy mavjud emas", reply_markup=Mk)
@dp.message_handler(state=Birthday.Month)
async def answer_month(message: types.Message, state: FSMContext):
    month = int(message.text)
    # print(month)
    await state.update_data(
        {"month": month}
    )
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")

    await message.answer("Tug'ilgan kun kiriting (<b>13</b>)", reply_markup=Mk)

    await Birthday.next()

@dp.message_handler(lambda message: not message.text.isdigit(), state=Birthday.Day)
async def process_day(message: types.Message):
    """
    If day is invalid
    """
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")
    return await message.answer("kun faqat raqamlarda kiritilishi kerak!<b>13</b>", reply_markup=Mk)
@dp.message_handler(lambda message: int(message.text) not in range(1, 32), state=Birthday.Day)
async def process_day_invalid(message: types.Message):
    """
    Foydalanuvchining tug'ilgan kunini oladi
    """
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")
    return await message.answer("Kechirasz, bunday kun mavjud emas", reply_markup=Mk)


@dp.message_handler(state=Birthday.Day)
async def answer_month(message: types.Message, state: FSMContext):
    day = int(message.text)
    Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    Mk.add("🛑 To'xtatish")
    # print(day)

    await state.update_data(
        {"day": day}
    )
    # Ma`lumotlarni qayta o'qiymiz
    data = await state.get_data()
    name = data.get("name")
    year = data.get("year")
    month = data.get("month")
    day = data.get("day")


    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"Ism - {name}\n"
    msg += f"Tug'ilgan yil - {year}\n"
    msg += f"Tug'ilgan oy: - {month}\n"
    msg += f"Tug'ilgan kun: - {day}\n"

    # await message.answer(msg)

    # State dan chiqaramiz
    # 1-variant
    await state.finish()

    # 2-variant
    # await state.reset_state()

    # 3-variant. Ma`lumotlarni saqlab qolgan holda
    # await state.reset_state(with_data=False)
    # await bot.send_message(chat_id=ADMINS[0], text=msg)
    member_id = message.from_user.id
    await state.finish()  # malumotlar ochib ketadi

    try:
        await db.add_birthday(telegram_id=member_id,
                          full_name=data['name'],
                          Year=data['year'],
                          Month=data['month'],
                          Day=data['day'],
                                         ),

    except asyncpg.exceptions.UniqueViolationError:
        await state.reset_state(with_data=True)
    if message.from_user.id == 5419118871:
        await message.answer(f"Tabriklaymiz,siz muvaffaqiyatli tug'ilgan kun kiritdingiz", reply_markup=AdminMain_menu)
    else:
        await message.answer(f"Tabriklaymiz,siz muvaffaqiyatli tug'ilgan kun kiritdingiz", reply_markup=Main_menu)

@dp.callback_query_handler(text="cancel_admin")
async def cancelmenu(call: CallbackQuery):
    await call.message.answer("<b>Asosiy bo'lim!</b>", reply_markup=Main_menu)
    await call.message.delete()
    await call.answer(cache_time=30)

@dp.callback_query_handler(text="cancel")
async def cancelmenu(call: CallbackQuery):
    await call.message.answer("<b>Asosiy bo'lim!</b>", reply_markup=Main_menu)
    await call.message.delete()
    await call.answer(cache_time=30)

 ###delete
#tug'ilgan kun o'chirish
@dp.message_handler(text="Delete birthday")
async def delete_db_fan(message: types.Message):
    tg_id = message.from_user.id
    my_birthday = await db.my_birthday(tg_id=tg_id)
    if my_birthday:
            Mk = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            for menu in my_birthday:
                fan_name_menu = menu[1]
                Mk.insert(KeyboardButton(text=fan_name_menu, resize_keyboard=True))
            Mk.add("🛑 To'xtatish")
            await message.answer(f"Kerakli Odamni tanlang! yoki tugmani bosing", reply_markup=Mk)
            await del_birthday.next()
    else:
        if message.from_user.id == 5419118871:
            await message.answer("❌ Sizda Tug'ilgan kunlar hozirda mavjud emas.\n"
                                 "Tug'ilgan kun qo'shish uchun <i>Add birthday</i> tugmasini bosing",
                                 reply_markup=AdminMain_menu)
        else:

            await message.answer("❌ Sizda Tug'ilgan kunlar hozirda mavjud emas.\n"
                                 "Tug'ilgan kun qo'shish uchun <i>Add birthday</i> tugmasini bosing",
                                 reply_markup=Main_menu)

@dp.message_handler(commands=["🛑 To'xtatish"], state=del_birthday)
async def cancel_delete(message: types.Message, state: FSMContext):
    if message.from_user.id == 5419118871:
        await message.answer("Siz Tug'ilgan o'chirishni bekor qildingiz", reply_markup=AdminMain_menu)
    else:
        await message.answer("Siz Tug'ilgan o'chirishni bekor qildingiz", reply_markup=Main_menu)
    await state.reset_state()

@dp.message_handler(state=del_birthday.birhtday_del)
async def data_del(message: types.Message, state: FSMContext):
    del_birthday = message.text.upper()
    # print(del_birthday)
    await state.update_data(
        {"del_birthday": del_birthday}
    )
    deletes = await db.delete_db_name(del_name=del_birthday)
    if deletes:
        if message.from_user.id == 5419118871:
            await message.answer(f"Siz tug'ilgan kun o'chirding\n\nDelete: {del_birthday}", reply_markup=AdminMain_menu)
            await state.reset_state(with_data=True)
        else:
            await message.answer(f"Siz tug'ilgan kun o'chirding\n\nDelete: {del_birthday}", reply_markup=Main_menu)
            await state.reset_state(with_data=True)
    else:
        if message.from_user.id == 5419118871:
            await message.answer("Hozirda bunday ismli odam yo'q.", reply_markup=AdminMain_menu)
        else:
            await message.answer("Hozirda bunday ismli odam yo'q.", reply_markup=Main_menu)

import datetime

@dp.message_handler(text="📊 Statistika")
async def show_Statistika(message: types.Message):
    tg_id = message.from_user.id
    timezone = pytz.timezone("Asia/Tashkent")

    today = datetime.datetime.now(timezone)
    year = today.year
    month = today.month
    day = today.day
    hour = today.hour
    minut = today.minute
    user_count = await db.count_FIO_state()
    birthday_count = await db.count_birthday()
    gr_date_count = await db.count_Gr_birthyday()
    gr_count = await db.count_Guruhlar()
    msg = f"<b><i>@happyMybirthday_bot</i></b>\n📆 {year}-{month}-{day} ⏰ {hour}:{minut}\n👥 Bot foydalanuvchilari: " \
          f"<b>{user_count}</b> ta\n" \
          f"🎁🎉 Tug'ilgan kunlar: <b>{birthday_count}</b> ta\n" \
          f"👥 Bot guruhlarda: <b>{gr_count}</b> ta\n" \
          f"🎁🎉 Tug'ilgan kunlar - guruhlarda: <b>{gr_date_count}</b> ta\n"
    if tg_id == 5419118871:
        await bot.send_message(chat_id=message.from_user.id, text=msg, reply_markup=AdminMain_menu)
    else:
        await bot.send_message(chat_id=message.from_user.id, text=msg, reply_markup=Main_menu)

