import streamlit as st

# Student information
name = "Ajinkya Shinde"
college = "MIT Academy of Engineering"
branch = "CSE (Data Science)"
year = "Second Year"
skills = "Python, Java, C++, SQL, Machine Learning"

# Title
st.title("Student Profile App")

# Profile section
st.header("Student Profile")

# Personal details
st.subheader("Name")
st.write(name)

st.subheader("College")
st.write(college)

st.subheader("Branch")
st.write(branch)

st.subheader("Year")
st.write(year)

st.subheader("Skills")
st.markdown(f"**{skills}**")