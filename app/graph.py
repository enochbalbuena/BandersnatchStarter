from altair import Chart, Tooltip
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    text_color = '#bbbbbb'

    graph = Chart(
        df,
        title=f"{y} by {x} for {target}",
    ).mark_circle(size=80).encode(
        x=x,
        y=y,
        color=target,
        tooltip=Tooltip(df.columns.to_list())
    ).properties(
        width=600,
        height=500,
        background='#1e1e1e',
        padding={"left": 20, "top": 20, "right": 20, "bottom": 20}
    ).configure_axis(
        labelColor=text_color,
        titleColor=text_color,
        gridColor='#444444',
        gridDash=[1, 4],
        gridWidth=0.5
    ).configure_title(
        color=text_color,
        fontSize=24,
        fontWeight='bold',
        anchor='middle',
        offset=20
    ).configure_legend(
        labelColor=text_color,
        titleColor=text_color,
        labelFontSize=14,
        titleFontSize=16,
        padding=10
    ).configure_view(
        strokeWidth=0
    )
    return graph
