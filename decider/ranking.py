"""
This module provides a function to sort the dataset based on weighted sum of fields.
"""

import pandas

def sort_data(data: pandas.DataFrame, *weights_and_cutoffs: float) -> pandas.DataFrame:
    """
    Loads the dataset, applies cutoffs, calculates weighted sum, and sorts the data.
    :param data:
    :type: pandas.DataFrame
    :param weights_and_cutoffs:
    :type weights_and_cutoffs: float
    :return: The sorted DataFrame.
    :rtype: pandas.DataFrame
    """

    # Copy the data for manipulation
    df = data.copy()

    # Determine sorting fields by excluding fields_to_exclude_from_sorting
    fields = df.columns

    # Get number of fields
    n_fields = len(fields)

    # Extract weights and cutoffs
    weights = weights_and_cutoffs[:n_fields]
    min_cutoffs_values = weights_and_cutoffs[n_fields : 2 * n_fields]
    max_cutoffs_values = weights_and_cutoffs[2 * n_fields :]

    # Apply cutoffs
    for field, min_cutoff, max_cutoff in zip(
        fields, min_cutoffs_values, max_cutoffs_values
    ):
        df = df[(df[field] >= min_cutoff) & (df[field] <= max_cutoff)]

    # Calculate weighted sum
    weighted_sum = sum(
        [df[field] * weight for field, weight in zip(fields, weights)]
    )

    # Sort data by weighted sum
    sorted_df = df.assign(weighted_sum=weighted_sum).sort_values(
        by=["weighted_sum"], ascending=False
    )

    return sorted_df