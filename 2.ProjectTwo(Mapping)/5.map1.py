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
for lt, ln, el in zip(lat,lon, elev):# when itering two lists at the same time, use zip as indicated.
    fg.add_child(folium.Marker(location = [lt,ln], popup = str(el)+" m", icon= folium.Icon(color=color_range(el))))#Marker is a feature group.


map.add_child(fg)
map.save("Map1.html")
