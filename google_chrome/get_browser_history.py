"""This module generates a list from the visit history and writes it to a file."""
import sqlite3
import datetime

def get_chrome(con: sqlite3.Connection) -> list:
    """
    Reads database of Chrome history and process data
    :param con: database connection
    :return: list of visits
    """
    c = con.cursor()

    c.execute("select id, url, title from urls")
    url_id_tuples = c.fetchall()
    url_id = {id_num: (url, title) for id_num, url, title in url_id_tuples}

    c.execute("select url, visit_time, visit_duration from visits")
    results_with_url_as_id = c.fetchall()

    results = []

    for id_num, visit_time, visit_duration in results_with_url_as_id[:10]:
        url, title = url_id[id_num]
        # [Google Chrome's] timestamp is formatted as the number of
        # microseconds since January, 1601.
        # To convert this to seconds, which is the standard for Python's
        # datetime module, we divide by 1,000,000.
        # Chrome's timestamps are based on the Windows epoch, which starts
        # on January 1, 1601. The Unix epoch starts on January 1, 1970.
        # The difference between these two dates is 11,644,473,600 seconds
        date, time = str(
            (datetime.datetime.fromtimestamp(visit_time / 1000000 - 11644473600))).split()
        results.append((url, title, date, time, visit_duration))

    c.close()
    return results


def get_chrome_os(user: str, os: str) -> list:
    """
    Reads Chrome History on Linux
    Returns list of tuples. Each tuple has structure:
    (url: srt, title: str, date_of_last_visit: str("yyyy-mm-dd"),
    time_of_last_visit: str("hh:mm:ss.ms"), time_of_visit: int)

    :param user: username of computer
    :param os: OS of computer. Can be "Windows", "Linux" or "MacOS"

    :return: list of visits
    """
    match os:
        case "Linux":
            con = sqlite3.connect(f'/home/{user}/.config/google-chrome/Default/History')
        case "Windows":
            con = sqlite3.connect(
                (f'C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/History'))
        case "MacOS":
            con = sqlite3.connect(
                (f'/Users/{user}/Library/Application Support/Google/Chrome/Default/History'))
        case _:
            raise ValueError("Incorrect OS")
    return get_chrome(con)


def write_data_to_file(history: list, filename: str) -> None:
    """
    Writes data to file
    :param history: list of visits of browser
    :param filename: name of file to write
    :return:
    """
    with open(filename, "w", encoding='utf-8') as file:
        for element in history:
            file.write(str(element) + "\n")
