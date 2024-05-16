from src.schedule import *
from telebot import types


class Buttons:
    button_week_schedule = types.KeyboardButton('Расписание недели')
    button_todays_schedule = types.KeyboardButton('Сегодняшнее расписание')
    button_change_schedule = types.KeyboardButton('Изменить расписание')
    button_back = types.KeyboardButton('Назад')
    button_finish = types.KeyboardButton('Закончить')
    buttons_days = []
    for day in Schedule.week:
        buttons_days.append(types.KeyboardButton(day))
