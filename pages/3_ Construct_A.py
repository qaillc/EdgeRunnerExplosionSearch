import streamlit as st

st.markdown("\n\n\n")

constructA_text = """


Key solutions include:
Skip Number Methodology (Construct A): Reduces computational load by eliminating unnecessary numbers in a sequence.

These approaches result in faster calculations and reduced computational costs, particularly in AI and ML systems, where large datasets require optimized handling.



"""


st.markdown(constructA_text)




# Function to skip numbers containing the specified digit
def skipf(skip_digit, start, end):
    sequence = [i for i in range(start, end + 1) if str(skip_digit) not in str(i)]
    return sequence

# Streamlit interface
st.title("Skip Numbers Containing a Specific Digit")

# Input for the digit to skip
skip_digit = st.number_input("Enter a digit to skip (0-9):", min_value=0, max_value=9, step=1)

# Slider to select the range of numbers
start, end = st.slider("Select the range of numbers:", 0, 1000, (0, 100))

# Button to generate the sequence
if st.button("Generate Sequence"):
    result = skipf(skip_digit, start, end)
    st.write(f"Sequence excluding numbers with '{skip_digit}' in the range {start} to {end}:")
    st.write(result)


