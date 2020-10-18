#Dynamic popup color
import folium
import pandas
df=pandas.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])
map = folium.Map([38.58,-99.09], zoom_start = 6, tiles ="Stamen Terrain")

def color_range(elev):
    if elev>=4000:
        return 'white'
    elif elev>=3000:
        return 'orange'
    elif elev>=2000:
        return 'pink'
    elif elev>=1500:
        return 'green'
    elif elev >= 1000:
        return 'blue'
    elif elev >=500:
        return 'lightgray'
    else:
        return 'gray'

fg= folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat,lon, elev):# when itering with two lists at the same time, use zip as indicated.
    fg.add_child(folium.CircleMarker(location = [lt,ln], radius = 6, popup = str(el)+" m", tooltip = 'Hi there!',
    fill_color=color_range(el), color='grey',fill = True, fill_opacity=0.6))

fg.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000<= x['properties']['POP2005'] < 20000000 else 'red'}))
map.add_child(fg)
map.save("Map1.html")
