import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

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