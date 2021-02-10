from pandas import DataFrame

from .driver import get_driver
from .consts import link_to_all_languages, log_path


def get_all_div_with_languages(driver):
    return driver.find_elements_by_css_selector('.div-col')


def get_links_to_languages_from_div(div):
    return div.find_elements_by_css_selector('a')


def get_language_info_from_link(link):
    return {
        'name': link.get_property('title'),
        'link': link.get_property('href')}


def get_all_languages_from_div(div):
    all_links = get_links_to_languages_from_div(div)
    all_names = map(get_language_info_from_link, all_links)
    return list(all_names)


def get_all_languages_from_divs(divs):
    all_languages = []
    for div in divs:
        all_languages += get_all_languages_from_div(div)
    return all_languages


def get_all_languages():
    driver = get_driver()
    driver.get(link_to_all_languages)
    divs_with_languages = get_all_div_with_languages(driver)
    all_languages = get_all_languages_from_divs(divs_with_languages)
    driver.quit()
    return all_languages


if __name__ == '__main__':
    all_languages = get_all_languages()
    df = DataFrame(all_languages)
    df.to_csv(log_path + 'name_link.csv', sep=';', index=False)


