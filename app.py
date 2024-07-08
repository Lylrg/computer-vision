import streamlit as st
from PIL import Image
import numpy as np
import torch
import torch.nn as nn
import torchvision.transforms as transforms
import torch.nn.functional as F
import os

# Load Image and Adding to web app
im = Image.open('icon.jpeg')
st.set_page_config(layout="wide", page_title='Bone Fracture Detection App', page_icon=im)
st.title('Bone Fracture Detection 🦴')

# Define your model class if not already defined
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 64, kernel_size=3, padding=1)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(64, 32, kernel_size=3, padding=1)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.flatten = nn.Flatten()
        self.fc1 = nn.Linear(32 * 37 * 37, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool1(x)
        x = F.relu(self.conv2(x))
        x = self.pool2(x)
        x = self.flatten(x)
        x = F.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

# Load your pre-trained model
model = SimpleCNN()
model.load_state_dict(torch.load('bone_fracture_model_150.pth', map_location=torch.device('cpu')))
model.eval()  # Set the model to evaluation mode

# Define a function to preprocess the image
def preprocess_image(image):
    # Define the transformations: Convert to grayscale, resize and normalize
    transform = transforms.Compose([
        transforms.Grayscale(num_output_channels=1),  # Convert to grayscale
        transforms.Resize((150, 150)),  # Resize to the model's expected input shape
        transforms.ToTensor(),  # Convert to tensor
        transforms.Normalize((0.5,), (0.5,))  # Normalize to [-1, 1]
    ])
    image = transform(image)
    image = image.unsqueeze(0)  # Add batch dimension
    return image

# Define the prediction function
def predict(image):
    processed_image = preprocess_image(image)
    with torch.no_grad():
        prediction = model(processed_image)
    return prediction.item()

my_expander = st.expander(label='Hello there 👋')
with my_expander:
    'Three data scientist buddies made this classifier using CNN with PyTorch 🚀'
    # GitHub link
    st.write("If you're interested in knowing more about how this model was built, visit the GitHub repository.")

    st.markdown("[![Static Badge](https://img.shields.io/badge/GitHub%20repo-555555?logo=GitHub&logoColor=white)](https://github.com/Lylrg/computer-vision)")


# Layout for LinkedIn buttons
col1, col2, col3 = st.columns([1, 2, 3])
with col2:
    st.write(""" ### 🛠️ Instructions
    Upload an X-ray image to detect if there is a fracture or not. 💻 This app uses a convolutional neural network (CNN) model to analyze the uploaded X-ray images and predict the presence of bone fractures.
             """)


with col1:
    st.subheader("👩‍💻👨‍💻 Creators")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/Alexandre-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/alex-conte/)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/Lydia-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lylrg/)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/Rodrigo-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rodrigo-pierini/)")

with col3:
    st.write(""" ### 🖼️ Example Images Source
    The example images are extracted from the paper titled "Traumatic fractures in adults: missed diagnosis on plain radiographs in the Emergency Department" by Antonio Pinto et al., where the images were misdiagnosed by a doctor.
             """)



# Instruction text
st.write("📂 Please upload an X-ray image or select an example image.")
st.write('Do not use this app for autodiagnosis purposes under any circumstances.')

# File uploader for user-uploaded images
uploaded_file = st.file_uploader('Upload an image...', type=['jpg', 'jpeg', 'png'])

# Dropdown menu for example images
example_images_path = 'example_images'
example_images = [f for f in os.listdir(example_images_path) if f.endswith(('jpg', 'jpeg', 'png'))]
selected_example = st.selectbox("Or choose an example image:", ["None"] + example_images)

if uploaded_file is not None:
    # Create two columns
    col1, col2 = st.columns(2)
    
    # Load the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image in the left column
    with col1:
        st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Display classification results in the right column
    with col2:
        # Make a prediction
        prediction = predict(image)
        
        # Display the result
        if prediction < 0.5:  # Assuming the model outputs a single sigmoid value for binary classification
            wasted = Image.open('wasted.jpg')
            st.image(wasted, use_column_width=True)
            st.write('There is a fracture.')
        else:
            thumbs = Image.open('thumbs.jpg')
            st.image(thumbs, use_column_width=True)
            st.write('There is NO fracture.')
elif selected_example != "None":
    # Create two columns
    col1, col2 = st.columns(2)
    
    # Load the selected example image
    image = Image.open(os.path.join(example_images_path, selected_example))
    
    # Display the selected example image in the left column
    with col1:
        st.image(image, caption='Example Image', use_column_width=True)
    
    # Display classification results in the right column
    with col2:
        # Make a prediction
        prediction = predict(image)
        
        # Display the result
        if prediction < 0.5:  # Assuming the model outputs a single sigmoid value for binary classification
            wasted = Image.open('wasted.jpg')
            st.image(wasted, use_column_width=True)
            st.write('There is a fracture.')
        else:
            thumbs = Image.open('thumbs.jpg')
            st.image(thumbs, use_column_width=True)
            st.write('There is NO fracture.')

