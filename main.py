import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
color_data = data["Primary Fur Color"]
color_names = []
color_counts = []
for color in color_data.to_list():
    if color not in color_names and str(color) != "nan":
        color_names.append(color)

for color in color_names:
    color_counts.append(color_data.to_list().count(color))

color_dict = {"Primary Fur Color": color_names, "Count": color_counts}

df = pandas.DataFrame(color_dict)
df.to_csv("color_count.csv")
for i in range(len(color_dict["Primary Fur Color"])):
    print("Primary Fur Color: "+color_dict["Primary Fur Color"][i] + ", Count: " + str(color_dict["Count"][i]))
