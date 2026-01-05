@echo off
echo ==========================================
echo Riverbank Adaptation Prediction System
echo ==========================================
echo.

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if model files exist
if not exist "best_model.pkl" (
    echo Model files not found!
    echo Training model first...
    echo.
    python train_and_save_model.py
    echo.
    if errorlevel 1 (
        echo Error training model!
        pause
        exit /b 1
    )
    echo Model training completed successfully!
    echo.
)

echo Starting web application...
echo.
echo The app will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.
streamlit run app.py
