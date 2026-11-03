import polars as pl
import polars.selectors as cs

pl.Config.set_tbl_cols(-1)
#pl.Config.set_tbl_width_chars(-1)

data = pl.read_csv("./Data/superbowl_commercials.csv")

bool_cols = data.columns[4:11]

print(bool_cols)

print(data['Brand'].value_counts())
# for column in bool_cols:
#     data = (
#         data
#         .with_columns(
#             pl.when(cs.by_dtype(pl.Float64) == "TRUE")
#             .then(pl.lit(True))
#             .when(cs.by_dtype(pl.Float64) == "FALSE")
#             .then(pl.lit(False))
#             .otherwise
#             .alias(column)
#         )
#     )

# print(data.schema)
