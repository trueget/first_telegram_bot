from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


'''кнопка возврата на главное меню'''
btn_return = KeyboardButton('Главное меню 🆙')


'''главное меню'''
btn_info_about_me = KeyboardButton('info about you ❗️')
btn_other_main = KeyboardButton('-другое-')
main_menu = ReplyKeyboardMarkup(resize_keyboard=True ).add(btn_info_about_me, btn_other_main)


'''переход в подменю -ДРУГОЕ- '''
btn_other_1 = KeyboardButton('другое 1 ♐️')
btn_other_2 = KeyboardButton('другое 2 ♐️')
menu_other = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_other_1, btn_other_2, btn_return)
