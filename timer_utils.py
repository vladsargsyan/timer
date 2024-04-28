# timer_utils.py


def parse_time_input(time_str):
    try:
        hours, minutes, seconds = map(int, time_str.split(':'))
        return hours * 3600 + minutes * 60 + seconds
    except ValueError:
        return None
