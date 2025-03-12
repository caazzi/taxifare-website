import streamlit as st
import pandas as pd
import requests
import datetime
import folium
from streamlit_folium import folium_static, st_folium

'''
# How much will your taxi cost?
'''

st.markdown('''
I will need some information to estimate how much your ride will cost.
''')

'''
## Please inform the following:
'''

d = st.date_input("1. When?", datetime.datetime(2025,3,12))

import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

st.write("Click on the map to select the initial and final points:")

# Manhattan coordinates (centered roughly on Midtown)
manhattan_lat = 40.7831
manhattan_lng = -73.9712

# Initialize session state to store points if not already initialized
if 'points' not in st.session_state:
    st.session_state.points = []
if 'reset_clicked' not in st.session_state:
    st.session_state.reset_clicked = False

# Function to handle reset button
def reset_points():
    st.session_state.points = []
    st.session_state.reset_clicked = True

# Create a folium map centered on Manhattan
m = folium.Map(location=[manhattan_lat, manhattan_lng], zoom_start=13)


# Display the map and get the clicked point
map_data = st_folium(m, width=700, height=500, key=f"map_{len(st.session_state.points)}")

# Process clicked points
if map_data is not None and "last_clicked" in map_data and not st.session_state.reset_clicked:
    lat = map_data["last_clicked"]["lat"]
    lng = map_data["last_clicked"]["lng"]

    # Limit to two points
    if len(st.session_state.points) < 2:
        st.session_state.points.append((lat, lng))
        st.rerun()  # st.rerun() replaces st.experimental_rerun() in newer versions

# Reset flag after rerun
if st.session_state.reset_clicked:
    st.session_state.reset_clicked = False

# Display selected points
if st.session_state.points:
    st.write("### Selected Points")
    for i, (lat, lng) in enumerate(st.session_state.points, 1):
        st.write(f"Point {i}: Latitude {lat:.6f}, Longitude {lng:.6f}")

    # Create a DataFrame with the selected points for visualization
    df = pd.DataFrame({
        'lat': [point[0] for point in st.session_state.points],
        'lon': [point[1] for point in st.session_state.points]
    })

    # Show points on a Streamlit native map
    st.map(df)

    # If two points are selected, calculate distance and show a line between them
    if len(st.session_state.points) == 2:
        st.write("### Two points selected!")

        # Create a map showing the line between points
        line_map = folium.Map(location=[manhattan_lat, manhattan_lng], zoom_start=13)

        # Add markers for the two points
        for i, (lat, lng) in enumerate(st.session_state.points, 1):
            folium.Marker(
                [lat, lng],
                popup=f"Point {i}",
                tooltip=f"Point {i}"
            ).add_to(line_map)

        # Add a line connecting the two points
        folium.PolyLine(
            st.session_state.points,
            color="red",
            weight=2.5,
            opacity=1
        ).add_to(line_map)

        # Display the map with the line
        st_folium(line_map, width=700, height=500, key="line_map")

        # Add buttons for actions with the two points
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Use These Points"):
                st.success("Points confirmed! You can now use these coordinates in your application.")
                # Here you could add code to process the selected points

        with col2:
            if st.button("Reset Selection", on_click=reset_points):
                pass  # The reset function will be called via on_click

numb_passagers = st.slider("4. How many passangers?", 1, 4, 1)

'''
## Thanks! Your predicted fare is:
'''
