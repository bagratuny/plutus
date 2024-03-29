from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import datetime
import os


def init_browser():
    options = Options()
    options.headless = True
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(2300, 2000)
    return browser


def make_screenshot(link, user, date, filename):
    browser = init_browser()
    browser.get(link)

    try:
        button = browser.find_element_by_xpath(
            '// *[@id="disclaimer-modal"]/div/div/div/div/div[1]/div/a[1]')
        button.click()
    except:
        print('cannot find button')

    try:
        container = browser.find_element_by_xpath(
            '/html/body/div[2]/div[3]/div/div/div[1]/div/div/div/div/div[3]/div[6]/div')
        browser.execute_script(
            "arguments[0].style.overflow = 'unset';", container)
    except:
        print('cannot find container')

    try:
        container_wrapper = browser.find_element_by_css_selector(
            'body > div.page > div.page__main > div > div')
        browser.execute_script(
            "arguments[0].style.width = 'auto';", container_wrapper)
    except:
        print('cannot find container__wrapper')

    try:
        os.mkdir('folder/{}'.format(user))
        os.mkdir('folder/{}/{}'.format(user, date))
    except FileExistsError:
        print('folder already exist')

    sleep(2)

    path_to_file = 'folder/{}/{}/{}.png'.format(
        user, date, filename)

    browser.save_screenshot(path_to_file)

    try:
        location = container_wrapper.location
        size = container_wrapper.size

        x = location['x']
        y = location['y']
        width = location['x']+size['width']
        height = location['y']+size['height']

        im = Image.open(path_to_file)
        im = im.crop((int(x), int(y), int(width), int(height)))
        im.save(path_to_file)
    except:
        print()

    browser.quit()

    # sleep(15)
