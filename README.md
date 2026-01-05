# 🌊 Riverbank Adaptation Prediction System

A minimal web deployment for predicting household adaptation capacity to riverbank erosion using machine learning.

## 📋 Overview

This web application allows users to input household characteristics and receive predictions about their adaptation category:
- **Highly Adaptive** - Well prepared for erosion
- **Moderately Adaptive** - Some preparation measures in place
- **Non-Adaptive** - Needs immediate attention

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```powershell
   cd "C:\Users\Yousuf Rayhan Emon\OneDrive\Documents\NTK"
   ```

2. **Install required packages**
   ```powershell
   pip install -r requirements.txt
   ```

### Training the Model

Before running the web app for the first time, you need to train and save the model:

```powershell
python train_and_save_model.py
```

This will:
- Load the `riverbank_with_indices.csv` dataset
- Train multiple models (Random Forest, XGBoost, Gradient Boosting)
- Select the best performing model
- Save the model and preprocessing objects as `.pkl` files

**Expected output files:**
- `best_model.pkl` - Trained model
- `scaler.pkl` - Feature scaler
- `label_encoders.pkl` - Categorical encoders
- `target_encoder.pkl` - Target label encoder
- `model_metadata.pkl` - Model metadata

### Running the Web Application

Once the model is trained, launch the web app:

```powershell
streamlit run app.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

## 🖥️ Using the Web Interface

1. **Fill in the input fields:**
   - Demographics (Gender, Age, Education, Income, Family Size)
   - Housing & Land information
   - Erosion experience details
   - Adaptation measures
   - Vulnerability indices (can use default values)

2. **Click "Predict Adaptation Category"**

3. **View Results:**
   - Prediction category with confidence score
   - Probability distribution across all categories
   - Personalized recommendations

## 📁 Project Structure

```
NTK/
├── app.py                          # Streamlit web application
├── train_and_save_model.py         # Model training script
├── requirements.txt                # Python dependencies
├── riverbank_with_indices.csv      # Dataset
├── Complete_Analysis_Colab_FInal.ipynb  # Original analysis notebook
│
├── best_model.pkl                  # Trained model (generated)
├── scaler.pkl                      # Feature scaler (generated)
├── label_encoders.pkl              # Encoders (generated)
├── target_encoder.pkl              # Target encoder (generated)
└── model_metadata.pkl              # Metadata (generated)
```

## 🌐 Deployment Options

### Local Deployment (Current Setup)
- Run on your computer using the steps above
- Access at `http://localhost:8501`
- Perfect for testing and demonstrations

### Cloud Deployment Options

#### Option 1: Streamlit Community Cloud (Free)
1. Create a GitHub repository and push your code
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Deploy with one click!

#### Option 2: Heroku
1. Create a `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT
   ```
2. Deploy using Heroku CLI or GitHub integration

#### Option 3: AWS/Azure/Google Cloud
- Use container services (Docker)
- Deploy as a web service
- More control but requires cloud knowledge

## 📊 Model Features

The model uses 23 input features:

**Demographics:**
- Gender, Age, Education Level, Monthly Income, Family Size

**Housing & Land:**
- Housing Type, Land Ownership

**Erosion Experience:**
- Previous Erosion Experience, Distance from River, Relocation History, Infrastructure Loss

**Adaptation Measures:**
- Access to Warning, Government/NGO Assistance, Has Protection System
- Income Diversification, Employment Status, Community Involvement, Awareness Level

**Vulnerability Indices:**
- Distance Score, EII, ASI, SRI, ISS

## 🔧 Troubleshooting

### Model files not found
**Error:** "Model files not found! Please run 'train_and_save_model.py' first."
**Solution:** Run the training script first:
```powershell
python train_and_save_model.py
```

### Import errors
**Error:** "ModuleNotFoundError: No module named 'streamlit'"
**Solution:** Install requirements:
```powershell
pip install -r requirements.txt
```

### Port already in use
**Error:** "Port 8501 is already in use"
**Solution:** Use a different port:
```powershell
streamlit run app.py --server.port 8502
```

## 📈 Model Performance

The system automatically selects the best performing model based on:
- Accuracy (primary metric)
- F1-Score (secondary metric)

Typical performance:
- Accuracy: >90%
- F1-Score: >0.85

## 🤝 Contributing

To modify the model or add features:

1. **Update training script** (`train_and_save_model.py`)
2. **Retrain the model**
3. **Update web app** (`app.py`) if adding new input fields
4. **Test thoroughly** before deployment

## 📝 License

This project is for academic/research purposes.

## 👥 Contact

For questions or issues, contact the development team.

---

**Built with:**
- Python 3.8+
- Streamlit
- Scikit-learn
- XGBoost
- Pandas & NumPy

**Last Updated:** January 2026
