from pandas import DataFrame

from .driver import get_driver
from .utils import remove_id_from_url
from .consts import link_to_all_languages, path_to_links_dataset


def get_all_div_with_languages(driver):
    return driver.find_elements_by_css_selector('.div-col')


def get_links_to_languages_from_div(div):
    return div.find_elements_by_css_selector('a')


def get_language_info_from_link(link):
    return {
        'name': link.get_property('title'),
        'source': link.get_property('href')}


def get_all_languages_from_div(div):
    all_links = get_links_to_languages_from_div(div)
    all_names = map(get_language_info_from_link, all_links)
    return list(all_names)


def get_all_languages_from_divs(divs):
    all_languages = []
    for div in divs:
        all_languages += get_all_languages_from_div(div)
    return all_languages


def get_all_languages(driver, link_to_all_languages):
    driver.get(link_to_all_languages)
    divs_with_languages = get_all_div_with_languages(driver)
    all_languages = get_all_languages_from_divs(divs_with_languages)
    return all_languages


def get_df_with_all_languages(driver, link_to_all_languages):
    all_languages = get_all_languages(driver, link_to_all_languages)
    df = DataFrame(all_languages)
    df['source'] = df['source'].map(remove_id_from_url)
    df = df.drop_duplicates()
    return df


if __name__ == '__main__':
    driver = get_driver()
    df = get_df_with_all_languages(driver, link_to_all_languages)
    df.to_csv(
        path_to_links_dataset,
        sep='\t',
        index=False)
    driver.quit()


