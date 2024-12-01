import streamlit as st

st.title("My Web App")

st.header('My Coustom Header')

agree = st.checkbox("I agree with Mohit...")
if agree:
    st.write("Great!")

# Radio button for movie genre
genre = st.radio(
    "What's your favorite movie genre",
    ["Comedy", "Drama", "Documentary"]
)

if genre == "Comedy":
    st.write("You selected Comedy.")


Nu = st.number_input('enter number')
if st.button("Get Root"):
    res = Nu**2
    st.header(res)