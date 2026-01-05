"""
System Architecture & Workflow Diagram
"""

SYSTEM_ARCHITECTURE = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                   RIVERBANK ADAPTATION PREDICTION SYSTEM                  ║
║                         System Architecture                               ║
╚═══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│                          1. DATA LAYER                                  │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────┐
    │  riverbank_with_indices.csv      │
    │  ────────────────────────────    │
    │  • 2968 households               │
    │  • 25 features                   │
    │  • 3 target classes              │
    └──────────────┬───────────────────┘
                   │
                   ▼

┌─────────────────────────────────────────────────────────────────────────┐
│                     2. MODEL TRAINING LAYER                             │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────┐
    │  train_and_save_model.py         │
    │  ────────────────────────────    │
    │  ┌────────────────────────────┐  │
    │  │ 1. Load & Preprocess Data  │  │
    │  └──────────┬─────────────────┘  │
    │             ▼                     │
    │  ┌────────────────────────────┐  │
    │  │ 2. Encode Categorical      │  │
    │  └──────────┬─────────────────┘  │
    │             ▼                     │
    │  ┌────────────────────────────┐  │
    │  │ 3. Train Multiple Models   │  │
    │  │    • Random Forest         │  │
    │  │    • XGBoost               │  │
    │  │    • Gradient Boosting     │  │
    │  └──────────┬─────────────────┘  │
    │             ▼                     │
    │  ┌────────────────────────────┐  │
    │  │ 4. Select Best Model       │  │
    │  └──────────┬─────────────────┘  │
    │             ▼                     │
    │  ┌────────────────────────────┐  │
    │  │ 5. Save Model & Objects    │  │
    │  └──────────┬─────────────────┘  │
    └─────────────┼─────────────────────┘
                  │
                  ▼
    ┌─────────────────────────────────┐
    │  Saved Model Files (.pkl)       │
    │  ───────────────────────────    │
    │  • best_model.pkl               │
    │  • scaler.pkl                   │
    │  • label_encoders.pkl           │
    │  • target_encoder.pkl           │
    │  • model_metadata.pkl           │
    └──────────────┬──────────────────┘
                   │
                   ▼

┌─────────────────────────────────────────────────────────────────────────┐
│                      3. APPLICATION LAYER                               │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────────────────────┐
    │         app.py                   │
    │  ────────────────────────────    │
    │  Streamlit Web Application       │
    │                                  │
    │  ┌────────────────────────────┐  │
    │  │   User Interface           │  │
    │  │   ──────────────           │  │
    │  │   • Input Form (23 fields) │  │
    │  │   • Predict Button         │  │
    │  │   • Results Display        │  │
    │  └────────────────────────────┘  │
    │                                  │
    │  ┌────────────────────────────┐  │
    │  │   Prediction Engine        │  │
    │  │   ────────────────         │  │
    │  │   • Load saved models      │  │
    │  │   • Preprocess inputs      │  │
    │  │   • Generate predictions   │  │
    │  │   • Calculate confidence   │  │
    │  └────────────────────────────┘  │
    │                                  │
    │  ┌────────────────────────────┐  │
    │  │   Results Rendering        │  │
    │  │   ────────────────         │  │
    │  │   • Color-coded display    │  │
    │  │   • Probability charts     │  │
    │  │   • Recommendations        │  │
    │  └────────────────────────────┘  │
    └──────────────┬───────────────────┘
                   │
                   ▼

┌─────────────────────────────────────────────────────────────────────────┐
│                       4. DEPLOYMENT LAYER                               │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────┐         ┌──────────────────┐
    │  Local Server    │         │  Cloud Platform  │
    │  ──────────────  │         │  ──────────────  │
    │  localhost:8501  │   OR    │  Streamlit Cloud │
    │                  │         │  share.streamlit │
    └────────┬─────────┘         └────────┬─────────┘
             │                            │
             └──────────┬─────────────────┘
                        ▼

┌─────────────────────────────────────────────────────────────────────────┐
│                          5. USER LAYER                                  │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │  Supervisor  │  │  Researchers │  │ Stakeholders │
    │              │  │              │  │              │
    │  • Demo      │  │  • Analysis  │  │  • Planning  │
    │  • Evaluate  │  │  • Testing   │  │  • Policy    │
    └──────────────┘  └──────────────┘  └──────────────┘
"""

WORKFLOW_DIAGRAM = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                           USER WORKFLOW                                   ║
╚═══════════════════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 1: INITIAL SETUP (One-time, 2-3 minutes)                         │
└─────────────────────────────────────────────────────────────────────────┘

    START
      │
      ▼
    ┌────────────────────────────┐
    │ Double-click               │
    │ start_app.bat              │
    └──────────┬─────────────────┘
               │
               ▼
    ┌────────────────────────────┐
    │ Script checks for          │
    │ model files                │
    └──────────┬─────────────────┘
               │
         ┌─────┴─────┐
         │           │
      No │           │ Yes
         │           │
         ▼           ▼
    ┌────────┐  ┌────────┐
    │ Train  │  │ Skip   │
    │ Model  │  │ to App │
    └───┬────┘  └───┬────┘
        │           │
        └─────┬─────┘
              ▼
    ┌────────────────────────────┐
    │ Launch Streamlit App       │
    └──────────┬─────────────────┘
               │
               ▼
    ┌────────────────────────────┐
    │ Browser Opens              │
    │ App Ready!                 │
    └────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 2: MAKING PREDICTIONS (30 seconds per prediction)                │
└─────────────────────────────────────────────────────────────────────────┘

    USER ARRIVES
      │
      ▼
    ┌────────────────────────────┐
    │ View Clean Interface       │
    │ • Sidebar: Model Info      │
    │ • Main: Input Form         │
    └──────────┬─────────────────┘
               │
               ▼
    ┌────────────────────────────┐
    │ Fill Input Fields          │
    │ ─────────────────          │
    │ Demographics:              │
    │  → Gender                  │
    │  → Age                     │
    │  → Education               │
    │  → Income                  │
    │  → Family Size             │
    │                            │
    │ Housing:                   │
    │  → Type                    │
    │  → Land Ownership          │
    │                            │
    │ Erosion:                   │
    │  → Previous Experience     │
    │  → Distance from River     │
    │  → Relocation History      │
    │                            │
    │ Adaptation:                │
    │  → Warning System          │
    │  → Govt Assistance         │
    │  → Protection System       │
    │  → Income Diversification  │
    │  → Employment              │
    │  → Community Involvement   │
    │  → Awareness Level         │
    │                            │
    │ Indices:                   │
    │  → Distance Score          │
    │  → EII, ASI, SRI, ISS      │
    └──────────┬─────────────────┘
               │
               ▼
    ┌────────────────────────────┐
    │ Click Predict Button       │
    │ 🔮 Predict Adaptation      │
    └──────────┬─────────────────┘
               │
               ▼
    ╔════════════════════════════╗
    ║  PROCESSING (< 1 second)   ║
    ╠════════════════════════════╣
    ║  1. Encode inputs          ║
    ║  2. Scale features         ║
    ║  3. Load model             ║
    ║  4. Generate prediction    ║
    ║  5. Calculate probabilities║
    ╚════════════════════════════╝
               │
               ▼
    ┌────────────────────────────┐
    │ Display Results            │
    │ ───────────────            │
    │                            │
    │ ╔════════════════════════╗ │
    │ ║ PREDICTION CATEGORY    ║ │
    │ ║ (Color-Coded Box)      ║ │
    │ ║ Confidence: XX.X%      ║ │
    │ ╚════════════════════════╝ │
    │                            │
    │ 📊 Probability Chart       │
    │  Highly Adaptive:    45%   │
    │  Moderately Adaptive: 35%  │
    │  Non-Adaptive:       20%   │
    │                            │
    │ 💡 Recommendations         │
    │  • Specific actions        │
    │  • Based on category       │
    │  • Actionable steps        │
    └──────────┬─────────────────┘
               │
          ┌────┴────┐
          │         │
          ▼         ▼
    ┌──────────┐ ┌──────────┐
    │ Try      │ │ Share    │
    │ Another  │ │ Results  │
    └────┬─────┘ └──────────┘
         │
         └──► Loop back to fill form

┌─────────────────────────────────────────────────────────────────────────┐
│  STEP 3: INTERPRETATION                                                 │
└─────────────────────────────────────────────────────────────────────────┘

    Result Categories:
    
    ┌────────────────────────────────────────────┐
    │ ✅ HIGHLY ADAPTIVE                         │
    │ ────────────────────────────────────       │
    │ Meaning: Well-prepared household           │
    │ Actions: Maintain current strategies       │
    │ Risk Level: LOW                            │
    └────────────────────────────────────────────┘
    
    ┌────────────────────────────────────────────┐
    │ ⚠️ MODERATELY ADAPTIVE                     │
    │ ────────────────────────────────────       │
    │ Meaning: Some preparation in place         │
    │ Actions: Strengthen existing measures      │
    │ Risk Level: MEDIUM                         │
    └────────────────────────────────────────────┘
    
    ┌────────────────────────────────────────────┐
    │ ❌ NON-ADAPTIVE                            │
    │ ────────────────────────────────────       │
    │ Meaning: Needs immediate attention         │
    │ Actions: Seek assistance, build capacity   │
    │ Risk Level: HIGH                           │
    └────────────────────────────────────────────┘
"""

DATA_FLOW = """
╔═══════════════════════════════════════════════════════════════════════════╗
║                           DATA FLOW DIAGRAM                               ║
╚═══════════════════════════════════════════════════════════════════════════╝

Input Data (User)
    │
    │  23 Features:
    │  • Gender, Age, Education, Income, Family
    │  • Housing, Land
    │  • Erosion experience, Distance
    │  • Warning, Assistance, Protection
    │  • Employment, Community, Awareness
    │  • Indices (Distance Score, EII, ASI, SRI, ISS)
    │
    ▼
┌───────────────────────────────────────┐
│  Data Preprocessing                   │
│  ──────────────────                   │
│  • Convert to DataFrame               │
│  • Encode categorical variables       │
│  •   Gender: M/F → 0/1                │
│  •   Education: encode levels         │
│  •   Housing: encode types            │
│  •   Yes/No: → 1/0                    │
│  • Keep numeric as-is                 │
└──────────────┬────────────────────────┘
               │
               ▼
┌───────────────────────────────────────┐
│  Feature Scaling                      │
│  ───────────────                      │
│  • Apply StandardScaler               │
│  • Normalize all features             │
│  • Same scale as training data        │
└──────────────┬────────────────────────┘
               │
               ▼
┌───────────────────────────────────────┐
│  Model Prediction                     │
│  ────────────────                     │
│  • Load best_model.pkl                │
│  • Input scaled features              │
│  • Generate prediction                │
│  • Calculate probabilities            │
│  •   P(Highly Adaptive)               │
│  •   P(Moderately Adaptive)           │
│  •   P(Non-Adaptive)                  │
└──────────────┬────────────────────────┘
               │
               ▼
┌───────────────────────────────────────┐
│  Post-Processing                      │
│  ───────────────                      │
│  • Decode prediction to label         │
│  • Convert probabilities to %         │
│  • Determine confidence               │
│  • Select recommendation template     │
└──────────────┬────────────────────────┘
               │
               ▼
Output Results (Display)
    │
    │  • Prediction Category
    │  • Confidence Score
    │  • Probability Distribution
    │  • Personalized Recommendations
    │
    ▼
USER SEES RESULTS
"""

if __name__ == "__main__":
    print(SYSTEM_ARCHITECTURE)
    print("\n\n")
    print(WORKFLOW_DIAGRAM)
    print("\n\n")
    print(DATA_FLOW)
