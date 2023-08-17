from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("delete_birthday", "Guruhingizdagi tug'ilgan kunlarni o'chiring."),
            types.BotCommand("add_birthday", "Guruhingizga yangi tug'ilgan kunlar qo'shishing."),
            types.BotCommand("my_birthday", "Guruhingizdagi tug'ilganlar ro'yxati."),
        ]
    )
