# Heart Disease Risk Predictor

A comprehensive web application that uses both Machine Learning and Deep Learning models to predict heart disease risk based on various health indicators.

## Project Overview

This project implements a dual-model approach for cardiovascular risk assessment:
- **Machine Learning Model**: Logistic Regression for traditional statistical analysis
- **Deep Learning Model**: Neural Network for advanced pattern recognition

## Features

- **Real-time Risk Assessment**: Instant predictions using both ML and DL models
- **Comprehensive Health Evaluation**: Analyzes 50+ health indicators including:
  - Demographics (age, gender)
  - Medical history (angina, stroke, diabetes, etc.)
  - Lifestyle factors (smoking, alcohol, physical activity)
  - Functional status (mobility, vision, hearing)
- **Modern Web Interface**: User-friendly HTML/CSS/JavaScript frontend
- **RESTful API**: FastAPI backend for scalable deployment
- **Dual Model Comparison**: Get predictions from both ML and DL approaches

## Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Machine Learning**: Scikit-learn, Logistic Regression
- **Deep Learning**: TensorFlow/Keras, Neural Networks
- **Data Processing**: Pandas, NumPy
- **Model Persistence**: Joblib, Keras HDF5

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download the dataset**
   - Place your heart disease dataset CSV file in the project root
   - Rename it to `Heart_Disease_Prediction_Dataset.csv`
   - Ensure it contains the required features (see dataset section below)

5. **Train the models** (if needed)
   - Run the Jupyter notebook: `Final Notebook.ipynb`
   - This will generate the `ML.pkl` and `DL.h5` model files

## Usage

1. **Start the application**
   ```bash
   python app.py
   ```

2. **Access the web interface**
   - Open your browser and go to: `http://127.0.0.1:8001`
   - Fill in the health assessment form
   - Click "Calculate Risk Assessment" to get predictions

3. **API Endpoint**
   - POST request to: `http://127.0.0.1:8001/predict`
   - Send form data with all required health indicators

## Dataset Requirements

The application expects a CSV file with the following features:
- Demographics: Gender, Age categories, Physical activities
- Medical History: Angina, Stroke, Skin cancer, Kidney disease, Arthritis, etc.
- Functional Status: Hearing, Vision, Mobility, Concentration difficulties
- Health Status: General health, Diabetes status
- Lifestyle: Smoking, E-cigarette usage, Alcohol consumption
- Immunization: Pneumonia vaccine, COVID-19 status

## Project Structure

```
heart-disease-prediction/
├── app.py                          # FastAPI backend
├── index.html                      # Web interface
├── ML.pkl                          # Trained ML model
├── DL.h5                           # Trained DL model
├── Final Notebook.ipynb            # Analysis and training notebook
├── Helper Function/
│   └── DatasetReader.py           # Data processing utilities
├── Deliverables/
│   └── Deliverable 1.pdf          # Project documentation
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── .gitignore                      # Git ignore rules
```


## Disclaimer

This application is for educational and research purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical decisions.


---

**Note**: The dataset file (`Heart_Disease_Prediction_Dataset.csv`) is not included in this repository due to size limitations. Please ensure you have the appropriate dataset file in place before running the application.
