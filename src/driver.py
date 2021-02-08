from os import environ

from selenium import webdriver
from dotenv import load_dotenv


load_dotenv()


firefox_path = environ.get('firefox_path')
driver_path = environ.get('driver_path')


def get_driver():
    if firefox_path and driver_path:
        return webdriver.Firefox(
            firefox_binary=firefox_path,
            executable_path=driver_path)
    else:
        return webdriver.Firefox()


