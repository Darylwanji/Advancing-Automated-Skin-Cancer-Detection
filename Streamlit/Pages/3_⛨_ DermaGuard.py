
import streamlit as st
from PIL import Image
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np

labels_dict = {
    0: "Pigmented Bowen's Disease",
    1: "Basal Cell Carcinoma",
    2: "Benign Keratosis",
    3: "Dermatofibroma",
    4: "Melanoma",
    5: "Melanocytic Nevus",
    6: "Vascular Lesion"
}
# Load the models
@st.cache_data
def load_model(file_path):
    model = tf.keras.models.load_model(file_path)
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
        ('ResNet','DenseNet')
    )

    if model_option == 'ResNet':
        model = load_model('/Users/darylwanji/Desktop/Computer_Vision_Capstone_Project/ResNet.h5')
    elif model_option == 'DenseNet':
        model = load_model('/Users/darylwanji/Desktop/Computer_Vision_Capstone_Project/ResNet.h5')
        
    predictions = model.predict(image)[0]

     # Get the highest prediction
    max_index = np.argmax(predictions)
    max_label = labels_dict[max_index]
    max_prob = predictions[max_index]

    st.write(f"The model predicts the lesion to be **{max_label}** with a probability of **{max_prob:.2%}**")
