

def remove_id_from_url(url):
    if '#' in url:
        index_of_id_char = url.index('#')
        url_without_id = url[0: index_of_id_char]
        return url_without_id
    return url


