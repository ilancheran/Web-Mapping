import folium
import pandas

data=pandas.read_csv("volcanoes.txt")

lat= list(data["LAT"])
lon= list(data["LON"])
elev= list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
     return 'green'
    elif 1000 <= elevation < 3000:
     return 'blue'

    else:
     return 'darkred'

map=folium.Map(location=[9.89360,78.17643],zoom_start=10, tiles="stamen terrain")

fgv = folium.FeatureGroup(name="volcanoes")

for lt, ln, el in zip(lat,lon,elev):

    fgv.add_child(folium.CircleMarker(location=[lt,ln], radius =6, popup=str(el)+"m",
    fill_color=color_producer(el), color='grey',fill='true' ,fill_opacity=0.7 ))

fgp = folium.FeatureGroup(name="population")

fgp.add_child(folium.GeoJson(data=open('world.json' , 'r' , encoding='utf-8-sig').read() ,
style_function=lambda x:{'fillColor':'yellow' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

fgc = folium.FeatureGroup(name="HOME")

fgc.add_child(folium.Marker(location=[9.89360,78.17643] ,  popup='HOME' , color = 'Red'))

fgh = folium.FeatureGroup(name="HOME")

fgh.add_child(folium.Marker(location=[9.82807,78.25312] , radius=6 , popup='myhome' ,fill_color='blue' , color = 'grey', fill='true', fill_opacity=0.7))



map.add_child(fgv)
map.add_child(fgp)
map.add_child(fgc)
map.add_child(fgh)
map.add_child(folium.LayerControl())

map.save("Map1.html")
