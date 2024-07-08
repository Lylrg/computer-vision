# Bone Fracture Detection using CNN


Welcome to our Bone Fracture Detection Project, where we ventured into the world of computer vision 📷 and deep learning 🧠to assist in medical diagnostics! This was our debut into image classification.

## Project Overview

The goal of this project is to develop a machine learning model that can accurately classify X-ray images as either showing signs of bone fractures or not. This is crucial for assisting medical professionals in diagnosing patients efficiently and accurately.

The dataset used in this project includes multi-region X-ray images focused on diagnosing bone fractures. You can download the dataset from [here](https://drive.google.com/file/d/1WeuxOenviI1_ElW5ISED4MhvR_YFYdmB/view).


### CNN (Convolutional Neural Network)

CNNs are specifically designed for processing grid-like data with inherent spatial relationships, such as images. Key characteristics include:

- **Architecture**: Built with convolutional layers that apply filters across input data to extract features like edges and textures.
- **Pooling**: Utilizes pooling layers to downsample features, reducing computational complexity and capturing hierarchical representations.
- **Parameter Efficiency**: Efficiently handles large inputs like images by sharing weights (filters), reducing the number of parameters and improving generalization.

### Implementation Details 💻🔍

- **PyTorch**: This project utilizes PyTorch for training the CNN model. PyTorch offers GPU acceleration (`torch.cuda`) for faster computation.
  
- **Keras**: If you have a potato computer 🥔 and don't support GPU, don't worry! We have converted the code into Keras. You can find the Keras implementation in the `converting_keras.ipynb` file.


### Data Augmentation

To enhance the robustness of the model and prevent overfitting, we performed data augmentation using the `ImageDataGenerator` from Keras with the following parameters:

### Validation Results

The performance metrics indicate that our model is highly effective in detecting bone fractures from X-ray images. Here are some key points:

- **High Test Accuracy**: The model correctly classifies 98.67% of the test samples.
- **Excellent Precision and Recall**: Precision of 98.00% and recall of 99.80% show the model's reliability in identifying true positives while minimizing false positives and false negatives.
- **Strong F1 Score**: The F1 Score of 98.89% balances precision and recall, demonstrating the model's overall effectiveness.

Additionally, our model was tested on a set of X-ray images that were misclassified by doctors. It correctly identified these images as showing signs of bone fractures, further validating its accuracy and potential as a diagnostic tool.

Overall, these results showcase the robustness and accuracy of our CNN model in bone fracture detection, making it a valuable tool for medical diagnostics.

### Deployed Model

We have deployed our model using Streamlit for easy access and testing. You can try it out [here](https://bonefracturedetector.streamlit.app).

## Team
This project was developed by:

[![LinkedIn](https://img.shields.io/badge/Alexandre-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alex-conte/)
[![LinkedIn](https://img.shields.io/badge/Rodrigo-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rodrigo-pierini/)
[![LinkedIn](https://img.shields.io/badge/Lydia-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lylrg/)


