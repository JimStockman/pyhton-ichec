date1 = {'day': 9, 'month': 6, 'year': 2023}
date2 = {'day': 9, 'month': 16, 'year': 2023}
date3 = {'day': 9, 'month': 6, 'year': -5}
date4 = {'day': 39, 'month': 16, 'year': 2023}
date5 = {'day': 29, 'month': 2, 'year': 2023}
date6 = {'day': 31, 'month': 4, 'year': 2023}


def check_date(date):
    y = date['year']
    m = date['month']
    d = date['day'] #Retrieve value behind the 'day' key in the date dictionary

    thirty_days_months = [4, 6, 9, 11]

    # Year must be strictly higher than 0
    if y < 1:
        return False

    # Month must be between 1 and 12
    if m not in range(1, 13):
        return False

    # Day must be between 1 and 31
    if d not in range(1, 32):
        return False

    # 30 Days month check
    if m in thirty_days_months:
        if d not in range(1, 31):
            return False

    # Leap year check
    if m == 2:
        if y % 4 == 0:
            if d not in range(1, 30):
                return False

        else:  # Normal February day
            if d not in range(1, 29):
                return False

    return True

print(check_date(date1))
print(check_date(date2))
print(check_date(date3))
print(check_date(date4))
print(check_date(date5))
print(check_date(date6))
