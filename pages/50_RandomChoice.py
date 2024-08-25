import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap
import random

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
    fig, ax = plt.subplots()
    ax.matshow(grid, cmap=cmap)
    
    # Add grid lines and remove ticks
    ax.set_xticks(np.arange(-0.5, 4, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, 4, 1), minor=True)
    ax.grid(which='minor', color='gray', linestyle='-', linewidth=2)
    ax.tick_params(left=False, bottom=False, labelleft=False, labelbottom=False)
    
    return fig

# Function to generate a random number between 0 and 1111111111111111
def generate_number():
    random_number = random.randint(0, 1111111111111111)  # Generate a random number between 0 and 1111111111111111
    random_number_str = str(random_number)
    if len(random_number_str) < 16:
        random_number_str = random_number_str.zfill(16)  # Pad with zeros to ensure 16 digits
    return modify_number(random_number_str)

st.title("4x4 Boolean Grid")

# Button to generate the boolean string
if st.button("Generate Random Boolean String"):
    boolean_string = generate_number()
    st.write(f"Generated Boolean String: {boolean_string}")
    
    # Display the grid
    fig = create_grid(boolean_string)
    if fig:
        st.pyplot(fig)
