from re import match


def get_first_group(regex, text):
    return match(regex, text).groups()[0]


def remove_id_from_url(url):
    if '#' in url:
        index_of_id_char = url.index('#')
        url_without_id = url[0: index_of_id_char]
        return url_without_id
    return url


def remove_start_and_end_spaces(text):
    without_initial_spaces = get_first_group('\s*(\S.*)', text)
    without_end_spaces = get_first_group('(.*\S)\s*', without_initial_spaces)
    return without_end_spaces


def remove_content_from_parentheses(text):
    index_of_parentheses = text.index('(')
    text_before_parentheses = text[0:index_of_parentheses]
    return text_before_parentheses


def format_name(name):
    name = name.lower()
    text_before_parentheses = remove_content_from_parentheses(name)
    return remove_start_and_end_spaces(text_before_parentheses)


