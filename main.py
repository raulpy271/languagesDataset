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


def create_links_tsv(driver, path):
    df = get_df_with_all_languages(driver, link_to_all_languages)
    df.to_csv(path, sep='\t', index=False)


def get_df_with_links(driver, df_path):
    if not isfile(df_path):
        create_links_tsv(driver)
    return read_csv(df_path, sep='\t')


def use_a_small_df_if_is_test_env(df):
    if bool(environ.get('TESTING')):
        df = df[:][0:10]
    return df


def main():
    driver = get_driver()


    print('Getting dataset with all language links\n')
    df_with_links = get_df_with_links(driver, path_to_links_dataset)
    df_with_links = use_a_small_df_if_is_test_env(df_with_links)
    print(f'Dataset with {len(df_with_links)} languages links created\n')


    print('Getting dataset with all language details')
    df_with_details = get_all_languages_details_in_df(
        driver, df_with_links['source'])
    df = df_with_links.merge(
        df_with_details, left_index=True, right_index=True)
    df.to_csv(
        path_to_all_languages_dataset,
        sep='\t',
        index=False)
    driver.quit()


if __name__ == '__main__':
    main()
    print('\nDataset with all language details saved in:',
          path_to_all_languages_dataset)


