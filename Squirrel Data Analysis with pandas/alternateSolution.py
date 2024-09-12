import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240911.csv")
grey_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray" ])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon" ])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black" ])

data_dict = {
    "Color": ["Grey", "Red", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

#TODO creating our desired output

print(pandas.DataFrame(data_dict))