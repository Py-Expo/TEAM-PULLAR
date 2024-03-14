import os
import requests
import streamlit as st

API_TOKEN = "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"
API_URL = "https://api-inference.huggingface.co/models/Kaludi/Food-Classification"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

# Streamlit UI code
st.title('Food Classification App')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Process image and display results
if uploaded_file:
    st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
    
    # Save uploaded file to a temporary location
    temp_location = os.path.join(uploaded_file.name)
    with open(temp_location, "wb") as f:
        f.write(uploaded_file.getvalue())

    output = query(temp_location)
    # st.write("Prediction:", output)

    # Extract label with highest score
    max_score_label = max(output, key=lambda x: x['score'])['label']
    st.write("The food recognized is :", max_score_label)

    # Remove temporary file
    os.remove(temp_location)
