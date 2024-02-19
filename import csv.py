import csv
with open('C:\\Users\\dolbnya\\Desktop\\test\\weekly schedule_1.csv', newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['delivery_date'])