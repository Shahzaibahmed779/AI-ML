import pandas as pd

def inspect_csv(file_path):
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    print("\n📄 Basic Info:")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    
    print("\n🏷️ Column Labels:")
    print(df.columns.tolist())

    print("\n🧬 Data Types:")
    print(df.dtypes)

    print("\n❓ Missing Values:")
    print(df.isnull().sum())

    print("\n🔍 Sample Data (first 5 rows):")
    print(df.head())


inspect_csv('Heart_Disease_Prediction_Dataset.csv')
