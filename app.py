import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("svc_linear_model.pkl")

st.set_page_config(page_title="Breast Cancer Predictor", layout="centered")
st.title("🔬 Breast Cancer Cell Classifier")
st.write("This app predicts whether a breast tumor is **benign (0)** or **malignant (1)** using 9 cellular features.")

st.sidebar.header("🧪 Input Features")
st.sidebar.write("Adjust the sliders below to input test data.")

# Feature sliders with descriptions
feature_info = {
    "Clump Thickness": "Thickness of the clump of cells",
    "Uniformity of Cell Size": "Consistency in size of cells",
    "Uniformity of Cell Shape": "Consistency in shape of cells",
    "Marginal Adhesion": "How tightly cells stick to each other",
    "Single Epithelial Cell Size": "Size of individual epithelial cells",
    "Bare Nuclei": "Presence of bare nuclei",
    "Bland Chromatin": "Texture of the chromatin in nucleus",
    "Normal Nucleoli": "Appearance of nucleoli inside cells",
    "Mitoses": "Rate of cell division (mitosis)"
}

inputs = []
for feature, description in feature_info.items():
    value = st.sidebar.slider(f"{feature}", 1, 10, 5, help=description)
    inputs.append(value)

if st.sidebar.button("🔍 Predict"):
    data = np.array([inputs])
    prediction = model.predict(data)[0]

    # You can also add probabilities if your model supports it
    st.subheader("📊 Prediction Result")
    if prediction == 0:
        st.success("✅ The tumor is likely **Benign (0)** 🟢")
    else:
        st.error("⚠️ The tumor is likely **Malignant (1)** 🔴")
        
    # Optional: Confidence from model if supported
    if hasattr(model, "predict_proba"):
        probs = model.predict_proba(data)
        st.write("Confidence Score:")
        st.progress(float(np.max(probs)))
        st.code(f"{np.max(probs)*100:.2f}%")

else:
    st.info("Set feature values in the sidebar and click **Predict** to see the result.")
