from selenium import webdriver

from .consts import driver_path, firefox_path


driver = webdriver.Firefox(
    firefox_binary=firefox_path,
    executable_path=driver_path
)


