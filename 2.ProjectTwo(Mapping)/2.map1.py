#Multiple Markers
import folium

map = folium.Map([38.58,-99.09], zoom_start = 6, tiles ="Stamen Terrain")

# map.add_child(folium.Marker(location = [38.2,-99.1], popup = "Hi I'm a marker", icon= folium.Icon(color='green'))) #not prefereable
fg= folium.FeatureGroup(name="My Map")
for coordinates in [[38.2,-99.1],[39.2,-97.1]]:
    fg.add_child(folium.Marker(location = coordinates, popup = "Hi I'm a marker", icon= folium.Icon(color='green')))#Marker is a feature group.

map.add_child(fg)
map.save("Map1.html")
