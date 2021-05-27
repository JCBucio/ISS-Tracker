import json
import urllib.request
import time
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# http://open-notify.org/Open-Notify-API/
url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print('\nPEOPLE IN SPACE: ', result['number'])

people = result['people']

for p in people:
  print(p['name'], ' in ', p['craft'])

print('\n')

url_position = 'http://api.open-notify.org/iss-now.json'
response_position = urllib.request.urlopen(url_position)
result_position = json.loads(response_position.read())

location = result_position['iss_position']
lat = float(location['latitude'])
lon = float(location['longitude'])
print('#### ACTUAL POSITION ####')
print('Latitude: ', lat)
print('Longitude: ', lon, '\n')

df = pd.read_json(url_position)
df['latitude'] = df.loc['latitude', 'iss_position']
df['longitude'] = df.loc['longitude', 'iss_position']
df.reset_index(inplace=True)
df = df.drop(['index', 'message'], axis=1)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.scatter_geo(df, lat='latitude', lon='longitude')

app.layout = html.Div(children=[
    html.H1(children='ISS Tracker', style={'textAlign': 'center'}),

    html.Div(children='''
    Script que nos da la ubicación exacta de la ISS al momento de correr el programa
    ''', style={'textAlign': 'center'}),

    dcc.Graph(
        id='iss-position-map',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
