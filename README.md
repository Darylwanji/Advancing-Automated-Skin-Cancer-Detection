#  DermaGuard: AI-Driven Precision in Skin Cancer Detection
## Leveraging Machine Learning for Accurate Skin Cancer Detection
=========================

### Executive Summary

The training of neural networks for the automated diagnosis of pigmented skin lesions, such as melanoma and basal cell carcinoma, is currently limited by the small size and lack of diversity in existing datasets of dermatoscopic images. Dermatoscopic images are critical for developing accurate machine-learning models that can assist in diagnosing various skin conditions. However, without a sufficiently large and diverse dataset, the neural networks may not perform well across different populations and types of lesions, leading to less reliable diagnostic tools.

#### Dataset Dictionary
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

* `data` 
    - contains link to copy of the dataset (stored in a publicly accessible cloud storage)
    - saved copy of aggregated / processed data as long as those are not too large (> 10 MB)

* `model`
    - `joblib` dump of final model(s)

* `notebooks`
    - contains all final notebooks involved in the project

* `docs`
    - contains final report, presentations which summarize the project

* `references`
    - contains papers / tutorials used in the project

* `src`
    - Contains the project source code (refactored from the notebooks)

* `.gitignore`
    - Part of Git, includes files and folders to be ignored by Git version control

* `conda.yml`
    - Conda environment specification

* `README.md`
    - Project landing page (this page)

* `LICENSE`
    - Project license

#### Dataset
[https://archive.ics.uci.edu/dataset/229/skin+segmentation
Bhatt,Rajen and Dhall,Abhinav. (2012). Skin Segmentation. UCI Machine Learning Repository. https://doi.org/10.24432/C5T30C.](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000?resource=download&select=HAM10000_metadata.csv)

### Credits & References

TBA
