import pandas as pd
import plotly.express as px
import flet as ft
from flet.plotly_chart import PlotlyChart

def main(page: ft.Page):

    # Load the gapminder dataset
    df = px.data.gapminder()

    # Filter data for Turkey and Canada
    df_turkey_canada = df[df['country'].isin(['Turkey', 'Canada'])]

    # Create bar chart comparing populations of Turkey and Canada over the years
    fig = px.bar(
        df_turkey_canada,
        x="year",
        y="pop",
        color="country",
        labels={"pop": "Population"},
        title="Population Comparison: Turkey vs Canada",
        height=400,
    )

    # Add the Plotly chart to the page
    page.add(PlotlyChart(fig, expand=True))

# Start the Flask web application
ft.app(target=main)
