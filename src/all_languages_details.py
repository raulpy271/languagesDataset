from pandas import DataFrame, read_csv

from .driver import get_driver
from .consts import log_path
from .language_technical_details import get_details_about_language_from_wiki


def get_all_languages_details(driver, languages_links):
    all_languages_details = []
    for link in languages_links:
        driver.get(link)
        language_details = get_details_about_language_from_wiki(driver, link)
        all_languages_details.append(language_details)
    return all_languages_details


def get_all_languages_details_in_df(driver, languages_links):
    all_languages_details = get_all_languages_details(driver, languages_links)
    df = DataFrame(all_languages_details)
    return df


if __name__ == '__main__':
    driver = get_driver()
    df = read_csv(log_path + 'links.tsv', sep='\t')
    df = get_all_languages_details_in_df(driver, df['link'])
    driver.quit()

