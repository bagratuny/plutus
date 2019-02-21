from users import USERS
from links import LINKS
import telebot
import time
import datetime
import screens


BOT_TOKEN = LINKS.get('token')

say_hi = 'Доброго времени суток, {}! Скоро пришлю файлы.\nВремя (UTC±0:00): {}, ваш ID: {}'

bot = telebot.TeleBot(BOT_TOKEN)


def scan(sites):
    print("\n------- NEW SCAN -------\n")
    for key, site in sites:
        print(site, user)
        screens.make_screenshot(site, user, datetime.datetime.now().day, key)
        document = open(
            "folder/{}/{}/{}.png".format(user, datetime.datetime.now().day, key), "rb")
        try:
            bot.send_document(user, document)
        except telebot.apihelper.ApiException:
            bot.send_message(user, "Error: telebot.apihelper.ApiException")
        time.sleep(5)
    bot.send_message(
        user, 'Время (UTC±0:00): {}\nСеанс окончен. До завтра!'.format(datetime.datetime.now()))
    print("\n------- END SCAN -------\n")
    time.sleep(5)


while True:
    now = datetime.datetime.now()
    for user in USERS.keys():
        print("Пользователь: {}:{}, время: {}".format(
            user, USERS[user]['name'], datetime.datetime.now()))

        if USERS[user]['time'] == 'day' and now.hour > 6 and now.hour <= 16:
            bot.send_message(
                user, say_hi.format(
                    USERS[user]['name'], datetime.datetime.now(), user))
            scan(USERS[user]['sites'].items())
        elif USERS[user]['time'] == 'night' and (now.hour > 16 or now.hour <= 6):
            bot.send_message(
                user, say_hi.format(
                    USERS[user]['name'], datetime.datetime.now(), user))
            scan(USERS[user]['sites'].items())

    time.sleep(43200)
