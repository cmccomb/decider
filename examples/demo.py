import pandas
import decider


# Example Data
data = pandas.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})


# Define functions
def add_ten_to_a(series):
    series["C"] = series["A"] + 10
    return series


def multiply_a_and_b(series):
    series["D"] = series["A"] * series["B"]
    return series


# Extend DataFrame
decider.gui(decider.preprocess(data, [add_ten_to_a, multiply_a_and_b], ["A"])).launch(
    debug=True
)
