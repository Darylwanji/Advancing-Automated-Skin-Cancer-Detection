#  Advancing Automated Skin Cancer Detection 
## Leveraging Machine Learning for Accurate Skin Cancer Detection
=========================

### Executive Summary

The training of neural networks for the automated diagnosis of pigmented skin lesions, such as melanoma and basal cell carcinoma, is currently limited by the small size and lack of diversity in existing datasets of dermatoscopic images. Dermatoscopic images are critical for developing accurate machine-learning models that can assist in diagnosing various skin conditions. However, without a sufficiently large and diverse dataset, the neural networks may not perform well across different populations and types of lesions, leading to less reliable diagnostic tools.

#### Dataset Dictionary

HAM10000_images_part_1 and HAM10000_images_part_2:

These datasets contain the actual dermatoscopic images of skin lesions. They are typically stored as image files (e.g., JPEG, PNG) and are used for training and testing machine learning models for skin lesion diagnosis and segmentation.

HAM10000_metadata.csv:

This CSV file contains metadata associated with the HAM10000 dataset. Metadata usually includes information such as lesion ID, diagnosis (e.g., melanoma, nevus), patient characteristics (e.g., age, sex), and diagnostic method (e.g., histopathology, expert consensus). It serves as a key reference for linking image data to clinical and diagnostic details.
hmnist_28_28_L.csv:

This CSV file contains a subset of the HAM10000 dataset where each entry represents a 28x28 grayscale image of a skin lesion. Each pixel value is typically represented as an integer between 0 and 255, indicating the grayscale intensity.

hmnist_28_28_RGB.csv:

Similar to hmnist_28_28_L.csv, this CSV file contains a subset of the HAM10000 dataset but with each entry representing a 28x28 RGB (color) image of a skin lesion. Each pixel is represented by three values (Red, Green, Blue) indicating the color intensity.

hmnist_8_8_L.csv and hmnist_8_8_RGB.csv:

These CSV files contain another subset of the HAM10000 dataset but with images reduced to 8x8 resolution. hmnist_8_8_L.csv contains grayscale images, while hmnist_8_8_RGB.csv contains RGB images.

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
