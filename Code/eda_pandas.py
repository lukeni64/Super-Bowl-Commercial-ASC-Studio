import pandas as pd
import numpy as np

#remove the limit on maximum displayed columns
pd.set_option('display.max_columns', None)

#read in dataset
data = pd.read_csv("./Data/superbowl_commercials.csv")

#prints the number of ads in dataset for each brand
print(data['Brand'].value_counts())

#prints the number of ads in dataset for each year
print(data['Year'].value_counts())

car_companies = ["Kia", "Toyota", "Hyundai"]

junk_food_companies = ["Coca-Cola", "Pepsi", "Doritos"]

data = data.assign(
    **{
        "Estimated Cost": data["Estimated Cost"] * 1_000_000,
        "TV Viewers": data["TV Viewers"] * 1_000_000,
        "Industry": np.select(
            [
                data["Brand"].str.startswith("Bud"),
                data["Brand"].str.contains("|".join(car_companies), regex=True),
                data["Brand"].str.contains("|".join(junk_food_companies), regex=True),
            ],
            [
                "Alcoholic Beverages",
                "Car",
                "Junk Food",
            ],
            default="N/A",
        ),
    }
)

data.to_csv("Data/cleaned_superbowl_commercials.csv")

cleaned_data = pd.read_csv("Data/cleaned_superbowl_commercials.csv")

#displays first five rows of dataframe
print(cleaned_data.head())