# countdown.py
import time
from timer_utils import parse_time_input


def countdown_timer(total_seconds):
    while total_seconds > 0:
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        total_seconds -= 1
