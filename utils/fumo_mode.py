# This file is strictly a joke. Fumo friday.
import datetime

day = datetime.datetime.today().weekday()


def friday_check():
    if day == 4:
        return True
    return False
