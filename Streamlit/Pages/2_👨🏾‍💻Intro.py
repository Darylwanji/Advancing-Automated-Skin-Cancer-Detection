import streamlit as st 

st.title("Introduction")

st.write("""
        **About DermaGuard**

        DermaGuard is an AI-driven application developed to assist in the detection of skin cancer from images of skin lesions. Early detection of skin cancer is crucial for effective treatment and improved survival rates. By leveraging state-of-the-art machine learning models, DermaGuard aims to provide a reliable and efficient tool for preliminary analysis.

        ### How It Works:
        1. **Image Upload:** Users can upload an image of a skin lesion.
        2. **Model Selection:** Choose between different pre-trained models (DenseNet and ResNet) to analyze the image.
        3. **Prediction:** The selected model processes the image and provides a prediction.

        ### Technology:
        - **DenseNet:** A densely connected convolutional network known for its efficiency in image classification tasks.
        - **ResNet:** A residual network that addresses the vanishing gradient problem, allowing for the training of very deep networks.

        ### Purpose:
        DermaGuard is designed to be an educational tool to demonstrate the potential of machine learning in medical diagnostics. It is not intended to replace professional medical evaluation.

        **Disclaimer:** The predictions made by DermaGuard are not definitive and should not be used as a basis for any medical decisions. Always consult a healthcare professional for medical advice and diagnosis.
    """)