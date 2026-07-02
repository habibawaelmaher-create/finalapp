
# 🩺 Diabetes Prediction Using Deep Learning

A machine learning project that predicts whether a person is likely to have diabetes based on medical information. The project includes data preprocessing, exploratory data analysis, model training using TensorFlow/Keras, and deployment through a Streamlit web application.

---

## 📌 Project Overview

This project uses the Pima Indians Diabetes Dataset to build a binary classification model that predicts whether a patient has diabetes.

The workflow includes:

- Data loading and exploration
- Data cleaning
- Outlier detection and removal
- Feature scaling
- Data visualization
- Model training using a Deep Neural Network (DNN)
- Model evaluation
- Saving the trained model and scaler
- Streamlit web application for real-time predictions

---

## 📂 Project Structure


├── archive/
│   └── diabetes.csv
├── notebook.ipynb
├── StreamlitUI.py
├── diabetes_model.pkl
├── diabetes_scaler.pkl
├── requirements.txt
└── README.md


---

## 📊 Dataset

The project uses the *Pima Indians Diabetes Dataset*, which contains medical information about female patients.

### Features

- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

### Target

- *Outcome*
  - 0 → No Diabetes
  - 1 → Diabetes

---

## ⚙️ Data Preprocessing

The following preprocessing steps were performed:

- Checked for missing values
- Removed duplicate records
- Detected and removed outliers using the IQR method
- Normalized features using *MinMaxScaler*
- Split the data into training, validation, and testing sets

---

## 📈 Exploratory Data Analysis

Several visualizations were created to better understand the dataset, including:

- Class distribution
- Correlation heatmap
- Feature distributions
- Scatter plots
- Outlier analysis

---

## 🤖 Model

A Deep Neural Network (DNN) was built using TensorFlow/Keras.

### Architecture

- Input Layer
- Dense Layer (ReLU)
- Dropout
- Dense Layer (ReLU)
- Dropout
- Output Layer (Sigmoid)

### Loss Function

- Binary Crossentropy

### Optimizer

- Adam

### Evaluation Metric

- Accuracy

---

## 💻 Streamlit Application

The Streamlit interface allows users to enter:

- Glucose
- BMI
- Pregnancies
- Diabetes Pedigree Function
- Age

The application:

1. Loads the saved scaler.
2. Normalizes the user input.
3. Loads the trained model.
4. Predicts whether diabetes is likely.
5. Displays the prediction.

---

## 🚀 Installation

Clone the repository:

bash
git clone https://github.com/yourusername/diabetes-prediction.git


Move into the project folder:

bash
cd diabetes-prediction


Create a virtual environment:

### Windows

bash
python -m venv jano-env
jano-env\Scripts\activate


### Linux/macOS

bash
python3 -m venv jano-env
source jano-env/bin/activate


Install dependencies:

bash
pip install -r requirements.txt


---

## ▶️ Running the Application

Run the Streamlit app:

bash
streamlit run StreamlitUI.py


The application will open in your web browser.

---

## 📦 Required Libraries

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- tensorflow
- streamlit
- joblib

Install manually if needed:

bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow streamlit joblib


---

## 📊 Results

The trained deep learning model successfully classifies patients as diabetic or non-diabetic based on the selected medical features.

The deployed Streamlit application enables users to obtain instant predictions through an easy-to-use graphical interface.

---

## 🔮 Future Improvements

- Improve prediction accuracy through hyperparameter tuning.
- Add more machine learning model comparisons.
- Display prediction probabilities.
- Deploy the application online using Streamlit Community Cloud.
- Add feature importance and explainability (SHAP/LIME).

---

## 👨‍💻 Author

Jano Khaled
Habiba Wael 

Computer Engineering Student

---

## 📄 License

This project is intended for educational purposes.