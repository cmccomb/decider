import pandas
import decider


# Example Data
data = {"A": [1, 2, 3], "B": [4, 5, 6]}
df = pandas.DataFrame(data)


# Define functions
def add_ten(series):
    series["C"] = series["A"] + 10
    return series


def multiply(series):
    series["C"] = series["A"] * series["B"]
    return series


# Extend DataFrame
decider.gui(decider.extend_dataframe(df, [add_ten, multiply])).launch(debug=True)
