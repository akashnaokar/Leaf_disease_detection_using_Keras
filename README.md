# Leaf Disease Detection Using Deep Learning & Keras

This project utilizes deep learning techniques to detect plant diseases from images of plant leaves. It employs convolutional neural networks (CNNs) implemented in Python using libraries such as TensorFlow and Keras.

## Project Overview

The project aims to develop a system capable of accurately identifying plant diseases from images of leaves. Early detection of diseases is crucial in agriculture to prevent crop losses and ensure food security.

## Implementation Steps

1. **Dataset Preparation:** The dataset consists of images of plant leaves affected by various diseases. Images are preprocessed and organized into training and testing sets.

2. **Model Building:** A CNN model is constructed using Keras. The model architecture includes convolutional layers, pooling layers, dropout layers, and dense layers.

3. **Training:** The model is trained on the training dataset using an appropriate optimizer and loss function. Data augmentation techniques are applied to improve model generalization.

4. **Evaluation:** The trained model is evaluated using the testing dataset to assess its accuracy in disease detection.

5. **Prediction:** The model is used to predict the class of an input leaf image. The predicted class and probability are displayed along with the input image.

## Dataset

The dataset used in this project can be found on Kaggle: [New Plant Diseases Dataset](https://www.kaggle.com/datasets/vipoooool/new-plant-diseases-dataset/data). It comprises images of plant leaves with various diseases, organized into folders based on the specific disease.

To obtain the dataset:
- Visit the provided Kaggle link.
- Download the dataset files from the Kaggle website.
- Extract the downloaded files into the appropriate directory in your project.