# Medical Appointment No-Show Risk Prediction (XGBoost, SHAP)
*High-Recall Machine Learning & Prescriptive Strategy for Clinical Operations*

## The Business Problem
Medical no-shows cost clinics thousands in lost revenue and idle provider time. This project identifies high-risk patients *before* their appointments and prescribes a mathematical scheduling strategy to mitigate the loss.

## Technical Highlights
- **Model:** XGBoost Classifier achieved a **ROC-AUC of 0.71** and optimized the model for **91% Recall** to maximize detection of potential revenue leakage cases.
- **Calibration:** Used `CalibratedClassifierCV` to translate uncalibrated probabilities into honest, real-world probabilities.
- **Interpretability:** Used **SHAP** values to break open the "black box" and map the behavioral drivers of no-shows.
- **Validation:** Performed **Cohort Profiling** to prove the top 10% risk decile perfectly mirrored the highest-risk behaviors found in EDA.

## Key Insights
- **The Wait-Time Trap:** Appointments booked 7+ days in advance (`MediumWait` & `LongWait`) make up only 35.8% of bookings but drive **57% of all no-shows**.
- **The Confirmation:** The model's Top Risk Decile captures a concentrated **38.5% true no-show rate** (a 1.91x lift over baseline), featuring a **4.38x over-representation** of Long-Wait patients.
- **The Same-Day Shield:** Same-day bookings act as a near-guarantee of patient attendance.

## Operational Strategy: Asymmetric Overbooking
Instead of aggressive daily double-booking (which burns out providers), the clinic should implement targeted **Asymmetric Overbooking**. By safely double-booking the high-risk `LongWait` slots with low-risk `Same-Day` patients, the clinic can mathematically absorb the no-show damage and protect revenue without bottlenecking the waiting room.

### Tech stack 
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- Xgboost
- Shap
