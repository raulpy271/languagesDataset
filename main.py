from os import environ
from os.path import isfile

from pandas import DataFrame, read_csv

from src.driver import get_driver
from src.consts import path_to_links_dataset, link_to_all_languages
from src.all_languages import get_df_with_all_languages
from src.all_languages_details import get_all_languages_details_in_df


def create_links_tsv(driver):
    df = get_df_with_all_languages(driver, link_to_all_languages)
    df.to_csv(
        path_to_links_dataset,
        sep='\t',
        index=False)


def get_df_with_links(driver):
    if not isfile(path_to_links_dataset):
        create_links_tsv(driver)
    return read_csv(path_to_links_dataset, sep='\t')


if __name__ == '__main__':
    driver = get_driver()
    df_with_links = get_df_with_links(driver)
    df = get_all_languages_details_in_df(driver, df_with_links['link'][:50:10])
    driver.quit()


