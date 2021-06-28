# do not execute function (working) if time is between 10 AM and 10 PM
import datetime
import time


class OutsideWorkingHours(Exception):
    pass


def working_hours(start_time, end_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            hour = datetime.datetime.now().hour
            if start_time.hour > hour or hour > end_time.hour:
                raise OutsideWorkingHours('This can only be executed during working hours')
            result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@working_hours(datetime.time(hour=10), datetime.time(hour=22))
def working(work: str):
    print(f"Working on: {work}")
    time.sleep(3)


working('My Job')
