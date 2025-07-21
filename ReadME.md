# 🧠 MRI-Based Age Detection Web Application

## 🚀 Overview

This project is a **Django-based web application** that predicts a person's age from MRI scan data using **deep learning**. Users can upload MRI scan files (in `.h5` format), which are then processed using a **pre-trained neural network** to predict age. The application features secure user authentication, an admin panel, dataset management, and a responsive UI built with Bootstrap.

---

## 📚 Table of Contents

* [Project Structure](#project-structure)
* [Features](#features)
* [Setup & Installation](#setup--installation)
* [Usage Guide](#usage-guide)
* [Technical Details](#technical-details)
* [File/Folder Descriptions](#filefolder-descriptions)
* [Dependencies](#dependencies)
* [Customization & Extending](#customization--extending)
* [Troubleshooting](#troubleshooting)
* [Credits](#credits)

---

## 🏗️ Project Structure

* `Mri_Based_Age_Dect/`: Django project settings and ASGI/WSGI configurations.
* `user/`: Main app for user authentication, MRI upload, prediction, and admin control.
* `static/images/`: Directory containing MRI files, the machine learning model (`my_model.h5`), and other static assets.
* `templates/`: HTML templates for user and admin interfaces.
* `db.sqlite3`: SQLite database for user and session data.

---

## ✨ Features

* **User Registration & Login**: Secure access control for users and admins.
* **MRI Upload & Prediction**: Upload `.h5` MRI files and receive instant age predictions.
* **Admin Panel**: Admins can manage user accounts and view activity.
* **Dataset Management**: Basic interface for managing uploaded MRI scans.
* **Modern UI**: Responsive and clean interface using Bootstrap.

---

## 🛠️ Setup & Installation

### Prerequisites

* Python 3.8+
* pip
* Virtual environment tool (`venv`, `virtualenv`, etc.)

### Installation Steps

```bash
# 1. Clone the repository:
git clone https://github.com/yourusername/mri-age-detection.git
cd mri-age-detection

# 2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# 3. Install dependencies:
pip install -r requirements.txt

# 4. Apply migrations:
python manage.py makemigrations
python manage.py migrate

# 5. Run the development server:
python manage.py runserver
```

### Access the Application

Open your browser and go to: `http://127.0.0.1:8000/`

---

## 👤 Usage Guide

### User Workflow

1. Register or log in to your account.
2. Navigate to the **Prediction** page.
3. Upload an `.h5` MRI scan file.
4. Receive your **predicted age** instantly.

### Admin Workflow

1. Log in as an admin.
2. View, activate, or delete registered users.

---

## 🔬 Technical Details

### Deep Learning Pipeline

#### 1. Data Ingestion & Preprocessing

* Uploaded `.h5` files are read using `h5py`.
* Volumetric MRI data is normalized and reshaped to match the model's input requirements.

#### 2. Model Architecture

* A **deep convolutional neural network (CNN)** built with Keras and TensorFlow.
* Trained on a dataset of MRI scans labeled with corresponding ages.
* Consists of multiple convolutional, pooling, and dense layers optimized for regression.

#### 3. Prediction

* The preprocessed MRI data is passed through the model.
* The model outputs a **continuous age value**.

#### 4. Result Display

* The predicted age is displayed in a clean, user-friendly interface.

### Key Files

* `user/utility/uti.py`: Handles file reading, preprocessing, and model inference.
* `user/views.py`: Manages requests, uploads, and rendering.
* `static/images/my_model.h5`: Pre-trained model for prediction.

---

## 📁 File/Folder Descriptions

* `Mri_Based_Age_Dect/`: Django settings, URLs, ASGI/WSGI apps.
* `user/`: Business logic for authentication and prediction.
* `static/images/`: MRI data, images, and model weights.
* `templates/`: UI HTML templates.
* `db.sqlite3`: Local database file.

---

## 📦 Dependencies

* `Django`
* `numpy`
* `pandas`
* `h5py`
* `scikit-learn`
* `matplotlib`
* `seaborn`
* `tensorflow` (Keras backend)

---

## 🧑‍💻 Customization & Extending

* **Model Update**: Replace `my_model.h5` with a retrained or fine-tuned Keras model.
* **New Features**: Add disease classification, MRI segmentation, or analytics.
* **UI Improvements**: Enhance layout and styling using modern frontend tools.

---

## ❗ Troubleshooting

* **File Upload Errors**: Make sure files are in `.h5` format with correct structure.
* **Model Errors**: Ensure `my_model.h5` exists and is compatible.
* **Static File Issues**: Verify `STATIC_URL` and `STATICFILES_DIRS` in `settings.py`.

---

## 📝 Credits

* MRI Data and Model: *\[Insert source or citation]*
* Built using: **Django**, **Keras**, **TensorFlow**, **Bootstrap**

---

## 📷 Example Screenshots

> *(Add screenshots of home, prediction, and result pages here)*

---

## 💡 Final Thoughts

This project showcases how **deep learning** can extract meaningful insights from **complex medical data**. By automating age prediction from MRI scans, we aim to support medical research and clinical tools that rely on understanding the aging brain.

> 🚀 Ready to explore? Clone the repo, upload a scan, and experience the power of AI in medicine!

---
