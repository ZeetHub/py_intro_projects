#Dynamic popus
import folium
import pandas
df=pandas.read_csv("Volcanoes.txt")
lat = list(df["LAT"])
lon = list(df["LON"])
elev = list(df["ELEV"])
map = folium.Map([38.58,-99.09], zoom_start = 6, tiles ="Stamen Terrain")

fg= folium.FeatureGroup(name="My Map")
for lt, ln, el in zip(lat,lon, elev):# when itering two lists at the same time, use zip as indicated.
    fg.add_child(folium.Marker(location = [lt,ln], popup = str(el)+" m", icon= folium.Icon(color='green')))#Marker is a feature group.
    #popup = folium.popup(str(el), parse_html=True).... If there are quotes in the strings....other wise blank web page screen appears.

map.add_child(fg)
map.save("Map1.html")
