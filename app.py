"""
Riverbank Adaptation Prediction Web Application
Minimal deployment for model predictions
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Page configuration
st.set_page_config(
    page_title="Riverbank Adaptation Predictor",
    page_icon="🌊",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2c3e50;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .prediction-box {
        padding: 2rem;
        border-radius: 10px;
        margin-top: 2rem;
        text-align: center;
    }
    .adaptive {
        background-color: #d4edda;
        border: 2px solid #28a745;
    }
    .moderately-adaptive {
        background-color: #fff3cd;
        border: 2px solid #ffc107;
    }
    .non-adaptive {
        background-color: #f8d7da;
        border: 2px solid #dc3545;
    }
    .prediction-label {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
    .confidence-text {
        font-size: 1.2rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model_components():
    """Load all model components"""
    try:
        model = joblib.load('best_model.pkl')
        scaler = joblib.load('scaler.pkl')
        label_encoders = joblib.load('label_encoders.pkl')
        target_encoder = joblib.load('target_encoder.pkl')
        metadata = joblib.load('model_metadata.pkl')
        return model, scaler, label_encoders, target_encoder, metadata
    except FileNotFoundError:
        st.error("⚠️ Model files not found! Please run 'train_and_save_model.py' first.")
        st.stop()

# Load model components
model, scaler, label_encoders, target_encoder, metadata = load_model_components()

# Title
st.markdown('<div class="main-header">🌊 Riverbank Adaptation Prediction System</div>', unsafe_allow_html=True)
st.markdown("---")

# Sidebar with model info
with st.sidebar:
    st.markdown("### 📊 Model Information")
    st.write(f"**Model Type:** {metadata['model_name']}")
    st.write(f"**Accuracy:** {metadata['accuracy']*100:.2f}%")
    st.write(f"**F1-Score:** {metadata['f1_score']:.4f}")
    st.markdown("---")
    st.markdown("### 📝 Instructions")
    st.write("1. Fill in all input fields")
    st.write("2. Click 'Predict Adaptation Category'")
    st.write("3. View the prediction result")
    st.markdown("---")
    st.markdown("### 🎯 Prediction Categories")
    st.success("**Highly Adaptive** - Well prepared")
    st.warning("**Moderately Adaptive** - Some preparation")
    st.error("**Non-Adaptive** - Needs attention")

# Create input form
st.markdown('<div class="sub-header">Enter Household Information</div>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 👤 Demographics")
    union = st.text_input("Union Name", value="Kachua")
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=18, max_value=100, value=40)
    education = st.selectbox("Education Level", 
                            ["Not Educated", "Partially Educated", "Educated"])
    monthly_income = st.number_input("Monthly Income (BDT)", min_value=0, max_value=100000, value=7000)
    family_size = st.number_input("Family Size", min_value=1, max_value=20, value=5)

with col2:
    st.markdown("#### 🏠 Housing & Land")
    housing_type = st.selectbox("Housing Type", ["Temporary", "Semi-Permanent", "Permanent"])
    land_ownership = st.selectbox("Land Ownership", ["Yes", "No"])
    
    st.markdown("#### 🌊 Erosion Experience")
    previous_erosion = st.selectbox("Previous Erosion Experience", ["Yes", "No"])
    distance_from_river = st.number_input("Distance from River (meters)", 
                                         min_value=0, max_value=1000, value=150)
    relocation_history = st.selectbox("Relocation History", ["Yes", "No"])
    infrastructure_loss = st.selectbox("Infrastructure Loss", ["Yes", "No"])

with col3:
    st.markdown("#### 🛡️ Adaptation Measures")
    access_to_warning = st.selectbox("Access to Warning System", ["Yes", "No"])
    govt_assistance = st.selectbox("Government/NGO Assistance", ["Yes", "No"])
    has_protection = st.selectbox("Has Protection System", ["Yes", "No"])
    income_diversification = st.selectbox("Income Diversification", ["Yes", "No"])
    employment_status = st.selectbox("Employment Status", ["Employed", "Not Employed"])
    community_adaptation = st.selectbox("Involved in Community Adaptation", ["Yes", "No"])
    awareness_level = st.selectbox("Awareness Level", ["Low", "Moderate", "High"])

# Additional calculated indices
st.markdown('<div class="sub-header">Vulnerability Indices (Optional - Auto-calculated if left at default)</div>', unsafe_allow_html=True)

col4, col5, col6, col7 = st.columns(4)
with col4:
    distance_score = st.number_input("Distance Score", min_value=0.0, max_value=1.0, value=0.85, step=0.01)
with col5:
    eii = st.number_input("EII (Exposure Index)", min_value=0.0, max_value=1.0, value=0.65, step=0.01)
with col6:
    asi = st.number_input("ASI (Adaptive Sensitivity)", min_value=0.0, max_value=1.0, value=0.50, step=0.01)
with col7:
    sri = st.number_input("SRI (Socio-economic Resilience)", min_value=0.0, max_value=1.0, value=0.48, step=0.01)

iss = st.number_input("ISS (Institutional Support Score)", min_value=0.0, max_value=1.0, value=0.33, step=0.01)

# Prediction button
st.markdown("---")
if st.button("🔮 Predict Adaptation Category", type="primary", use_container_width=True):
    try:
        # Prepare input data
        input_data = {
            'Gender': gender,
            'Age': age,
            'Education_Level': education,
            'Monthly_Income': monthly_income,
            'Family_Size': family_size,
            'Housing_Type': housing_type,
            'Land_Ownership': land_ownership,
            'Previous_Erosion_Experience': previous_erosion,
            'Distance_from_River': distance_from_river,
            'Access_to_Warning': access_to_warning,
            'Relocation_History': relocation_history,
            'Govt_or_NGO_Assistance': govt_assistance,
            'Has_Protection_System': has_protection,
            'Infrastructure_Loss': infrastructure_loss,
            'Income_Diversification': income_diversification,
            'Employment_Status': employment_status,
            'Involved_in_Community_Adaptation': community_adaptation,
            'Awareness_Level': awareness_level,
            'Distance_score': distance_score,
            'EII': eii,
            'ASI': asi,
            'SRI': sri,
            'ISS': iss
        }
        
        # Create DataFrame
        input_df = pd.DataFrame([input_data])
        
        # Encode categorical variables
        for col in metadata['categorical_columns']:
            if col in input_df.columns:
                input_df[col] = label_encoders[col].transform(input_df[col])
        
        # Scale features
        input_scaled = scaler.transform(input_df)
        
        # Make prediction
        prediction_encoded = model.predict(input_scaled)[0]
        prediction_proba = model.predict_proba(input_scaled)[0]
        
        # Decode prediction
        prediction = target_encoder.inverse_transform([prediction_encoded])[0]
        confidence = prediction_proba[prediction_encoded] * 100
        
        # Display result with styling
        st.markdown("---")
        
        # Determine CSS class based on prediction
        if prediction == "Highly Adaptive":
            box_class = "adaptive"
            emoji = "✅"
        elif prediction == "Moderately Adaptive":
            box_class = "moderately-adaptive"
            emoji = "⚠️"
        else:
            box_class = "non-adaptive"
            emoji = "❌"
        
        st.markdown(f'''
        <div class="prediction-box {box_class}">
            <div class="prediction-label">{emoji} {prediction}</div>
            <div class="confidence-text">Confidence: {confidence:.1f}%</div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Show probability distribution
        st.markdown("### 📊 Probability Distribution")
        prob_df = pd.DataFrame({
            'Category': metadata['target_classes'],
            'Probability': prediction_proba * 100
        })
        prob_df = prob_df.sort_values('Probability', ascending=False)
        
        st.bar_chart(prob_df.set_index('Category'))
        
        # Recommendations based on prediction
        st.markdown("### 💡 Recommendations")
        
        if prediction == "Non-Adaptive":
            st.error("""
            **Immediate Actions Needed:**
            - Seek government/NGO assistance programs
            - Participate in community adaptation initiatives
            - Develop income diversification strategies
            - Install early warning systems
            - Consider housing improvements
            """)
        elif prediction == "Moderately Adaptive":
            st.warning("""
            **Suggested Improvements:**
            - Strengthen existing protection systems
            - Increase community involvement
            - Explore additional income sources
            - Enhance disaster preparedness
            """)
        else:
            st.success("""
            **Continue Best Practices:**
            - Maintain current adaptation strategies
            - Share knowledge with community
            - Stay updated on early warning systems
            - Keep monitoring river conditions
            """)
        
    except Exception as e:
        st.error(f"❌ Error making prediction: {str(e)}")
        st.exception(e)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>Riverbank Adaptation Prediction System | Powered by Machine Learning</p>
    <p style='font-size: 0.8rem;'>This tool helps assess household adaptation capacity to riverbank erosion</p>
</div>
""", unsafe_allow_html=True)
