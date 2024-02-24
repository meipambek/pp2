import datetime
x = datetime.datetime.now()
yesterday = x - datetime.timedelta(1)
tomorrow = x + datetime.timedelta(1)
print(yesterday.strftime("%A"), x.strftime("%A"), tomorrow.strftime("%A"))
print(yesterday)
print(x)
print(tomorrow)