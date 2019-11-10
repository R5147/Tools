# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel).

# [Aim]
# Calculate day_old using two inputs (birthday, current date)
# Inputs for birthday and current date
# - birthday (year1, month1, day1)
# - current date (year2, month2, day2)
# 
# [Process analyse]
# 1. initialise varialbe day_old, year_diff, month_days1, month_days2
# 2. update month_days1 or/and month_days2 if year1 or/and year2 is/are leap year
# 3. check if year_diff == 0, if it is true, go to step 3.1., else, go to step 4
# 3.1. calculate day_old by finding the date between two months (current_year_days function is required), then, go to step 6
# 4. check if year_diff == 1, if it is true, go to step 4.1, else, go to step 5
# 4.1. calculate day_old by finding the first and last year day (year_days function is required), then, go to step 6
# 5. calculate day_old by finding the first year day, last year day and the year(s) day between first and last year (year_days function is required), then, go to step 6
# 6. return the day_old
# 
# [Code]


def is_leap_year(y):
    if y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True


def current_year_days(month1, day1, month2, day2, month_days):
    yeardays = 0
    for month in range(month1 - 1, month2 - 1):
        if month == month1 - 1:
            yeardays += month_days[month] - day1
        else:
            yeardays += month_days[month]
    if month2 - month1 == 0:
        yeardays += day2 - day1
    else:
        yeardays += day2
    return yeardays


def year_days(year, month, day, month_days, offset):
    total_year_day = 365
    yeardays = 0
    if is_leap_year(year):
        total_year_day = 366
    for month in range(month - 1):
        yeardays += month_days[month]
    yeardays += day
    # if offset is 0, it means first year, otherwise, last year
    if offset == 0:
        yeardays = total_year_day - yeardays
    return yeardays


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    day_old = 0
    year_diff = year2 - year1
    month_days1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month_days2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap_year(year1):
        month_days1[1] = 29
    if is_leap_year(year2):
        month_days2[1] = 29

    if year_diff == 0:
        day_old += current_year_days(month1, day1, month2, day2, month_days1)
    elif year_diff == 1:
        day_old += year_days(year1, month1, day1, month_days1, 0) + year_days(year2, month2, day2, month_days2, 1)
    else:
        for year in range(year1, year2 + 1):
            if year == year1:
                day_old += year_days(year1, month1, day1, month_days1, 0)
            elif year != year2:
                if is_leap_year(year):
                    day_old += 366
                else:
                    day_old += 365
            else:
                day_old += year_days(year2, month2, day2, month_days2, 1)
    return day_old


print(daysBetweenDates(2019, 11, 1, 2019, 11, 9))
print(daysBetweenDates(2012, 1, 1, 2012, 2, 28))
print(daysBetweenDates(2012, 1, 1, 2012, 3, 1))
print(daysBetweenDates(2011, 6, 30, 2012, 6, 30))
print(daysBetweenDates(2011, 1, 1, 2012, 8, 8))
print(daysBetweenDates(1900, 1, 1, 1999, 12, 31))
