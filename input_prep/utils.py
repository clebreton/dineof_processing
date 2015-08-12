#!/usr/bin/env python3
__author__ = 'uwe'

import re

def getProcDateStrings(procDate):
    retValue = []
    year = procDate[:4]     # 0
    retValue.append(year)
    month = procDate[4:6]   # 1
    retValue.append(month)
    day = procDate[6:]      # 2
    retValue.append(day)
    l3_dateString = year + '-' + month + '-' + day  # 3
    retValue.append(l3_dateString)
    l3_dateRange = l3_dateString + '_' + l3_dateString  # 4
    retValue.append(l3_dateRange)
    return retValue

def getProductDateString(productName):
    return re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', productName)[0]