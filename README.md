# 🧠 Breast Cancer Prediction Web App

This project uses machine learning to predict whether a breast tumor is **benign or malignant**, based on 9 clinical features. Built with:

- 🧪 Scikit-learn
- 📊 SVC (Linear Kernel)
- 🌐 Streamlit (for web app)

 ##  breast-cancer-predictor/
├── app.py                   # Streamlit web app
├── main.ipynb              # Jupyter notebook with training code
├── svc_linear_model.pkl     # Trained model
├── breast_cancer.csv        # Dataset
├── requirements.txt         # Dependencies
├── README.md                # Project overview


## 📂 Files

- `main.ipynb`: Training notebook
- `app.py`: Streamlit app for interactive predictions
- `svc_linear_model.pkl`: Trained model
- `breast_cancer.csv`: Original dataset

## 🚀 Usage

1. Clone the repo:
    ```bash
    git clone https://github.com/your-username/breast-cancer-predictor.git
    cd breast-cancer-predictor
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

---

## 🧬 Sample Inputs

- Clump Thickness: 5
- Bare Nuclei: 1
- Mitoses: 1
(...and so on)

## ✅ Output

The app will tell you whether the tumor is likely **Benign (0)** or **Malignant (1)**.

---
