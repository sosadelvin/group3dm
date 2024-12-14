import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import folium
from folium import plugins

# 1. Members of the Group
group_members = """
Our team consists of Berliana Indah, Defira Lubnaziza, and Sosa Delvin Cindiva.
"""
st.title("Team Introduction")
st.write(group_members)

# 2. Visualization of Directed and Undirected Graph

# Directed Graph
st.subheader("Directed Graph")
directed_graph = nx.DiGraph()
directed_graph.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4)])

# Plot directed graph
fig, ax = plt.subplots(figsize=(8, 6))
nx.draw(directed_graph, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', arrowsize=20, ax=ax)
plt.title("Directed Graph")
st.pyplot(fig)

# Undirected Graph
st.subheader("Undirected Graph")
undirected_graph = nx.Graph()
undirected_graph.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4)])

# Plot undirected graph
fig, ax = plt.subplots(figsize=(8, 6))
nx.draw(undirected_graph, with_labels=True, node_color='lightgreen', node_size=2000, font_size=12, font_weight='bold', ax=ax)
plt.title("Undirected Graph")
st.pyplot(fig)

# 3. Graph Showing Connections Among Cities in Central Java

st.subheader("City Connections in Central Java")

# Create a graph for cities in Central Java
cities_graph = nx.Graph()
cities_graph.add_edges_from([
    ("Semarang", "Solo"), 
    ("Semarang", "Yogyakarta"),
    ("Solo", "Surakarta"), 
    ("Yogyakarta", "Magelang"),
    ("Magelang", "Semarang"),
    ("Solo", "Klaten"),
    ("Surakarta", "Klaten")
])

# Visualize the cities' graph
fig, ax = plt.subplots(figsize=(10, 8))
nx.draw(cities_graph, with_labels=True, node_color='lightblue', node_size=3000, font_size=12, font_weight='bold', edge_color='orange', ax=ax)
plt.title("City Connections in Central Java")
st.pyplot(fig)

# 4. Interactive Map with City Locations and Connections

# Coordinates of the cities in Central Java
city_coordinates = {
    "Semarang": [-6.9667, 110.4194],
    "Solo": [-7.5667, 110.8231],
    "Yogyakarta": [-7.7956, 110.3695],
    "Surakarta": [-7.5667, 110.8231],  # Same as Solo, they are part of the same region
    "Magelang": [-7.4705, 110.2201],
    "Klaten": [-7.7319, 110.5891]
}

# Define the connections between cities (edges)
city_connections = [
    ("Semarang", "Solo"), 
    ("Semarang", "Yogyakarta"),
    ("Solo", "Surakarta"), 
    ("Yogyakarta", "Magelang"),
    ("Magelang", "Semarang"),
    ("Solo", "Klaten"),
    ("Surakarta", "Klaten")
]

# Create a map centered around Central Java
central_java_map = folium.Map(location=[-7.5, 110.5], zoom_start=9)

# Add markers for each city
for city, coords in city_coordinates.items():
    folium.Marker(location=coords, popup=city).add_to(central_java_map)

# Add connections (lines) between cities using PolyLine
for connection in city_connections:
    city1, city2 = connection
    coords1 = city_coordinates[city1]
    coords2 = city_coordinates[city2]
    
    # Add a line (polyline) between the two cities
    folium.PolyLine(locations=[coords1, coords2], color="blue", weight=2.5, opacity=0.8).add_to(central_java_map)

# Display the map
st.subheader("Interactive Map of City Connections in Central Java")
st.markdown("Below is an interactive map showing the locations of various cities and their connections in Central Java.")
st.components.v1.html(central_java_map._repr_html_(), height=500)
