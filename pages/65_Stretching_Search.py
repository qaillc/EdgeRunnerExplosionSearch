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
    binary_representation = bin(interpolated_value_int)[2:].zfill(16)  # Ensure it has 16 bits
    
    return int(binary_representation, 2)  # Return as an integer for grid conversion

def bool_to_grid(boolean_value):
    return modify_number(bin(boolean_value)[2:].zfill(16))

# Streamlit app
st.title("Stretching Space Search with Dual Sliders")

# Slider for selecting the position for the first interpolation
max_slider_value = 256
position1 = st.slider("Radial Out", 0, max_slider_value, 0)

# Define the start and distinct end values for each of the four numbers
start_value = 32768
end_values = [0, 65280, 65534, 255]

# Interpolate each value based on the first slider position
interpolated_values = [
    interpolate_value(start_value, end_values[0], position1, max_slider_value),  # Number 1
    interpolate_value(start_value, end_values[1], position1, max_slider_value),  # Number 2
    interpolate_value(start_value, end_values[2], position1, max_slider_value),  # Number 3
    interpolate_value(start_value, end_values[3], position1, max_slider_value)   # Number 4
]

# Second slider for selecting the interpolation between pairs
pair_selection = st.selectbox("Select Number Pair to Interpolate", [f"Number {i+1} to Number {i+2}" for i in range(3)])
pair_index = int(pair_selection.split()[1]) - 1

position2 = st.slider(f"Translate from {pair_selection}", 0, max_slider_value, 0)

# Interpolate between the selected pair of numbers
interpolated_pair_value = interpolate_value(interpolated_values[pair_index], interpolated_values[pair_index + 1], position2, max_slider_value)

# Display the interpolated numbers
st.write("Interpolated Numbers:")
for i, value in enumerate(interpolated_values):
    st.write(f"Number {i+1}: {value}")

# Convert the interpolated numbers to boolean strings
boolean_strings = [bool_to_grid(value) for value in interpolated_values]

# Create grids for each number and display them in a row
st.write("Grids for Interpolated Numbers:")
cols = st.columns(4)
for i, boolean_string in enumerate(boolean_strings):
    with cols[i]:
        st.write(f"Grid for Number {i+1}:")
        fig = create_grid(boolean_string)
        if fig:
            st.pyplot(fig)

# Plot the new grid for the interpolated pair value
st.write(f"New Grid for {pair_selection}:")
fig = create_grid(bool_to_grid(interpolated_pair_value))
if fig:
    st.pyplot(fig)
