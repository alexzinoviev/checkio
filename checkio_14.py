import datetime

def days_diff(date1, date2):
    date_1 = datetime.date(int(date1[0]), int(date1[1]), int(date1[2]))
    date_2 = datetime.date(int(date2[0]), int(date2[1]), int(date2[2]))
    difference = date_2 - date_1
    difference_str = str(difference)
    if difference_str == '0:00:00':
        return 0
    else:
        diff_days = int(difference_str.split()[0])
        if diff_days < 0:
            diff_days = diff_days * (-1)
        return diff_days


print(days_diff((1982, 4, 19), (1982, 4, 25)))# == 3
#print(days_diff((2014, 1, 1), (2014, 8, 27)))# == 238
#print(days_diff((2014, 8, 27), (2014, 1, 1)))# == 238