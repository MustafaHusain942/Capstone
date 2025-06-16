import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
from tensorflow.keras.applications import DenseNet121
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
from PIL import Image
import io

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Set page config
st.set_page_config(page_title="Leaf Disease Classification", page_icon="🍃")

@st.cache_resource
def load_classification_model():
    try:
        model = load_model('best_densenet_model.h5')
    except:
        # If loading fails, recreate the model architecture
        base_model = DenseNet121(weights='imagenet', include_top=False, input_shape=(225, 225, 3))
        base_model.trainable = False
        
        x = base_model.output
        x = GlobalAveragePooling2D()(x)
        x = Dense(256, activation='relu')(x)
        x = Dropout(0.4)(x)
        output_layer = Dense(3, activation='softmax')(x)
        
        model = Model(inputs=base_model.input, outputs=output_layer)
        model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
        
        # Load weights if they exist
        if os.path.exists('best_densenet_model.h5'):
            model.load_weights('best_densenet_model.h5')
    
    return model

def predict_image(img):
    # Convert the uploaded file to an image
    img = Image.open(img).convert('RGB')
    img = img.resize((225, 225))
    
    # Convert to array and preprocess
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    
    # Make prediction
    predictions = model.predict(img_array)
    class_names = ['Healthy', 'Powdery', 'Rust']
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = float(np.max(predictions[0]))
    
    return predicted_class, confidence

# Load the model
model = load_classification_model()

# Main UI
st.title("Leaf Disease Classification")
st.write("Upload an image to classify leaf diseases")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    # Display the uploaded image
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    
    with col2:
        st.write("Classifying...")
        predicted_class, confidence = predict_image(uploaded_file)
        
        st.success(f"Prediction: {predicted_class}")
        st.info(f"Confidence: {confidence:.2%}")

# Add some information about the application
st.markdown("""
---
### About this app
This application uses a DenseNet121-based deep learning model to classify leaf diseases into three categories:
- Healthy
- Powdery Mildew
- Rust

Upload a clear image of a leaf to get the classification results.
""")