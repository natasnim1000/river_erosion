"""
Train and save the best model for deployment
This script trains multiple models and saves the best performing one
"""

import pandas as pd
import numpy as np
import joblib
import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from xgboost import XGBClassifier

RANDOM_STATE = 42
np.random.seed(RANDOM_STATE)

print("Loading dataset...")
df = pd.read_csv('riverbank_with_indices.csv')

# Target variable
y = df['Adaptation_Category']

# Features to use
feature_cols = ['Gender', 'Age', 'Education_Level', 'Monthly_Income', 'Family_Size',
                'Housing_Type', 'Land_Ownership', 'Previous_Erosion_Experience',
                'Distance_from_River', 'Access_to_Warning', 'Relocation_History',
                'Govt_or_NGO_Assistance', 'Has_Protection_System', 'Infrastructure_Loss',
                'Income_Diversification', 'Employment_Status', 'Involved_in_Community_Adaptation',
                'Awareness_Level', 'Distance_score', 'EII', 'ASI', 'SRI', 'ISS']

X = df[feature_cols]

print(f"Dataset shape: {X.shape}")
print(f"Target classes: {y.unique()}")

# Encode categorical variables
label_encoders = {}
categorical_cols = X.select_dtypes(include=['object']).columns

for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le

# Encode target
target_encoder = LabelEncoder()
y_encoded = target_encoder.fit_transform(y)

print(f"\nCategorical columns encoded: {list(categorical_cols)}")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=RANDOM_STATE, stratify=y_encoded
)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print(f"\nTrain set: {X_train_scaled.shape}")
print(f"Test set: {X_test_scaled.shape}")

# Define models
models = {
    'RandomForest': RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=RANDOM_STATE,
        n_jobs=-1
    ),
    'XGBoost': XGBClassifier(
        n_estimators=200,
        max_depth=8,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=RANDOM_STATE,
        eval_metric='mlogloss'
    ),
    'GradientBoosting': GradientBoostingClassifier(
        n_estimators=200,
        learning_rate=0.1,
        max_depth=5,
        min_samples_split=5,
        random_state=RANDOM_STATE
    )
}

results = []

print("\n" + "="*80)
print("TRAINING MODELS")
print("="*80)

for model_name, model in models.items():
    print(f"\nTraining {model_name}...")
    
    model.fit(X_train_scaled, y_train)
    
    # Predictions
    y_pred = model.predict(X_test_scaled)
    
    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='macro')
    
    print(f"  Test Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")
    print(f"  Test F1-Score: {f1:.4f}")
    
    results.append({
        'model_name': model_name,
        'model': model,
        'accuracy': accuracy,
        'f1_score': f1
    })

# Select best model
best_result = max(results, key=lambda x: x['accuracy'])
best_model = best_result['model']
best_model_name = best_result['model_name']

print("\n" + "="*80)
print(f"BEST MODEL: {best_model_name}")
print(f"Accuracy: {best_result['accuracy']:.4f} ({best_result['accuracy']*100:.2f}%)")
print(f"F1-Score: {best_result['f1_score']:.4f}")
print("="*80)

# Save the best model and preprocessing objects
print("\nSaving model and preprocessing objects...")

joblib.dump(best_model, 'best_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
joblib.dump(label_encoders, 'label_encoders.pkl')
joblib.dump(target_encoder, 'target_encoder.pkl')

# Save feature names and metadata
metadata = {
    'feature_columns': feature_cols,
    'categorical_columns': list(categorical_cols),
    'model_name': best_model_name,
    'accuracy': best_result['accuracy'],
    'f1_score': best_result['f1_score'],
    'target_classes': list(target_encoder.classes_)
}
joblib.dump(metadata, 'model_metadata.pkl')

print("\nSaved files:")
print("  - best_model.pkl")
print("  - scaler.pkl")
print("  - label_encoders.pkl")
print("  - target_encoder.pkl")
print("  - model_metadata.pkl")

print("\n✓ Model training and saving complete!")
