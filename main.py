from os import environ
from os.path import isfile

from pandas import DataFrame, read_csv
from dotenv import load_dotenv

from src.driver import get_driver
from src.all_languages import get_df_with_all_languages
from src.all_languages_details import get_all_languages_details_in_df
from src.consts import (
    path_to_links_dataset,
    path_to_all_languages_dataset,
    link_to_all_languages)


load_dotenv()


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


def use_a_small_df_to_test(df):
    if bool(environ.get('TESTING')):
        df = df[:][0:1]
    return df


if __name__ == '__main__':
    driver = get_driver()
    df_with_links = get_df_with_links(driver)
    df_with_links = use_a_small_df_to_test(df_with_links)
    df_with_details = get_all_languages_details_in_df(
        driver, df_with_links['source'])
    df = df_with_links.merge(
        df_with_details, left_index=True, right_index=True)
    df.to_csv(
        path_to_all_languages_dataset,
        sep='\t',
        index=False)
    driver.quit()


