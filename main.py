from users import USERS
from links import LINKS
import telebot
import time
import datetime
import screens


BOT_TOKEN = LINKS.get('token')

bot = telebot.TeleBot(BOT_TOKEN)


def scan(sites):
    now = datetime.datetime.now()
    browser = screens.init_browser()
    for key, site in sites:
        print(site, user)
        screens.make_screenshot(site, browser, user, now.day, key)
        document = open(
            "folder/{}/{}/{}.png".format(user, now.day, key), "rb")
        bot.send_document(user, document)
    browser.close()


say_hi = 'Доброго времени суток, {}! Скоро пришлю файлы.\nВремя: {}, ваш ID: {}'

while True:
    now = datetime.datetime.now()
    for user in USERS.keys():
        print("Пользователь: {}:{}, время: {}".format(
            user, USERS[user]['name'], now))

        if USERS[user]['time'] == 'day' and now.hour >= 12:
            bot.send_message(
                user, say_hi.format(
                    USERS[user]['name'], now, user))
            scan(USERS[user]['sites'].items())
        elif USERS[user]['time'] == 'night' and now.hour >= 0 and now.hour < 12:
            bot.send_message(
                user, say_hi.format(
                    USERS[user]['name'], now, user))
            scan(USERS[user]['sites'].items())

    time.sleep(60)
