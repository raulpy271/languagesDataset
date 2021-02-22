from re import match


def get_first_group(regex, text):
    return match(regex, text).groups()[0]


def remove_id_from_url(url):
    if '#' in url:
        index_of_id_char = url.index('#')
        url_without_id = url[0: index_of_id_char]
        return url_without_id
    return url


def link_is_broken(link):
    title = link.get_attribute('title')
    if ('new' in link.get_attribute('class')
            or 'action=edit' in link.get_attribute('href')
            or 'page does not exist' in title):
        return True
    return False


def link_isnt_broken(link):
    return not link_is_broken(link)


def remove_start_and_end_spaces(text):
    without_initial_spaces = get_first_group('\s*(\S.*)', text)
    without_end_spaces = get_first_group('(.*\S)\s*', without_initial_spaces)
    return without_end_spaces


def remove_content_from_parentheses(text):
    index_of_parentheses = text.index('(')
    text_before_parentheses = text[0:index_of_parentheses]
    return text_before_parentheses


def should_remove_parentheses(text):
    return '(' in text and ')' in text


def format_name(name):
    name = name.lower()
    if should_remove_parentheses(name):
        name = remove_content_from_parentheses(name)
    return remove_start_and_end_spaces(name)


