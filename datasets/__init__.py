from pandas import read_csv

from src.consts import path_to_all_languages_dataset


languages = read_csv(path_to_all_languages_dataset, sep='\t')


