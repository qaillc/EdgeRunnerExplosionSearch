import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Function to modify the generated number according to the rules
def modify_number(number):
    modified_number = ''
    for digit in number:
        if digit not in '01':  # Change any digit that is not 0 or 1 to 1
            modified_number += '1'
        else:
            modified_number += digit
    return modified_number

# Function to create the grid based on the boolean string
def create_grid(boolean_string):
    if len(boolean_string) != 16:
        st.error("The generated string is not 16 digits long.")
        return None
    
    # Convert string to a list of integers
    grid = np.array([int(bit) for bit in boolean_string]).reshape(4, 4)
    
    # Create a colormap for the grid
    cmap = ListedColormap(['white', 'black'])
    
    # Plot the grid
    fig, ax = plt.subplots(figsize=(2, 2))  # Shrink the graph size
    ax.matshow(grid, cmap=cmap)
    
    # Add grid lines and remove ticks
    ax.set_xticks(np.arange(-0.5, 4, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 4, 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=2)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    
    return fig

# Function to interpolate between start and end values
def interpolate_value(start_value, end_value, position, max_position):
    difference = end_value - start_value
    interpolated_value = start_value + (difference * (position / max_position))

    interpolated_value_int = int(interpolated_value)
    binary_representation = bin(interpolated_value_int)[2:].zfill(16)
    
    return binary_representation

st.title("Star Search")

# Slider for selecting the start value
start_value = st.slider("Start Value", 0, 65535, 32768)

# Slider for selecting the position, starting at 0
max_slider_value = 256
position = st.slider("Radial Out", 0, max_slider_value, 0)

# Define the distinct end values for each of the four numbers
end_values = [0, 65280, 65534, 255]

# Interpolate each value based on the slider position
interpolated_values = [
    interpolate_value(start_value, end_values[0], position, max_slider_value),  # Number 1
    interpolate_value(start_value, end_values[1], position, max_slider_value),  # Number 2
    interpolate_value(start_value, end_values[2], position, max_slider_value),  # Number 3
    interpolate_value(start_value, end_values[3], position, max_slider_value)   # Number 4
]

# Display the interpolated boolean strings
st.write("Interpolated Boolean Strings:")
for i, boolean_string in enumerate(interpolated_values):
    st.write(f"Number {i+1}: {boolean_string}")

# Create grids for each number and display them in a row
cols = st.columns(4)
for i, boolean_string in enumerate(interpolated_values):
    with cols[i]:
        st.write(f"Grid for Number {i+1}:")
        fig = create_grid(boolean_string)
        if fig:
            st.pyplot(fig)
