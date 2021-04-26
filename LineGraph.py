import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Input
app=dash.Dash(__name__)
df=pd.read_csv("owid-covid-data(1).csv")

#App Layout

app.layout=html.Div([
    html.H1("Progression of Covid"),
    dcc.Dropdown(id="my_option",
                 options=[{'label':i,'value':i}
                          for i in df["location"].unique()],
                 value="Afghanistan"

                 ),
    html.Br(),
    html.Div(id="deathno",title="Deaths",draggable="true"),
    dcc.Graph(id="linegraph",figure={}),
    dcc.Graph(id="linegraph2",figure={})

])

#call back

@app.callback(
    [Output(component_id="deathno",component_property="children"),
     Output(component_id="linegraph",component_property="figure"),
     Output(component_id="linegraph2",component_property="figure")],
    Input(component_id="my_option",component_property="value")
)


def update_graph(option_slctd):
    filterdata=df[df["location"]==option_slctd]
    deaths=int(filterdata["new_deaths"].sum())
    fig=px.line(filterdata,x="date",y="total_cases")
    fig2=px.line(filterdata,x="date",y="new_cases",title="New Cases With Date")
    return "Deaths="+str(deaths),fig,fig2

if __name__ == '__main__':
    app.run_server(debug=True)