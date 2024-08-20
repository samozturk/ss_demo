import wikipedia


def get_wiki_summary(city:str) -> str:
    """
Retrieves a summary of the Wikipedia page for the given city.

Args:
    city (str): The name of the city to search for on Wikipedia.

Returns:
    str: A summary of the Wikipedia page for the given city.
"""
    results = wikipedia.search(city)
    wiki_pagename = results[0]
    page_summary = wikipedia.summary(wiki_pagename)#
    return page_summary