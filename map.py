import folium
from folium.plugins import MarkerCluster 
import pandas as pd
# import io
# from PIL import Image


mt = 'Ethiopia Map Showing Location of Manuscripts II'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(mt) 


googleSheetId = '1Yjk75jFIOdj0GXBjS_ok7CV96KlB8EKOWFuL9dwV1E4'

workSheetName = 'Known_coordinates'

url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId, 
    workSheetName
)

df = pd.read_csv(url)


#df = df.head(10)
#print(df)

e_map = folium.Map(location=[9.1450,40.4897], max_zoom=7,zoom_start=6)

mc = MarkerCluster().add_to(e_map)

for (index,row) in df.iterrows():
    folium.Marker(location=[row.loc['Latitude'], row.loc['Longitude']],
                 popup=row.loc['Place'],tooltip='<strong>Click for more information..</strong>').add_to(mc)
  
e_map.get_root().html.add_child(folium.Element(title_html))

e_map.save('ethiopia_map.html')

# img_data = e_map._to_png(5)
# img = Image.open(io.BytesIO(img_data))
# img.save('data/ethiopia_map.png')



