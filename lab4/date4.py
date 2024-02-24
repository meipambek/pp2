import datetime
def date_difference_in_seconds(date1, date2):
    difference = abs(date2 - date1)
    difference_seconds = difference.total_seconds()
    return int(difference_seconds)

y = datetime.datetime.strptime("11 September 2011, 08:46:00", "%d %B %Y, %H:%M:%S")  #specified time
x = datetime.datetime.today().replace(microsecond = 0)  #curent time
print((x - y))
print(date_difference_in_seconds(x, y), "seconds")
