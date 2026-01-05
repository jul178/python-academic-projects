"""This module provides tools for analysing Google Chrome browsing history."""
from get_browser_history import get_chrome_os

def sites_on_date(visits: list, date: str)-> set[str]:
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in the browser history
    (you get it as the result of the fucntion get_chrome_os
    from get_browser_history module)
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    >>> visits = [
    ...     ("a.com", "A", "2025-01-20", "09:00:21", 5),
    ...     ("b.com", "B", "2025-04-01", "02:43:11", 3),
    ...     ("a.com", "A", "2024-08-01", "12:00:00", 4)
    ... ]
    >>> sites_on_date(visits, "2024-08-01")
    {'a.com'}
    >>> sites_on_date(visits, "2025-06-28")
    set()
    """
    url_on_date = set()
    for url, _, date_of_last_visit, _, _ in visits:
        if date == date_of_last_visit:
            url_on_date.add(url)

    return url_on_date

def most_frequent_sites(visits: list, number: int)-> set[str]:
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    If the frequence is the same choose sites in the alphabetical order
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    >>> visits = [
    ...     ("a.com", "A", "2025-01-20", "09:00:21", 5),
    ...     ("b.com", "B", "2025-04-01", "02:43:11", 3),
    ...     ("a.com", "A", "2024-08-01", "12:00:00", 4),
    ...     ("c.com", "C", "2024-01-03", "13:10:00", 2)
    ... ]
    >>> most_frequent_sites(visits, 1)
    {'a.com'}
    >>> a = most_frequent_sites(visits, 5)
    >>> {'a.com', 'b.com', 'c.com'} <= a
    True
    """
    frequent_sites = {}

    for url, _, _, _, _ in visits:
        if url in frequent_sites:
            frequent_sites[url] += 1
        else:
            frequent_sites[url] = 1

    if number >= len(frequent_sites):
        return set(sorted(frequent_sites.keys()))

    sorted_urls = sorted(frequent_sites.items(), key=lambda url: url[0]) #sort by alphabet order
    sorted_urls = sorted(sorted_urls, key=lambda url: url[1], reverse=True) #sort by frequenses

    result = set()
    for url, _ in sorted_urls[:number]:
        result.add(url)

    return result


def get_url_info(visits: list, url: str)->tuple:
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)

    If url was not visited, title and last visit date/time should be empty strings,
    number of visits and average time should be zeros
    >>> visits = [
    ...     ("a.com", "A", "2024-09-17", "10:00:00", 5),
    ...     ("b.com", "B", "2024-01-02", "11:00:00", 3),
    ...     ("a.com", "A", "2024-01-03", "09:00:00", 7)
    ... ]
    >>> get_url_info(visits, "a.com")
    ('A', '2024-09-17', '10:00:00', 2, 6.0)
    >>> get_url_info(visits, "x.com")
    ('', '', '', 0, 0)
    """
    list_of_searched_site = []
    for el in visits:
        if el[0] == url:
            list_of_searched_site.append(el)

    if len(list_of_searched_site) == 0:
        return ('', '', '', 0, 0)

    title = list_of_searched_site[0][1]
    last_visit_date = list_of_searched_site[0][2]
    last_visit_time = list_of_searched_site[0][3]
    total_time = 0

    for el in list_of_searched_site:
        date = el[2]
        time = el[3]

        # if (date > last_visit_date or date == last_visit_date or
        #     time > last_visit_time or time == last_visit_time):
        #     last_visit_date = date
        #     last_visit_time = time
        if date > last_visit_date:
            last_visit_date = date
            last_visit_time = time
        elif date == last_visit_date and time > last_visit_time:
            last_visit_date = date
            last_visit_time = time

        total_time += el[4]
    num_of_visits = len(list_of_searched_site)
    average_time = total_time / num_of_visits

    result = (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    return result


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

    os = input("Your OS: ")
    user = input("Your username: ")

    VISITS = get_chrome_os(user, os)
