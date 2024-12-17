"""
This module contains the Gradio interface for the PSH dataset.
"""

import gradio

import pandas
from .ranking import sort_data


# Define Gradio interface
def gui(data: pandas.DataFrame) -> gradio.Interface:
    """
    Create a Gradio interface for the PSH dataset.
    :return: The Gradio interface.
    :rtype: gradio.Interface
    """
    weights = []
    min_cutoffs = []  # List to store minimum cutoff sliders
    max_cutoffs = []  # List to store maximum cutoff sliders

    with gradio.Blocks() as demo:
        for field in data.columns:
            with gradio.Row():
                # Get min/max values for the field
                min_val = data[field].min()
                max_val = data[field].max()

                # Create sliders for min and max cutoffs
                min_cutoff = gradio.Slider(
                    minimum=min_val,
                    maximum=max_val,
                    label=f"{field} Min Cutoff",
                    step=1,
                )
                min_cutoffs.append(min_cutoff)

                max_cutoff = gradio.Slider(
                    minimum=min_val,
                    maximum=max_val,
                    label=f"{field} Max Cutoff",
                    step=1,
                    value=max_val,
                )  # Set initial value to max
                max_cutoffs.append(max_cutoff)

                weight = gradio.Number(label=f"{field} Weight", value=1)
                weights.append(weight)

        output = gradio.DataFrame(label="Sorted Data")

        # Update change events
        for elem in min_cutoffs + max_cutoffs + weights:
            elem.change(
                lambda *x: sort_data(data, *x),
                inputs=weights + min_cutoffs + max_cutoffs,
                outputs=output,
            )

        demo.load(
            lambda *x: sort_data(data, *x),
            inputs=weights + min_cutoffs + max_cutoffs,
            outputs=output,
        )

    return demo
