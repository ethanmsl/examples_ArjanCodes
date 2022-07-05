from dash import Dash, dcc, html
from pandas import DataFrame
from src.components import (
    bar_chart,
    category_dropdown,
    month_dropdown,
    pie_chart,
    record_store,
    year_dropdown,
)

from . import ids


def create_layout(app: Dash, data: DataFrame) -> html.Div:
    # initialize the record store
    record_store.initialize(app, data)

    # create the layout
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, data),
                    month_dropdown.render(app, data),
                    category_dropdown.render(app, data),
                ],
            ),
            bar_chart.render(app),
            pie_chart.render(app),
            dcc.Store(id=ids.RECORDS),
            dcc.Store(id=ids.YEAR_BUTTON_CLICKS, data=0),
            dcc.Store(id=ids.MONTH_BUTTON_CLICKS, data=0),
            dcc.Store(id=ids.CATEGORY_BUTTON_CLICKS, data=0),
        ],
    )