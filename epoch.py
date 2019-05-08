from datetime import datetime

startDate = input("Start date. The correct format is YYYY-MM-DD hh:mm:ss : ")

d = datetime.strptime(startDate,'%Y-%m-%d %H:%M:%S')
convert = d.strftime("%s") 

print(convert)
