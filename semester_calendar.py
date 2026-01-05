""" A module for generating formatted calendars for a specific range of months.

This module provides a function to create a calendar for a period such as an
academic semester, with support for both plain text and HTML output formats.
"""
import calendar
def get_semester_calendar(output_type: str, year: int,
                          first_month: int, last_month: int) -> str | None:
    """
    Construct and present the academic semester calendar in txt and html (HTML table) form.

    param output_type: str, The desired format. Accepts 'txt' for plain
                        text or 'html' for an HTML table.
    param year: int, The year for the calendar.
    param first_month: int, The starting month of the period (1-12).
    param last_month: int, The ending month of the period (1-12). Must be
                    greater than or equal to first_month.
    return: str or None, A single string containing the formatted calendar for the
                    entire period, or None if the input parameters are
                    invalid
    >>> get_semester_calendar("txt", 2024, 10, 10)
    '    October 2024\\n\
Mo Tu We Th Fr Sa Su\\n\
    1  2  3  4  5  6\\n\
 7  8  9 10 11 12 13\\n\
14 15 16 17 18 19 20\\n\
21 22 23 24 25 26 27\\n\
28 29 30 31\\n'
    >>> get_semester_calendar("html", 2024, 10, 10)
    '<table border="0" cellpadding="0" cellspacing="0" class="month">\\n\
<tr><th colspan="7" class="month">October 2024</th></tr>\\n\
<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th>\
<th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th>\
<th class="sun">Sun</th></tr>\\n<tr><td class="noday">&nbsp;</td><td class="tue">1</td>\
<td class="wed">2</td><td class="thu">3</td><td class="fri">4</td><td class="sat">5</td>\
<td class="sun">6</td></tr>\\n<tr><td class="mon">7</td><td class="tue">8</td>\
<td class="wed">9</td><td class="thu">10</td><td class="fri">11</td><td class="sat">12</td>\
<td class="sun">13</td></tr>\\n<tr><td class="mon">14</td><td class="tue">15</td>\
<td class="wed">16</td><td class="thu">17</td><td class="fri">18</td><td class="sat">19</td>\
<td class="sun">20</td></tr>\\n<tr><td class="mon">21</td><td class="tue">22</td>\
<td class="wed">23</td><td class="thu">24</td><td class="fri">25</td><td class="sat">26</td>\
<td class="sun">27</td></tr>\\n<tr><td class="mon">28</td><td class="tue">29</td>\
<td class="wed">30</td><td class="thu">31</td><td class="noday">&nbsp;</td>\
<td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>\\n</table>\\n'
    >>> get_semester_calendar("pdf", 2024, 10, 12)
    >>> get_semester_calendar("txt", 2024, 13, 15)
    """
    if isinstance(year, int) and isinstance(first_month, int) and isinstance(last_month, int):
        if 1 <= first_month <= 12 and 1 <= last_month <= 12 and first_month <= last_month:
            result = []
            if output_type == 'txt':
                cal = calendar.TextCalendar()
                for i in range(first_month, last_month + 1):
                    month_txt = cal.formatmonth(year, i)
                    result.append(month_txt)

                return ''.join(result)

            if output_type == 'html':
                cal = calendar.HTMLCalendar()
                for i in range(first_month, last_month + 1):
                    month_html = cal.formatmonth(year, i)
                    result.append(month_html)

                return ''.join(result)
            return None
        return None
    return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
