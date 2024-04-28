# main.py
from timer_utils import parse_time_input
from countdown import countdown_timer


def main():
    user_input = input("Insert time to count down (h:m:s): ")
    total_seconds = parse_time_input(user_input)

    if total_seconds is None or total_seconds <= 0:
        print("Invalid input. Please enter a valid time in the format h:m:s.")
        return

    print("Countdown started:")
    countdown_timer(total_seconds)
    print("Countdown complete!")


if __name__ == "__main__":
    main()
