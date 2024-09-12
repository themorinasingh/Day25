import pandas

data = pandas.read_csv("./weather_data.csv")

#converting the data in to different data types
data_dict = data.to_dict()
# print(data_dict)

temperature_data_list = data["temp"].to_list()
#print(temperature_data_list)

#calculating temperature average using basic methods
average_temp = round(sum(temperature_data_list) / len(temperature_data_list), 2)
#print(average_temp)

#calculating average temp with pandas
average_temperature = data['temp'].mean()
#print(average_temperature)

#finding the maximum temp sing pandas
max_temp = data['temp'].max()
#print(data[data.temp == 15])

#angela's challenger, accessing row with highest temp
row_wth_max_temp = data[data.temp == max_temp]
#print(row_wth_max_temp)

#let us access monday and store a row init
monday = data[data.day == "Monday"]
mondays_temp = monday.temp
mondays_temp_f = mondays_temp * 9 /5 + 32

print(mondays_temp_f)