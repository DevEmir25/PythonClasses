import csv

title = ["temprature", "fog" , "pressure"]
data = [[300,75.5,10] , [32.3,50,3]]

with open ('sensor_veri.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(title)
    for i in data:
        writer.writerow(i)