__author__ = 'uwe'


from datetime import date, timedelta
from os import remove
from os.path import exists
import bz2

# def getBackDOY(backDay, _year=date.today().year):
#     d0 = date(_year-1, 12, 31)
#     d1 = date.today() - timedelta(int(backDay))
#     delta=d1-d0
#     return delta.days

def getBackDate(backDay):
    _back_date = date.today() - timedelta(backDay)
    return _back_date

def getBackDateStr(backDay):
    _back_date = date.today() - timedelta(backDay)
    return str(_back_date.year) + str(_back_date.month).zfill(2) + str(_back_date.day).zfill(2)


def getDOY(_year, _month, _day):
    d1 = date(int(_year), int(_month), int(_day))
    d0 = date(int(_year)-1, 12, 31)
    delta=d1-d0
    return delta.days

def ensureTrailingSlash(path):
    if not path.endswith('/'):
        return path + '/'
    else:
        return path

def exit_on_empty_list(list):
    _size = len(list)
    if not _size:
        print("Nothing to do here. Now quitting.")
        exit(1)
    else:
        return _size

