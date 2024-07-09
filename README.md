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
 
 TBA


### Methodology

TBA 

### Organization

#### Repository 
Project Directory/
├── Advancing Automated Skin Cancer Detection/
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

#### Dataset
[https://archive.ics.uci.edu/dataset/229/skin+segmentation
Bhatt,Rajen and Dhall,Abhinav. (2012). Skin Segmentation. UCI Machine Learning Repository. https://doi.org/10.24432/C5T30C.](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000?resource=download&select=HAM10000_metadata.csv)

### Credits & References

TBA
