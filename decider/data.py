import pandas
import typing


def add_attributes(
    df: pandas.DataFrame,
    functions: list[typing.Callable[[pandas.Series], pandas.Series]],
):
    return df.apply(functions, axis=1)


def remove_attributes(
    df: pandas.DataFrame,
    names: list[str],
):
    return df.drop(columns=names)


def preprocess(
    df: pandas.DataFrame,
    functions: list[typing.Callable[[pandas.Series], pandas.Series]] = [],
    names: list[str] = [],
) -> pandas.DataFrame:
    return remove_attributes(add_attributes(df, functions), names)
