import csv
import pandas

# data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data.temp)
#

# Conver to dictionary
# data_dict = data.to_dict()
# print(data_dict)

# Convert column values to list
# print(data['temp'].tolist())

# Print Average of temp column
# print(data['temp'].mean())

# Print max of all in temp column
# print(data['temp'].max())

# Get Data from matching row and convert from celsius to farhenheit
# monday = data[data.day == 'Monday']
# temp_c = monday.temp[0]
#
# temp_f = (temp_c * 9/5) + 32
# print(temp_f)
# print(data[data.temp == data['temp'].max()])

# Create a dataframe
# data_dict = {
#     'students': ['John', 'Brad', 'Patty', 'Roger'],
#     'scores': [ 90, 10, 100, 90 ]
# }
#
# data = pandas.DataFrame(data_dict)
# print(type(data))
# data.to_csv('new_data.csv')

data = pandas.read_csv('Squirrel_Data.csv')
print(data['Primary Fur Color'])

black_count = len(data[data['Primary Fur Color'] == 'Black'])
grey_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])

squirrel_dict = {
    'Fur Color': ['grey', 'red', 'black'],
    'Count': [grey_count, red_count, black_count]
}

squirrel_data = pandas.DataFrame(squirrel_dict)
squirrel_data.to_csv('Squirrel_Count.csv')
