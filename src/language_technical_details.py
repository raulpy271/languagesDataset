from .driver import get_driver


def get_infobox_rows(driver):
    infobox_table = driver.find_element_by_css_selector('table>tbody')
    rows_in_infobox = infobox_table.find_elements_by_css_selector('tr')
    return rows_in_infobox


def get_row_from_infobox_with_an_specific_text(driver, text):
    text = text.lower()
    for row in get_infobox_rows(driver):
        if text in (row.text.lower()):
            return row


def get_website(driver):
    text_to_search = 'website'
    website_tr = (
        get_row_from_infobox_with_an_specific_text(driver, text_to_search)) 
    if website_tr:
        website_link_element = website_tr.find_element_by_css_selector('a')
        link_str = website_link_element.get_attribute('href')
        return link_str


def get_first_paragraph(driver):
    first_paragraph = ''
    all_paragraphs = driver.find_elements_by_css_selector(
        'div.mw-parser-output>p')
    for paragraph in all_paragraphs:
        if paragraph.text:
            first_paragraph = paragraph.text
            break
    return first_paragraph


def get_details_about_language_from_wiki(driver, language_wiki):
    language_details = {'link': language_wiki}
    driver.get(language_wiki)
    language_details['about'] = get_first_paragraph(driver)
    website = get_website(driver)
    if website:
        language_details['link'] = website
    return language_details


if __name__ == '__main__':
    driver = get_driver()
    language_wiki = (
        'https://en.wikipedia.org/wiki/Clojure')
    language_details = get_details_about_language_from_wiki(
        driver,
        language_wiki)
    print(language_details)
    driver.quit()


