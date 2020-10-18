#Dynamic markers
import folium
import pandas
df=pandas.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
map = folium.Map([38.58,-99.09], zoom_start = 6, tiles ="Stamen Terrain")

fg= folium.FeatureGroup(name="My Map")
for lt, ln in zip(lat,lon):# when itering two lists at the same time, use zip as indicated.
    fg.add_child(folium.Marker(location = [lt,ln], popup = "Hi I'm a marker", icon= folium.Icon(color='green')))#Marker is a feature group.

map.add_child(fg)
map.save("Map1.html")
