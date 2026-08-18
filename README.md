# 🧠 AI-Based MRI Analysis

An AI-powered web application for brain tumor detection using MRI images. The system allows users to upload MRI scans and predicts the tumor type using a trained deep learning model.

## 🚀 Features

- Upload MRI images
- Automatic brain tumor detection
- Deep learning-based prediction
- User-friendly web interface
- Doctor login system
- Protected dashboard
- Prediction history page
- MRI image storage and management

## 🛠️ Technologies Used

### Frontend

- HTML
- CSS
- JavaScript

### Backend

- Python
- Django

### Machine Learning

- TensorFlow
- Keras
- NumPy

### Database

- SQLite

## 📂 Project Structure

```
AI-Based-MRI-Analysis/
│
├── ai/
├── config/
├── detector/
├── static/
├── templates/
├── manage.py
└── README.md
```

## 🧠 Tumor Classification

The model classifies MRI images into the following categories:

- Glioma
- Meningioma
- Pituitary Tumor
- No Tumor

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/AI-Based-MRI-Analysis.git
```

### Move to the project directory

```bash
cd AI-Based-MRI-Analysis
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

```bash
venv\Scripts\activate
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the server

```bash
python manage.py runserver
```

## 📸 Application Screens

- Home Page
- MRI Upload Page
- Result Page
- Doctor Login Page
- Dashboard
- History Page

## 🔒 Authentication

Only authenticated doctors can access:

- Dashboard
- History page

## 📈 Future Improvements

- User registration
- Advanced MRI analysis
- Cloud deployment
- Improved model accuracy

# 📸 Screenshots

## 🏠 Home Page

*Main entry point of the application with separate options for doctors and MRI analysis.*

---

## 🧠 MRI Upload Page

*Users can upload MRI images and enter patient information.*

---

## 📄 MRI Analysis Result

*Displays the predicted tumor type and the model's confidence score.

---

## 👨‍⚕️ Doctor Login

*Only authorized doctors can access the dashboard and patient history.*

---

## 📊 Doctor Dashboard

*Provides statistics and a summary of MRI analyses.*

---

## 📋 MRI Analysis History

*Displays previous MRI analyses and patient records.*

## 👨‍💻 Author

**Arjun Waman**

 BE (Information Technology)

## 📄 License

This project is developed for educational purposes.
