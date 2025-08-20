from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import joblib
import numpy as np
import uvicorn

# Initialize FastAPI app
app = FastAPI()

# Enable CORS for all origins (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with a specific origin if needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/", StaticFiles(directory=".", html=True), name="static")

# Load models with error handling
try:
    ml_model = joblib.load("ML.pkl")
    ml_available = True
except Exception as e:
    print(f"Warning: Could not load ML model: {e}")
    ml_model = None
    ml_available = False

try:
    from keras.models import load_model
    dl_model = load_model("DL.h5")
    dl_available = True
except ImportError:
    print("Warning: TensorFlow/Keras not available. Deep Learning model will not be used.")
    dl_model = None
    dl_available = False
except Exception as e:
    print(f"Warning: Could not load DL model: {e}")
    dl_model = None
    dl_available = False

@app.post("/predict")
def predict(
    Gender: int = Form(...),
    PhysicalHealthDays: float = Form(...),
    PhysicalActivities: int = Form(...),
    HadAngina: int = Form(...),
    HadStroke: int = Form(...),
    HadSkinCancer: int = Form(...),
    HadKidneyDisease: int = Form(...),
    HadArthritis: int = Form(...),
    DeafOrHardOfHearing: int = Form(...),
    BlindOrVisionDifficulty: int = Form(...),
    DifficultyConcentrating: int = Form(...),
    DifficultyWalking: int = Form(...),
    DifficultyDressingBathing: int = Form(...),
    ChestScan: int = Form(...),
    AlcoholDrinkers: int = Form(...),
    PneumoVaxEver: int = Form(...),
    GeneralHealth_Fair: bool = Form(...),
    GeneralHealth_Good: bool = Form(...),
    GeneralHealth_Poor: bool = Form(...),
    GeneralHealth_Very_good: bool = Form(...),
    HadDiabetes_No: bool = Form(...),
    HadDiabetes_Yes: bool = Form(...),
    HadDiabetes_Pregnancy: bool = Form(...),
    Smoker_CurrentSomeDays: bool = Form(...),
    Smoker_Former: bool = Form(...),
    Smoker_Never: bool = Form(...),
    ECig_NotAtAll: bool = Form(...),
    ECig_EveryDay: bool = Form(...),
    ECig_SomeDays: bool = Form(...),
    Age_25_29: bool = Form(...),
    Age_30_34: bool = Form(...),
    Age_35_39: bool = Form(...),
    Age_40_44: bool = Form(...),
    Age_45_49: bool = Form(...),
    Age_50_54: bool = Form(...),
    Age_55_59: bool = Form(...),
    Age_60_64: bool = Form(...),
    Age_65_69: bool = Form(...),
    Age_70_74: bool = Form(...),
    Age_75_79: bool = Form(...),
    Age_80_plus: bool = Form(...),
    Covid_HomeTest: bool = Form(...),
    Covid_Yes: bool = Form(...)
):
    input_data = [
        Gender, PhysicalHealthDays, PhysicalActivities, HadAngina, HadStroke, HadSkinCancer, HadKidneyDisease,
        HadArthritis, DeafOrHardOfHearing, BlindOrVisionDifficulty, DifficultyConcentrating, DifficultyWalking,
        DifficultyDressingBathing, ChestScan, AlcoholDrinkers, PneumoVaxEver,
        GeneralHealth_Fair, GeneralHealth_Good, GeneralHealth_Poor, GeneralHealth_Very_good,
        HadDiabetes_No, HadDiabetes_Yes, HadDiabetes_Pregnancy,
        Smoker_CurrentSomeDays, Smoker_Former, Smoker_Never,
        ECig_NotAtAll, ECig_EveryDay, ECig_SomeDays,
        Age_25_29, Age_30_34, Age_35_39, Age_40_44, Age_45_49, Age_50_54,
        Age_55_59, Age_60_64, Age_65_69, Age_70_74, Age_75_79, Age_80_plus,
        Covid_HomeTest, Covid_Yes
    ]

    input_array = np.array([input_data])
    
    # ML Model prediction
    if ml_available and ml_model is not None:
        try:
            ml_result = int(ml_model.predict(input_array)[0])
        except Exception as e:
            print(f"Error in ML prediction: {e}")
            ml_result = 0
    else:
        ml_result = 0
    
    # DL Model prediction
    if dl_available and dl_model is not None:
        try:
            dl_result = int(dl_model.predict(input_array)[0] >= 0.5)
        except Exception as e:
            print(f"Error in DL prediction: {e}")
            dl_result = 0
    else:
        dl_result = 0

    return {
        "ML_Model_Result": ml_result,
        "DL_Model_Result": dl_result,
        "ML_Available": ml_available,
        "DL_Available": dl_available
    }

# Only run when executing the script directly
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
