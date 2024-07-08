
import streamlit as st
from PIL import Image
import pickle
import numpy as np

# Load the models
@st.cache_data
def load_model(file_path):
    with open(file_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Function to preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))
    image = np.array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Title of the app
st.title("DermaGuard: AI-Driven Precision in Skin Cancer Detection")

# Upload the image
uploaded_file = st.file_uploader("Upload an image of the skin lesion", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess the image
    image = preprocess_image(image)

    # Model selection
    model_option = st.selectbox(
        'Choose a model for prediction:',
        ('DenseNet', 'ResNet')
    )

    if model_option == 'DenseNet':
        model = load_model('DenseNet.pkl')
    elif model_option == 'ResNet':
        model = load_model('ResNet.pkl')

    # Predict
    predictions = model.predict(image)
    st.write("Prediction results:")
    st.write(predictions)
