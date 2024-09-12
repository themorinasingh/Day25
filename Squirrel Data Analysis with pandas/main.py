import pandas

squirrel_data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240911.csv")

#TODO Create a dataframe containing fur color and number of quirells corrosponding to that color

#singliing out furcolor and creating a series
fur_colors = squirrel_data["Primary Fur Color"]
#using vLUE COUNTS TO CALCULAT values of given type of color an storing them in their respective colors
values = fur_colors.value_counts()
red = values["Cinnamon"]
gray = values["Gray"]
black = values["Black"]

#saving values in a dictionary
color_dict = {"Colour": ["Red", "Gray", "Black"], "Numbers In Park":[392,2473,103]}

#TODO creating the data frame with the values requested
challenge_dataframe = pandas.DataFrame(color_dict)
#printing requested data frame
print(challenge_dataframe)