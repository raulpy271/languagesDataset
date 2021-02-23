

def get_infobox_rows(driver):
    try:
        infobox_selector = 'table.infobox>tbody'
        infobox_table = driver.find_element_by_css_selector(infobox_selector)
        rows_in_infobox = infobox_table.find_elements_by_css_selector('tr')
    except:
        rows_in_infobox = []
    finally:
        return rows_in_infobox


def get_row_from_infobox_with_an_specific_text(driver, text):
    text = text.lower()
    for row in get_infobox_rows(driver):
        if text in (row.text.lower()):
            row_data = row.find_element_by_css_selector('td')
            return row_data


def get_row_from_infobox_with_a_text_from_a_list(driver, list_of_text):
    for text in list_of_text:
        row = get_row_from_infobox_with_an_specific_text(text)
        if row:
            return row


