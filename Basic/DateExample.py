# -*- coding:utf-8 -*-

import datetime

if __name__ == "__main__":
    today = datetime.date.today()
    todaydetail = datetime.datetime.today()
    print(today)
    print(todaydetail)

    print(today.year)
    print(today.month)
    print(today.day)

    print(todaydetail.hour)
    print(todaydetail.minute)
    print(todaydetail.second)
    print(todaydetail.microsecond)

    print(todaydetail.strftime("%Y/%m/%d %H:%M:%S"))
