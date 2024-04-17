import sys
import numpy as np    
import pandas as pd               
import plotly.express as px 
import streamlit as st 

# https://streamlit.io/components?category=charts
from streamlit_shap import st_shap
import time

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from category_encoders import OneHotEncoder

import shap

with st.sidebar:
    st.title('Page 3 ❄️')
    st.caption("This page showcases how to pre-build models that \
        you can quickly use to test performance and streamlit components") 
    
st.markdown("# Predict Your Data")
"""
Lets try out logistic regression!
"""

try:
    with st.form(key='confirm_variable_select'):
        file = st.session_state["uploaded_file"]
        file_columns = list(file.columns)
        print("file:", file)
        print("file cols:", list(file.columns))
        
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
            numerical_filter = st.multiselect("Select numerical X values", file_columns)
        with col2:
            categorical_filter = st.multiselect("Select categorical X values", file_columns)
        with col3:
            y_filter = st.selectbox("Select Y value", file_columns)

        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        with st.spinner("Training model..."):
            time.sleep(2) # simulate model training
            
            selected_cols = list(numerical_filter + categorical_filter)
            X = file[selected_cols]
            Y = file[y_filter]
            
            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
            
            ohe = OneHotEncoder(cols=categorical_filter)
            X_train = ohe.fit_transform(X_train)
            X_test = ohe.transform(X_test)
            
            scaler = StandardScaler()
            X_train.loc[:, numerical_filter] = scaler.fit_transform(X_train.loc[:, numerical_filter])
            X_test.loc[:, numerical_filter] = scaler.transform(X_test.loc[:, numerical_filter])
            
            log_reg = LogisticRegression()

            # Fit the model to the training data
            log_reg.fit(X_train, y_train)
            
            # Predict the outcomes for the testing data
            y_pred = log_reg.predict(X_test)

            # Evaluate the model's performance
            accuracy = accuracy_score(y_test, y_pred)
            
            explainer = shap.Explainer(
                log_reg, X_train, feature_names=X_train.columns
            )
            shap_values = explainer(X_test)
            st_shap(shap.plots.beeswarm(shap_values))
            
            print(log_reg.coef_)
            print(log_reg.coef_[0])
            st.write("Model Coefficients:")
            for i, col in enumerate(X_train.columns):
                st.write(col + ": " + str(log_reg.coef_[0][i]))
            
            st.write("Accuracy:", accuracy)
        
except:
    st.write("Please input data in the Main Page first!")
