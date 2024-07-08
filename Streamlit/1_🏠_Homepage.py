import streamlit as st 

st.set_page_config(
    page_title="DermaGuard",
    page_icon="👨🏾‍⚕️"
)

st.title("Home 🏠")
st.sidebar.success(" Select page above.")

st.write("""
        **DermaGuard: AI-Driven Precision in Skin Cancer Detection**

        Welcome to DermaGuard, an innovative tool designed to assist in the early detection of skin cancer using advanced machine learning models. Our goal is to provide an accessible and accurate method for analyzing skin lesions, helping in the early diagnosis and treatment of skin cancer.

        ### Features:
        - Upload an image of a skin lesion for analysis.
        - Choose from multiple pre-trained models (DenseNet and ResNet) for prediction.
        - Get real-time prediction results.

        **Disclaimer:** This tool is for educational purposes only and should not be used as a substitute for professional medical advice.
    """)