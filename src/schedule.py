import datetime


class Schedule:
    week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']

    current_schedule = {'Понедельник': [""] * 7, 'Вторник': [""] * 7, 'Среда': [""] * 7, 'Четверг': [""] * 7,
                        'Пятница': [""] * 7, 'Суббота': [""] * 7}

    schedule_of_new_subject = {'Понедельник': [-1] * 7, 'Вторник': [-1] * 7, 'Среда': [-1] * 7, 'Четверг': [-1] * 7,
                               'Пятница': [-1] * 7, 'Суббота': [-1] * 7}

    current_subject = ""

    time_of_class = ["9:00 -- 10:25", "10:45 -- 12:10", "12:20 -- 13:45", "13:55 -- 15:20", "15:30 -- 16:55",
                     "17:05 -- 18:30", "18:35 -- 20:00"]

    @classmethod
    def get_schedule_of_day(cls, day):
        schedule = day + ":\n"

        flag_empty = True
        for i in range(7):
            if cls.current_schedule[day][i] != "":
                schedule += f"Пара:  {i + 1}\n"
                schedule += f"Дисциплина:  {cls.current_schedule[day][i]}\n"
                schedule += f"Время:  " + cls.time_of_class[i] + "\n"
                schedule += "____________________________________\n\n"
                flag_empty = False

        if flag_empty:
            schedule += f"Пар нет"

        return schedule

    @classmethod
    def get_schedule(cls):
        schedule = []
        for day in cls.current_schedule:
            schedule.append(cls.get_schedule_of_day(day))

        return schedule

    @classmethod
    def update_schedule(cls):
        for key in cls.schedule_of_new_subject:
            for i in range(7):
                if cls.schedule_of_new_subject[key][i] == 1:
                    cls.current_schedule[key][i] = Schedule.current_subject
            cls.schedule_of_new_subject[key] = [-1] * 7

    @classmethod
    def get_todays_schedule(cls):
        day_of_the_week = datetime.datetime.today().weekday()
        if day_of_the_week == 6:
            text = "Сегодня вых, зачилься"
        else:
            text = cls.get_schedule_of_day(cls.week[day_of_the_week])

        return text
