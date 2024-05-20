from src.bot import *


@Bot.bot.message_handler(commands=['start'])
def start(message):
    Bot.show_main_menu(message)


@Bot.bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Назад':
            Bot.show_main_menu(message)

        elif message.text == 'Закончить':
            Schedule.update_schedule()
            Bot.show_main_menu(message)

        elif message.text == 'Расписание недели':
            Bot.show_with_button_back(Schedule.get_schedule(), message)

        elif message.text == 'Сегодняшнее расписание':
            todays_schedule = Schedule.get_todays_schedule()
            Bot.show_with_button_back([todays_schedule], message)

        elif message.text == 'Изменить расписание':
            Bot.start_changing_schedule(message)

        elif message.text in Schedule.current_schedule:
            Bot.first_show_changing_schedule_menu(message)


@Bot.bot.callback_query_handler(func=lambda call: True)
def answer(call):
    day = call.data.split()[1]

    if call.data.split()[0] == "ready":
        Bot.end_of_changing_day_schedule(call)
    else:
        num_of_class = int(call.data.split()[0])
        Schedule.schedule_of_new_subject[day][num_of_class - 1] *= (-1)
        Bot.show_changing_schedule_menu(call, day)


Bot.bot.polling(none_stop=True)
