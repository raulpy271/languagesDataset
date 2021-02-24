import pandas

from src.consts import path_to_all_languages_dataset
from src.utils import change_types_to_save_memory


languages_without_memory_saved = (
    pandas.read_csv(path_to_all_languages_dataset, sep='\t'))


languages = change_types_to_save_memory(languages_without_memory_saved, pandas)


