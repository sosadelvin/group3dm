import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import folium
from folium import plugins

# Menu for navigation
menu = ["Team Introduction", "Graphs Visualization", "Interactive Map"]
choice = st.sidebar.selectbox("Select a section", menu)

# 1. Team Introduction Section
if choice == "Team Introduction":
    group_members = """
    Our team consists of : 
    1.	Berliana Indah Alyanti (021202400012)
    2.	Defira Lubnaziza (021202400004)
    3.	Sosa Delvin Cindiva (021202400020)
    """
    st.title("Team Introduction")
    st.write(group_members)

# 2. Graphs Visualization Section
elif choice == "Graphs Visualization":
    st.subheader("Dynamic Graphs Visualization")

    # User input for the number of nodes and edges
    num_nodes = st.number_input("Number of nodes:", min_value=1, max_value=20, value=5)
    num_edges = st.number_input("Number of edges:", min_value=0, max_value=num_nodes*(num_nodes-1)//2, value=3)

    # Generate random graph based on input
    if num_nodes > 0 and num_edges > 0:
        G = nx.erdos_renyi_graph(num_nodes, num_edges / (num_nodes * (num_nodes - 1) / 2))  # Random graph
        
        # Directed graph
        st.subheader("Directed Graph")
        fig, ax = plt.subplots(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold', arrows=True, ax=ax)
        plt.title("Directed Graph")
        st.pyplot(fig)

        # Undirected graph
        st.subheader("Undirected Graph")
        fig, ax = plt.subplots(figsize=(8, 6))
        nx.draw(G, with_labels=True, node_color='lightgreen', node_size=2000, font_size=12, font_weight='bold', ax=ax)
        plt.title("Undirected Graph")
        st.pyplot(fig)

# 3. Interactive Map Section
elif choice == "Interactive Map":
    st.subheader("City Connections in Central Java")

    # Province selection
    province = st.selectbox("Select a province", ["Central Java", "East Java", "Yogyakarta"])

    if province == "Central Java":
        city_coordinates = {
            "Semarang": [-6.9667, 110.4194],
            "Solo": [-7.5667, 110.8231],
            "Yogyakarta": [-7.7956, 110.3695],
            "Surakarta": [-7.5667, 110.8231],  # Same as Solo, they are part of the same region
            "Magelang": [-7.4705, 110.2201],
            "Klaten": [-7.7319, 110.5891]
        }

        city_connections = [
            ("Semarang", "Solo"), 
            ("Semarang", "Yogyakarta"),
            ("Solo", "Surakarta"), 
            ("Yogyakarta", "Magelang"),
            ("Magelang", "Semarang"),
            ("Solo", "Klaten"),
            ("Surakarta", "Klaten")
        ]
        center_coords = [-7.5, 110.5]
        
    elif province == "East Java":
        city_coordinates = {
            "Surabaya": [-7.2575, 112.7521],
            "Malang": [-8.1200, 112.0400],
            "Madiun": [-7.6299, 111.5280],
            "Blitar": [-8.5566, 111.6872]
        }

        city_connections = [
            ("Surabaya", "Malang"),
            ("Malang", "Madiun"),
            ("Madiun", "Blitar"),
            ("Surabaya", "Blitar")
        ]
        center_coords = [-7.5, 112.5]
    
    elif province == "Yogyakarta":
        city_coordinates = {
            "Yogyakarta": [-7.7956, 110.3695],
            "Bantul": [-7.8770, 110.3305],
            "Sleman": [-7.7267, 110.3633]
        }

        city_connections = [
            ("Yogyakarta", "Bantul"),
            ("Yogyakarta", "Sleman"),
            ("Bantul", "Sleman")
        ]
        center_coords = [-7.75, 110.4]

    # Create a map centered around the chosen province
    province_map = folium.Map(location=center_coords, zoom_start=10)

    # Add markers for each city
    for city, coords in city_coordinates.items():
        folium.Marker(location=coords, popup=city).add_to(province_map)

    # Add connections (lines) between cities using PolyLine
    for connection in city_connections:
        city1, city2 = connection
        coords1 = city_coordinates[city1]
        coords2 = city_coordinates[city2]
        
        # Add a line (polyline) between the two cities
        folium.PolyLine(locations=[coords1, coords2], color="blue", weight=2.5, opacity=0.8).add_to(province_map)

    # Display the map
    st.markdown(f"Below is an interactive map showing the locations of various cities and their connections in {province}.")
    st.components.v1.html(province_map._repr_html_(), height=500)
