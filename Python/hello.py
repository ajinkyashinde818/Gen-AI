import streamlit as st

# Add a header title
st.title("My First Streamlit App")

# Create an interactive slider widget
number = st.slider("Pick a number", 0, 100, 25)

# Display the interactive output
st.write(f"The square of {number} is {number ** 2}")
