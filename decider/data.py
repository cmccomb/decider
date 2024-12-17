import pandas
import typing


def extend_dataframe(
    df: pandas.DataFrame,
    functions: list[typing.Callable[[pandas.Series], pandas.Series]],
):
    for function in functions:
        df.apply(function, axis=1)

    return df
