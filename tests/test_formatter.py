import datetime
from utils.formatters import DateTimeFormatter

def test_formatter():
    expected_day  = "05-07-2025"
    expected_time = "19-00"

    formatter = DateTimeFormatter()

    date = datetime.datetime(2025, 7, 5, 19, 00) 

    day = formatter.day(date)
    _time = formatter.time(date)

    assert day == expected_day and _time == expected_time
