import csv

with open("data.csv","w") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","mobile","email"])
    writer.writerow(["mohan","789541362","abc@gmail.com"])

with open("data.csv","r") as file:
    writer=csv.reader(file)
    for i in writer:
        print(i)