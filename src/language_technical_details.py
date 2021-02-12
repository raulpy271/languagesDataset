from .driver import get_driver


def get_first_paragraph(driver):
    all_paragraphs = driver.find_elements_by_css_selector(
        'div.mw-parser-output>p')
    first_paragraph = all_paragraphs[0]
    return first_paragraph.text


def get_details_about_language_from_wiki(driver, language_wiki):
    language_details = {
        'link': language_wiki}
    driver.get(language_wiki)
    language_details['about'] = get_first_paragraph(driver)
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


