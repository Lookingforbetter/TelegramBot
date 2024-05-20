import os
import telebot

from src.buttons import *


class Bot:
    bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

    @classmethod
    def show_main_menu(cls, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(Buttons.button_week_schedule, Buttons.button_todays_schedule)
        markup.add(Buttons.button_change_schedule)
        cls.bot.send_message(message.chat.id, 'Выберите', reply_markup=markup)

    @classmethod
    def show_with_button_back(cls, schedule, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(Buttons.button_back)
        for i in range(len(schedule)):
            cls.bot.send_message(message.chat.id, schedule[i], reply_markup=markup)

    @classmethod
    def show_week_menu(cls, message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        markup.add(Buttons.buttons_days[0], Buttons.buttons_days[1], Buttons.buttons_days[2], Buttons.buttons_days[3],
                   Buttons.buttons_days[4], Buttons.buttons_days[5], Buttons.button_finish)
        cls.bot.send_message(message.chat.id, 'Выберите день', reply_markup=markup)

    @classmethod
    def end_of_changing_day_schedule(cls, call):
        cls.bot.delete_message(call.message.chat.id, call.message.message_id)
        cls.show_week_menu(call.message)

    @classmethod
    def get_subject_and_start_changing(cls, message):
        Schedule.current_subject = message.text
        cls.show_week_menu(message)

    @classmethod
    def start_changing_schedule(cls, message):
        sent = cls.bot.send_message(message.chat.id, 'Введите название предмета, который вы хотите добавить')
        cls.bot.register_next_step_handler(sent, cls.get_subject_and_start_changing)

    @classmethod
    def get_markup_inline_for_changing_menu(cls, day):
        markup_inline = types.InlineKeyboardMarkup(row_width=2)

        buttons = []
        for i in range(1, 8):
            if Schedule.schedule_of_new_subject[day][i - 1] == 1:
                buttons.append(types.InlineKeyboardButton(text=f'{i} пара ✅', callback_data=f'{i} ' + day))
            else:
                buttons.append(types.InlineKeyboardButton(text=f'{i} пара', callback_data=f'{i} ' + day))

        markup_inline.add(buttons[0], buttons[1], buttons[2], buttons[3], buttons[4], buttons[5], buttons[6])

        markup_inline.add(types.InlineKeyboardButton(text=f'Готово', callback_data="ready " + day))

        return markup_inline

    @classmethod
    def first_show_changing_schedule_menu(cls, message):
        markup_inline = cls.get_markup_inline_for_changing_menu(message.text)
        cls.bot.send_message(message.chat.id, f'{message.text}: выберите пары:', reply_markup=markup_inline)

    @classmethod
    def show_changing_schedule_menu(cls, call, day):
        markup_inline = cls.get_markup_inline_for_changing_menu(day)
        cls.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text=day + ": выберите пары:", reply_markup=markup_inline)
