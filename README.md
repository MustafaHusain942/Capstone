# 🌱 VerdantScan

**VerdantScan** is an intelligent, AI-powered web application developed to assist farmers, agriculturists, and plant enthusiasts in identifying diseases in plant leaves with ease and accuracy. Leveraging the power of deep learning and computer vision, VerdantScan is capable of analyzing leaf images to classify them into one of the following categories: Healthy, Powdery Mildew, or Rust Disease.

With just a simple image upload, the application processes the image through trained Convolutional Neural Network (CNN) models to predict the plant’s health status in real-time. The results are not only limited to disease identification; VerdantScan also provides informative descriptions, prevention tips, and curative measures to help users take quick and effective action.

Whether managing a large-scale farm or caring for your home garden, VerdantScan aims to bridge the gap between agriculture and artificial intelligence, promoting healthier crops and more informed decision-making through accessible, tech-driven solutions.

---

📚 Table of Contents

- ✨ Features

- 🗂 Dataset Used

- ⚙️ Installation

- 🧰 Technologies Used

- 🚀 How to Use

- 🤝 Contributing

---

## ✨ Features

-  AI-Powered Disease Detection from uploaded plant leaf images
-  Interactive Queue Cards that reveal condition and cure information on hover
-  Categorization of Healthy, Powdery Mildew, and Rust conditions
-  Actionable Cure & Prevention Advice

---

## 🗂 Dataset Used

- Source: [Kaggle – Plant Disease Recognition Dataset](https://www.kaggle.com/datasets/rashikrahmanpritom/plant-disease-recognition-dataset)
- Categories: **Healthy**, **Powdery Mildew**, **Rust**
- The dataset is split into:
 ```bash
  dataset/ ├── train/ ├── test/ └── validation/
```

---

## ⚙️ Installation & Setup

###  1. Clone the Repository

```bash
git clone https://github.com/MustafaHusain942/VerdantScan.git
cd VerdantScan
```

###  2. Install Required Dependencies

```bash
pip install -r requirements.txt 
```

###  3. Train the Model to Get Weights

Run the .ipynb files to train and save your model weights

🔁 Make sure to update the model path in app.py

###  4. Run the Flask App

```bash
python app.py
```
```bash
http://127.0.0.1:5000
```

---

/

## 🧰 Technologies Used

- Python

- TensorFlow/Keras for model building

- Flask for backend API and routing

- TailwindCSS for modern responsive UI

- Matplotlib, OpenCV for data visualization and preprocessing

- Jupyter Notebook for training and experimentation

---

## 🚀 How to Use

- Upload a clear image of a plant leaf through the app.

- The AI model analyzes the image and predicts the condition.

- The app shows a queue card with:

- Condition (Healthy, Powdery Mildew, Rust)

- Description

- Tips for prevention/cure

- Hover on the image card to reveal actionable insights!

---

## 🤝 Contributing

We welcome all contributions to enhance VerdantScan! Here's how you can help:

- Fork this repository

- Create a feature branch:
  ```bash
  git checkout -b feature-name
  ```

- Commit your changes:
  ```bash
  git commit -am 'Add new feature'
  ```
  
- Push the branch:
```bash
  git push origin feature-name
```
- Open a Pull Request
