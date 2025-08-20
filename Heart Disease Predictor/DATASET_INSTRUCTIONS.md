# Dataset Setup Instructions

## 📊 Heart Disease Prediction Dataset

Due to GitHub's file size limitations (100MB), the dataset file is not included in this repository.

## 🔍 Dataset Information

- **File Name**: `Heart_Disease_Prediction_Dataset.csv`
- **Size**: ~72MB
- **Format**: CSV (Comma Separated Values)
- **Features**: 50+ health indicators

## 📥 How to Obtain the Dataset

### Option 1: Use Your Existing Dataset
If you already have the dataset file:
1. Place `Heart_Disease_Prediction_Dataset.csv` in the project root directory
2. Ensure it contains all required features (see feature list below)

### Option 2: Create Sample Dataset
If you don't have the original dataset, you can:
1. Use the `DatasetReader.py` helper function to understand the expected format
2. Create a sample dataset with the required features
3. Train the models using the Jupyter notebook

## 📋 Required Features

The application expects the following features in your CSV file:

### Demographics
- `Gender` (0/1)
- `Age_25_29`, `Age_30_34`, `Age_35_39`, `Age_40_44`, `Age_45_49`, `Age_50_54`, `Age_55_59`, `Age_60_64`, `Age_65_69`, `Age_70_74`, `Age_75_79`, `Age_80_plus` (boolean)
- `PhysicalActivities` (0/1)
- `PhysicalHealthDays` (0-30)

### Medical History
- `HadAngina` (0/1)
- `HadStroke` (0/1)
- `HadSkinCancer` (0/1)
- `HadKidneyDisease` (0/1)
- `HadArthritis` (0/1)
- `ChestScan` (0/1)

### Functional Status
- `DeafOrHardOfHearing` (0/1)
- `BlindOrVisionDifficulty` (0/1)
- `DifficultyConcentrating` (0/1)
- `DifficultyWalking` (0/1)
- `DifficultyDressingBathing` (0/1)

### Health Status
- `GeneralHealth_Fair`, `GeneralHealth_Good`, `GeneralHealth_Poor`, `GeneralHealth_Very_good` (boolean)
- `HadDiabetes_No`, `HadDiabetes_Yes`, `HadDiabetes_Pregnancy` (boolean)

### Lifestyle Factors
- `Smoker_Never`, `Smoker_Former`, `Smoker_CurrentSomeDays` (boolean)
- `ECig_NotAtAll`, `ECig_SomeDays`, `ECig_EveryDay` (boolean)
- `AlcoholDrinkers` (0/1)

### Immunization & Testing
- `PneumoVaxEver` (0/1)
- `Covid_Yes`, `Covid_HomeTest` (boolean)

### Target Variable
- `HeartDisease` (0/1) - The target variable for training

## 🔧 Data Format Requirements

- **Encoding**: UTF-8
- **Delimiter**: Comma (,)
- **Missing Values**: Handle appropriately (fill with 0 or mean values)
- **Data Types**: 
  - Binary features: 0 or 1
  - Boolean features: true/false or 0/1
  - Numerical features: integers or floats

## 📝 Example Data Structure

```csv
Gender,PhysicalHealthDays,PhysicalActivities,HadAngina,HadStroke,HeartDisease,...
1,5,1,0,0,0,...
0,0,1,0,0,0,...
1,10,0,1,0,1,...
```

## ⚠️ Important Notes

1. **Data Privacy**: Ensure your dataset doesn't contain personally identifiable information
2. **Data Quality**: Clean and preprocess your data before training
3. **Feature Names**: Column names must match exactly with the expected feature names
4. **Data Balance**: Ensure balanced representation of positive and negative cases

## 🚀 Next Steps

Once you have the dataset:
1. Place it in the project root directory
2. Run the Jupyter notebook to train the models
3. Start the application with `python app.py`

## 📞 Support

If you need help with dataset preparation or encounter issues, please:
1. Check the Jupyter notebook for data preprocessing steps
2. Review the `DatasetReader.py` helper function
3. Open an issue on GitHub for additional support
