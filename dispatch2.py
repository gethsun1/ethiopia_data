import pandas as pd
import folium
from folium.plugins import MarkerCluster 



mt = 'KENYA Map Showing Location of Dispatches'
title_html = '''
             <h3 align="center" style="font-size:26px"><b>{}</b></h3>
             '''.format(mt) 



googleSheetId = '1VvjjDgCN-faEgG0BGh8X54HHElu7l6ZHo8zJ6jAts_M'

workSheetName = 'sheet3'

url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId, 
    workSheetName
)

df = pd.read_csv(url)


d_map = folium.Map(location=[0.0236,37.9062], max_zoom=7,zoom_start=6)

# mc = MarkerCluster().add_to(d_map)

for (index,row) in df.iterrows():
    folium.CircleMarker(radius=[row['Total']], location=[row['Lat'], row['Long']],   
            color='#000000', fill=True, fill_color='#3186cc',popup=[row['Destination']],
            tooltip='<strong>Click for more information..</strong>').add_to(d_map)

d_map.get_root().html.add_child(folium.Element(title_html))

d_map.save('dispatch_map.html')
