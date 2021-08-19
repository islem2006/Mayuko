# This file is strictly a joke. Fumo friday.
# UPDATE: THIS IS NO LONGER IMPLEMENTED!
# SEE https://github.com/DynamicDonkey/Mayuko/blob/master/assets/CHANGELOG.md#14-8-21
import datetime

day = datetime.datetime.today().weekday()


def friday_check():
    if day == 4:
        return True
    return False
