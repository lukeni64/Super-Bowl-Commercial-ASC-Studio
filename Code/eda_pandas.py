import pandas as pd

#remove the limit on maximum displayed columns
pd.set_option('display.max_columns', None)

#read in dataset
data = pd.read_csv("./Data/superbowl_commercials.csv")

#prints the number of ads in dataset for each brand
print(data['Brand'].value_counts())

#prints the number of ads in dataset for each year
print(data['Year'].value_counts())

#put cost and viewer columns in correct units
data['Estimated Cost'] = data['Estimated Cost'] * 1000000
data['TV Viewers'] = data['TV Viewers'] * 1000000

#displays first five rows of dataframe
print(data.head())