import datetime
now = datetime.datetime.now()
myStr = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current datetime: {myStr}")