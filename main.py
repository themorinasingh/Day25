# with open("weather_data.csv", "r") as weather_data_file:
#     weather_data = weather_data_file.readlines()

#importing csv module to read csv file
import csv

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)

    temperatures = []

    for info in data:

    #angela wants only the numerical data to be sent in to temp, so we slice the list
        if info[1] != "temp":
            temperature = int(info[1])
            temperatures.append(temperature)

print(temperatures)