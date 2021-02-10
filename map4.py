import folium
from folium.plugins import MarkerCluster 
import pandas as pd

mt = 'Ethiopia Map Showing Manuscripts Century of Location'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(mt) 

googleSheetId = '15LtAukjlmXovxdvoAcPDQgalJmv6ZT7aYjmq8E5ilD0'

workSheetName = 'cent_df'

url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId, 
    workSheetName
)

df = pd.read_csv(url)



e_map = folium.Map(location=[9.1450,40.4897], max_zoom=7,zoom_start=6)

#mc = MarkerCluster().add_to(e_map)
 
clr = 'Red'  

for (index,row) in df.iterrows():
      if row.loc['Century'] == 17:
            clr='#ff0000'
      elif row.loc['Century'] == 18:
            clr ='#00ff00'
      elif row.loc['Century'] == 19:
            clr ='#0000ff'
      elif row['Century'] == 20:
            clr = '#3186cc'

for (index,row) in df.iterrows():
    folium.CircleMarker(location=[row.loc['Latitude'], row.loc['Longitude']],
                 radius=10,popup=row.loc['Century'],color='#000000', fill=True, fill_color=clr,
                 tooltip=row.loc['Century']).add_to(e_map)
  
e_map.get_root().html.add_child(folium.Element(title_html))

e_map.save('ethiopia_map4.html')
