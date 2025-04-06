# 🌱 VerdantScan

**VerdantScan** is an AI-powered web application designed to identify plant leaf diseases using deep learning. With a simple image upload, the app can detect whether a plant leaf is **Healthy**, infected by **Powdery Mildew**, or suffering from **Rust Disease** — along with prevention and cure tips.

---

## 📌 Project Overview

VerdantScan brings together **computer vision** and **agriculture** to make disease detection easier for farmers, researchers, and gardeners. Leveraging **pre-trained CNN models**, this project simplifies early disease diagnosis for better crop management.

---

## ✨ Features

- 📸 Upload leaf images for instant prediction
- 🧠 Deep learning with pre-trained CNN models (ResNet50, VGG16, MobileNetV2, etc.)
- 🩺 Get actionable tips for prevention and cure
- 🎨 Hover-over animated cards using Tailwind CSS
- 🧪 Flask backend for inference and deployment
- 📂 Train/test/validation dataset split for performance tracking

---

## 🗂 Dataset Used

- Source: [Kaggle – Plant Disease Recognition Dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset)
- Categories: **Healthy**, **Powdery Mildew**, **Rust**
- The dataset is split into:
- dataset/ ├── train/ ├── test/ └── validation/

---


---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MustafaHusain942/VerdantScan.git
cd VerdantScan```

### 2. Install Dependencies

```bash pip install -r requirements.txt ```

### 3. Train & Save Model Weights

Run the .ipynb files inside the models/ folder to train and save your model weights

🔁 Make sure to update the model path in app.py


