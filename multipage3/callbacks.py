import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app
import joblib
import dash_core_components as dcc
import plotly.express as px
import dash

from layouts import df
import pandas as pd
#df = pd.read_csv('oil2.csv')



@app.callback(
Output(component_id='output', component_property='children'),
[Input('btnPredict','n_clicks'),
State(component_id='Year', component_property='value'),
State('Month', 'value'),
State('Day', 'value')]
)

def update_graph(n_clicks,Year,Month,Day):
    model=joblib.load('my_oil_model.joblib')
    oilVolumePrediction=model.predict([[Year,Month,Day]])

    return oilVolumePrediction 






@app.callback(
Output(component_id='output-container', component_property='children'),
[Input(component_id='my-dropdown', component_property='value'),
Input('my-dropdown', 'value')
]
)

    
def update_graph(myTxt, month): 
    oilDf=df[df['MonthYear']== month]
   
    perday=oilDf.groupby(['Day'])['Oil_volume'].sum().reset_index()
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': perday.Day, 'y': perday.Oil_volume,'showlegend':True ,'type':'line', 'name':month,'line':dict(color='green')}
            ],
        
            'layout':{
                'title': "Oil data for "+month+'.','xaxis':{'title':'Day'},'yaxis':{'title':'Oil volume (m3/day)','range':[0,50],'showlegend':True}
            }
        }   
    )






@app.callback(
Output(component_id='output-container4', component_property='children'),
[Input(component_id='my-dropdown', component_property='value'),
Input('my-dropdown', 'value')
]
)

def update_graph(myTxt, year): 
    oilDf2=df[df['Year']== year]
  
    permonth=oilDf2.groupby(['Month'])['Oil_volume'].sum().reset_index()
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': permonth.Month, 'y': permonth.Oil_volume,'showlegend':True ,'type':'line','line':dict(color='green') , 'name':year,'marker':{'color':['red','blue','red','blue','red','blue','red','blue','red','blue','red','blue']}}
            ],
            'layout':{
                'title': "Oil data for "+str(year)+'.','xaxis':{'title':'Month'},'yaxis':{'title':'Oil volume (m3/day)'}
            }
        }
    )









#-----------------------------------------------------------------------------------------
@app.callback(
Output(component_id='output-container2', component_property='children'),
[Input(component_id='my-dropdown', component_property='value'),
Input('my-dropdown', 'value')]
)


def update_graph(myTxt, month): 
    oilDf=df[df['MonthYear']== month]
   
    perday=oilDf.groupby(['Day'])['Oil_volume'].sum().reset_index()
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': perday.Day, 'y': perday.Oil_volume,'type':'bar', 'showlegend':True,'name':month,'bar':dict(color='green'),'marker':{'color':['maroon','yellow','green','blue','indigo','violet','maroon','yellow','green','blue','indigo','violet','maroon','yellow','green','blue','indigo','violet','maroon','yellow','green','blue','indigo','violet','maroon','yellow','green','blue','indigo','violet']}}
            ],
            'layout':{
                'title': "Oil data for "+month+'.','xaxis':{'title':'Day'},'yaxis':{'title':'Oil volume (m3/day)'}
            }
        }
    )






@app.callback(
Output(component_id='output-container5', component_property='children'),
[Input(component_id='my-dropdown', component_property='value'),
Input('my-dropdown', 'value')
]
)

def update_graph(myTxt, year): 
    oilDf2=df[df['Year']== year]
    permonth=oilDf2.groupby(['Month'])['Oil_volume'].sum().reset_index()
    
    return dcc.Graph(
        id='example-graph',
        figure={
            'data':[
                {'x': permonth.Month, 'y': permonth.Oil_volume,'showlegend':True,'type':'bar', 'name':year,'marker':{'color':['maroon','yellow','green','blue','indigo','violet','maroon','yellow','green','blue','indigo','violet']}}
            ],
            'layout':{
                'title': "Oil data for "+str(year)+'.','xaxis':{'title':'Month'},'yaxis':{'title':'Oil volume (m3/day)'}
            }
        }
    )










#-----------------------------------------------------------------------------------------

