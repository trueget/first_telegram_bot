import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
from wiki_func import wiki_funk

from data_base import write_data, write_message_from_users
from config import TOKEN


'''настроить ведение журнала'''
logging.basicConfig(level=logging.INFO)


'''инициализация бота и диспетчера'''
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


'''обработчики команд (сообщений)'''
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    write_data(message.chat["id"], message.chat["first_name"])
    write_message_from_users(message.chat["first_name"], message.chat["id"], message.text)
    await message.answer(f'Привет, {message.chat["first_name"]}!', reply_markup=nav.main_menu)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    write_message_from_users(message.chat["first_name"], message.chat["id"], message.text)
    await message.answer('здесь пока пусто')


@dp.message_handler(commands=['game'])
async def process_game_command(message: types.Message):
    write_message_from_users(message.chat["first_name"], message.chat["id"], message.text)
    await message.answer('эта игра пока пуста')


@dp.message_handler()
async def all_buttons(message: types.Message):

    write_message_from_users(message.chat["first_name"], message.chat["id"], message.text)

    if message.text == 'info about you ❗️':
        await bot.send_message(message.from_user.id, f'Ваше имя -- {message.chat["first_name"]}\nВаше прозвище -- {message.chat["username"]}\nВаш id -- {message.chat["id"]}')
    elif message.text == '-другое-':
        await bot.send_message(message.from_user.id,'Вы перешли по кнопке -другое-' , reply_markup=nav.menu_other)
    elif message.text == 'другое 1 ♐️':
        await bot.send_message(message.from_user.id, 'вы нажали на кнопку ДРУГОЕ_1, к ней пока не подключен функционал 👻✍️👅')
    elif message.text == 'другое 2 ♐️':
        await bot.send_message(message.from_user.id, 'вы нажали на кнопку ДРУГОЕ_2, к ней пока не подключен функционал 🙅‍♂️🙆🤷‍♂️')
    elif message.text == 'Главное меню 🆙':
        await bot.send_message(message.from_user.id, 'Вы вернулись в нлавное меню', reply_markup=nav.main_menu)


@dp.message_handler(commands=['wiki'])
async def process_wiki_command(message: types.Message):
    write_message_from_users(message.chat["first_name"], message.chat["id"], message.text)
    await message.answer('Отправьте мне любое слово, и я найду его значение на Wikipedia')
    
@dp.message_handler(content_types=["text"])
async def handle_text(message: types.Message):
    await message.answer(wiki_funk(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
