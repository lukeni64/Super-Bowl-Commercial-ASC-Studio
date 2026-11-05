import polars as pl
import polars.selectors as cs

car_companies = ["Kia", "Toyota", "Hyundai"]

junk_food_companies = ["Coca-Cola", "Pepsi", "Doritos"]

#remove the limit on maximum displayed columns
pl.Config.set_tbl_cols(-1)

#read in dataset
data = pl.read_csv("./Data/superbowl_commercials.csv")

#prints the number of ads in dataset for each brand
print(data['Brand'].value_counts())

#prints the number of ads in dataset for each year
print(data['Year'].value_counts())

#put cost and viewer columns in correct units
data = data.with_columns(
    pl.col("Estimated Cost") * 1_000_000,
    pl.col("TV Viewers") * 1_000_000,
    pl.when(pl.col("Brand").str.starts_with("Bud"))
    .then(pl.lit("Alcoholic Beverages"))
    .when(pl.col("Brand").str.contains_any(car_companies))
    .then(pl.lit("Car"))
    .otherwise(pl.lit("Junk Food"))
    .alias("Industry")
)

data.write_csv("Data/cleaned_superbowl_commercials.csv")

cleaned_data = pl.read_csv("Data/cleaned_superbowl_commercials.csv")

#displays first five rows of dataframe
print(cleaned_data.head())
