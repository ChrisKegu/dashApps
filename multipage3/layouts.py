import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px


import pandas as pd

df = pd.read_csv('oil2.csv')

oilLayout = html.Div(children=[dbc.Row([dbc.Col(html.Div([
html.Div(children='''Oil Prediction'''),
html.H1('Oil Volume Prediction', style={'textAlign':'center','fontSize':'200%','color':'red','letterSpacing':'3px'}),
html.H4('Year',style={'letterSpacing':'3px'}),
dcc.Input(id='Year', value='2019', type='number',placeholder='Please Enter Year',style={'float':'center'}),
html.Br(),
html.H4('Month',style={'letterSpacing':'3px'}),
dcc.Input(id='Month',placeholder='Please Enter Month', value='1', type='number',min=1,max=12),
html.Br(),
html.H4('Day',style={'letterSpacing':'3px'}),
dcc.Input(id='Day',placeholder='Please Enter Day', value='1', type='number',min=1,max=30),
html.Br(),
html.Br(),
#html.Button('Predict',id='btnPredict',style={'background-color':'cyan','color':'black','text-decoration':'none','border':'none','padding':'10px 20px','text-align':'center','border-radius':'16px'}),
#dbc.Button('Predict',id='btnPredict',className="btn btn-primary"),
dbc.Button('Predict',id='btnPredict',color="success", className="mr-1"),



html.Br(),
html.Br(),
html.H1(id='output',style={'color':'blue'}),html.P('m3/day')   ] )) ])    ],style={'textAlign':'center' ,'background-image':'url("/assets/a.jpg")','background-size':'100% 1000px','background-repeat':'no-repeat','height':'970px','width':'100%'})









oil1Layout = html.Div([
dcc.Dropdown(
id='my-dropdown',
options=[
{'label': i, 'value': i} for i in df['MonthYear'].unique()
],
value='1',
searchable=True,multi=False,placeholder='Choose Month...',style={'margin-left':'2%','width':'97%'})

,html.Div(id='output-container'),html.H2("",style={'margin-left':'2%','background-image':'url("/assets/d.jpg")','height':'450px','width':'100%'})
],style={'backgroundColor':'black','height':'500px'})

dcc.Input(id='input', value='', type='text')



oil11Layout = html.Div([
dcc.Dropdown(
id='my-dropdown',
options=[
{'label': i, 'value': i} for i in df['Year'].unique()
],
value='2020',
searchable=True,placeholder='Choose Year...',style={'margin-left':'2%','width':'97%'})

,html.Div(id='output-container4'),html.H2("",style={'margin-right':'90px','background-image':'url("/assets/l.jpg")','height':'100%','width':'100%','background-size':'750px 500px','background-position':'0px 0px'})
],style={'margin-right':'0%','backgroundColor':'maroon','height':'500px'})

dcc.Input(id='input', value='', type='text')








#-----------------------------------------------------------------------------------------------
oil2Layout = html.Div([
dcc.Dropdown(
id='my-dropdown',
options=[
{'label': i, 'value': i} for i in df['MonthYear'].unique()
],
value='1',
searchable=True,placeholder='Choose Month...',style={'margin-left':'2%','width':'97%'}),
html.Div(id='output-container2'),html.H2("",style={'margin-left':'2%','background-image':'url("/assets/i.jpg")','height':'100%','width':'100%','background-size':'1500px 500px'})
],style={'margin-left':'0%','backgroundColor':'maroon','height':'500px'})

dcc.Input(id='input', value='', type='text')



oil22Layout = html.Div([
dcc.Dropdown(
id='my-dropdown',
options=[
{'label': i, 'value': i} for i in df['Year'].unique()
],
value='2020',
searchable=True,placeholder='Choose Year...',style={'margin-left':'2%','width':'97%'}),
html.Div(id='output-container5'),html.H2("",style={'margin-left':'2%','background-image':'url("/assets/h.jpg")','height':'100%','width':'100%','background-size':'1550px 500px'})
],style={'margin-left':'0%','backgroundColor':'black','height':'500px'})

dcc.Input(id='input', value='', type='text')




df=df.rename(columns={'Reservoir_pressure_(atm)':'Reservoir_pressure'})

fig = px.scatter(df, x="Reservoir_pressure", y="Oil_volume")


#-------------------------------------------------------------------------------------------------
oil3Layout = html.Div(children=[
    html.H1(children='',style={'margin-left':'5%'}),

    html.Div(children='''
         A scatter plot showing decrease in Oil production with time as reservoir pressure reduces.
    ''',style={'margin-left':'5%'}),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
],style={'margin-left':'0%'})

# dcc.Input(id='input', value='', type='text')


