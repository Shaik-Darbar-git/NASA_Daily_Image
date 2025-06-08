import requests
import streamlit as st

st.title("Get a Daily Image from NASA")

Api_key = "FHVHGGEP6yOF3stTOjdnApSyjzB60Oqum65r1lHG"
url = f"https://api.nasa.gov/planetary/apod?api_key={Api_key}"

request = requests.get(url)
data = request.json()

title = data["title"]
image_url = data["url"]
description = data["explanation"]

image_filepath = "img.png"
response = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response.content)

if st.button("Fetch Image"):
    st.subheader(title)
    st.image(image_filepath)
    st.subheader("Description")
    st.write(description)

