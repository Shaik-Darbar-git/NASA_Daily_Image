import requests
import streamlit as st

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


st.title(title)
st.image(image_filepath)
st.write(description)

