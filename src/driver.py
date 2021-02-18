from os import environ

from selenium import webdriver
from dotenv import load_dotenv


load_dotenv()


firefox_path = environ.get('FIREFOX_PATH')
driver_path = environ.get('DRIVER_PATH')


def get_driver():
    if firefox_path and driver_path:
        return webdriver.Firefox(
            firefox_binary=firefox_path,
            executable_path=driver_path)
    else:
        return webdriver.Firefox()


