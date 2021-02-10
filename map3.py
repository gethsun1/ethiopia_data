import folium
from folium.plugins import MarkerCluster 
import pandas as pd




mt = 'Ethiopia Map Showing Location of Manuscripts II'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(mt) 


googleSheetId = '1s4ltAOL0s_qpM6NZLPQdeXbJHZYH_U352lSYEpHDx8k'

workSheetName = 'lat_long_man'

url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId, 
    workSheetName
)

df = pd.read_csv(url)

df.dropna(axis='columns', how='all', inplace=True)




e_map = folium.Map(location=[9.1450,40.4897], max_zoom=7,zoom_start=6)

#mc = MarkerCluster().add_to(e_map)


for (index,row) in df.iterrows():
    folium.CircleMarker(radius=[row['Manuscripts']*2], location=[row['Latitude'], row['Longitude']],   
            color='#000000', fill=True, fill_color='#3186cc',popup=[row['Manuscripts']],
            tooltip='<strong>Click for more information..</strong>').add_to(e_map)

  
#e_map.get_root().html.add_child(folium.Element(title_html))

e_map.save('ethiopia_map3.html')