#  DermaGuard: AI-Driven Precision in Skin Cancer Detection
## Leveraging Machine Learning for Accurate Skin Cancer Detection
=========================

### Executive Summary

The training of neural networks for the automated diagnosis of pigmented skin lesions, such as melanoma and basal cell carcinoma, is currently limited by the small size and lack of diversity in existing datasets of dermatoscopic images. Dermatoscopic images are critical for developing accurate machine-learning models that can assist in diagnosing various skin conditions. However, without a sufficiently large and diverse dataset, the neural networks may not perform well across different populations and types of lesions, leading to less reliable diagnostic tools.

# Data Dictionary

| Column Name              | Description                                                                                            |
|--------------------------|--------------------------------------------------------------------------------------------------------|
| lesion_id                | Unique identifier for the lesion.                                                                      |
| image_id                 | Unique identifier for the image.                                                                       |
| Diagnosis                | Diagnosis code of the lesion (e.g., bkl for benign keratosis-like lesions, mel for melanoma, nv for melanocytic nevus). |
| Confirmation_Method      | Method used to confirm the diagnosis, e.g., histo (histology) or follow_up.                            |
| Age                      | Age of the patient.                                                                                    |
| Sex                      | Sex of the patient.                                                                                    |
| Location                 | Anatomical location of the lesion on the body.                                                         |
| Image_path               | File path to the image.                                                                                |
| Updated_Diagnosis_Label  | Updated label for the diagnosis, used for additional categorization or correction.                     |


### Demo

 To experience the application:

1. **Run the Streamlit App:**   
   `streamlit run 1_🏠_Homepage.py `     
      
   ![Sample run](https://github.com/Darylwanji/Advancing-Automated-Skin-Cancer-Detection/blob/main/Assets/Other/runstream.png?raw%3Dtrue)

2. **Navigation Steps:**
- Navigate through the different pages and go to the **DermaGuard** page.

1. **Usage Steps:**
- On the DermaGuard page, upload a lesion picture.      
     
  ![DermaGuard](https://github.com/Darylwanji/Advancing-Automated-Skin-Cancer-Detection/blob/main/Assets/Other/Derma.png?raw%3Dtrue)


- Select a model: **DenseNet** or **ResNet**.
- View the classification result.


### Methodology

##### Data Collection and Preprocessing
The dataset used in this project consists of high-resolution images of skin cancer lesions. The images were obtained from Kaggle, and is a publicly available dataset. Each image was labeled with the corresponding type of skin lesion.

Before training, the images were preprocessed as follows:

Resizing: All images were resized to a standard dimension of 224x224 pixels to match the input size required by DenseNet121 and ResNet50.

Normalization: Pixel values were scaled to the range [0, 1] for consistency and to facilitate model convergence.

Augmentation: Data augmentation techniques, such as rotation, flipping, and zooming, were applied to increase the diversity of the training set and reduce overfitting.

##### Model Selection
Two convolutional neural network architectures, DenseNet121 and ResNet50, were selected for this project due to their proven effectiveness in image classification tasks.

DenseNet121: DenseNet121 is known for its dense connectivity pattern, where each layer receives input from all preceding layers. This promotes feature reuse and mitigates the vanishing gradient problem, leading to efficient training.

ResNet50: ResNet50, a 50-layer deep residual network, utilizes skip connections or shortcuts to jump over some layers. This architecture helps in training very deep networks by preventing the vanishing gradient problem and ensuring that the network learns effectively.

##### Training Procedure
Initialization: Both DenseNet121 and ResNet50 models were initialized with pre-trained weights from the ImageNet dataset. This transfer learning approach leverages pre-learned features, enabling faster convergence and better performance, especially when dealing with limited data.

##### Implementation
The models were implemented using TensorFlow and Keras libraries. The training was conducted on a GPU-enabled environment to expedite the process.

By employing both DenseNet121 and ResNet50, the project aims to leverage the strengths of each architecture to achieve high accuracy in classifying skin cancer lesions, thereby aiding in early and accurate diagnosis.

### Organization

#### Repository 
```md
Project Directory/
├── Advancing Automated Skin Cancer Detection/  # Version controlled
│   ├── Assets/
│   │   └── # Contains project's assets (Graphs, Pictures, etc.)
│   ├── Docs/
│   │   └── # Contains final report, presentations which summarize the project
│   ├── Notebooks/
│   │   └── # Contains all final notebooks involved in the project
│   ├── References/
│   │   └── # Contains papers/tutorials used in the project
│   ├── Streamlit/
│   │   └── # Streamlit App files
│   ├── README.md
│   │   └── # Project landing page (this page)
│   └── LICENSE
│       └── # Project license
├── data/
│   ├── # Contains link to copy of the dataset (stored locally as it is over 5GB)
│   └── # Saved copy of aggregated/processed data as long as those are not too large (> 10MB)
├── model/
│   └── # `h5` dump of final model(s)
└── .gitignore
    └── # Part of Git, includes files and folders to be ignored by Git version control
```
#### Dataset

The dataset is too large to be included in the project. However, you can access and download it from the following link.

[https://archive.ics.uci.edu/dataset/229/skin+segmentation
Bhatt,Rajen and Dhall,Abhinav. (2012). Skin Segmentation. UCI Machine Learning Repository. https://doi.org/10.24432/C5T30C.](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000?resource=download&select=HAM10000_metadata.csv)

### Credits & References

> DenseNet : https://www.kaggle.com/code/angelarentsi/skin-disease-classification-densenet#DenseNet121  
> ResNet : Brainstation Class material

