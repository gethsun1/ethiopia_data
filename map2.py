import folium
import pandas as pd




googleSheetId = '1Yjk75jFIOdj0GXBjS_ok7CV96KlB8EKOWFuL9dwV1E4'

workSheetName = 'Known_coordinates'

url = 'https://docs.google.com/spreadsheets/d/{0}/gviz/tq?tqx=out:csv&sheet={1}'.format(
    googleSheetId, 
    workSheetName
)


df = pd.read_csv(url)

e_map = folium.Map(location=[9.1450,40.4897], max_zoom=7,zoom_start=6)

folium.CircleMarker(radius= 2, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=2).add_to(e_map)

folium.CircleMarker(radius= 8, location=(8.9853, 38.79112),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=8).add_to(e_map)

folium.CircleMarker(radius= 10, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=10).add_to(e_map)
folium.CircleMarker(radius= 10, location=(11.3388 , 38.77222),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=10).add_to(e_map)
folium.CircleMarker(radius= 27, location=(12.6086 ,39.73582),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=27).add_to(e_map)
folium.CircleMarker(radius= 3, location=(9.01059, 38.71711),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=3).add_to(e_map)
folium.CircleMarker(radius= 2, location=(9.01039, 38.71711),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=2).add_to(e_map)
folium.CircleMarker(radius= 6, location=(9.04673 , 38.73706),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=6).add_to(e_map)
folium.CircleMarker(radius= 4, location=(9.05327, 38.70371),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=4).add_to(e_map)
folium.CircleMarker(radius= 3, location=(9.11658, 38.71515),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=3).add_to(e_map)
folium.CircleMarker(radius= 3, location=(10.00071, 38.772),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=3).add_to(e_map)
folium.CircleMarker(radius= 3, location=(10.97215, 38.772),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=3).add_to(e_map)
folium.CircleMarker(radius= 3, location=(11.31343, 38.772),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=3).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)
folium.CircleMarker(radius= 1, location=(9.06476, 38.758),   
            color='#3186cc', fill=True, fill_color='#3186cc',
            tooltip=1).add_to(e_map)


e_map.save('ethiopia_map2.html')


