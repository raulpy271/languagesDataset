from .driver import get_driver
from .utils import get_year
from .finders import (
    get_infobox_rows,
    get_row_from_infobox_with_an_specific_text,
    get_row_from_infobox_with_a_text_from_a_list)


def get_year_of_first_release(driver):
    text_to_search = ['initial release', 'first appeared']
    initial_release_td = (
        get_row_from_infobox_with_a_text_from_a_list(driver, text_to_search)) 
    if initial_release_td:
        text_initial_release = initial_release_td.text
        year = get_year(text_initial_release)
        return year


def get_list_of_type_systems(driver):
    text_to_search = 'typing'
    typing_td = (
        get_row_from_infobox_with_an_specific_text(driver, text_to_search)) 
    if typing_td:
        link_elements_with_types = typing_td.find_elements_by_css_selector('a')
        if link_elements_with_types:
            types = map(
                lambda element: element.text, link_elements_with_types)
            return list(types)


def get_paradigms(driver):
    text_to_search = 'paradigm'
    paradigms_td = (
        get_row_from_infobox_with_an_specific_text(driver, text_to_search)) 
    if paradigms_td:
        link_elements_with_paradigms = (
            paradigms_td.find_elements_by_css_selector('a'))
        if link_elements_with_paradigms:
            paradigms = map(
                lambda element: element.text, link_elements_with_paradigms)
            return list(paradigms)


def get_website(driver):
    text_to_search = 'website'
    website_td = (
        get_row_from_infobox_with_an_specific_text(driver, text_to_search)) 
    if website_td:
        website_link_element = website_td.find_element_by_css_selector('a')
        link_str = website_link_element.get_attribute('href')
        return link_str


def get_first_paragraph(driver):
    all_paragraphs = driver.find_elements_by_css_selector(
        'div.mw-parser-output>p')
    for paragraph in all_paragraphs:
        if paragraph.text:
            first_paragraph = paragraph.text
            return first_paragraph


def get_details_about_language_from_wiki(driver, language_wiki):
    language_details = {}
    driver.get(language_wiki)
    language_details['about'] = get_first_paragraph(driver)
    language_details['first_release'] = get_year_of_first_release(driver)
    language_details['types'] = get_list_of_type_systems(driver)
    language_details['paradigms'] = get_paradigms(driver)
    language_details['website'] = get_website(driver)
    return language_details


if __name__ == '__main__':
    driver = get_driver()
    language_wiki = (
        'https://en.wikipedia.org/wiki/Bash_(Unix_shell)')
    language_details = get_details_about_language_from_wiki(
        driver,
        language_wiki)
    print(language_details)
    driver.quit()


