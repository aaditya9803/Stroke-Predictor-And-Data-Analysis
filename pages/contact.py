import streamlit as st

def show_contact():
    st.title('Contact and Contents')
    st.header(" ")
    st.header("1. Contents")
    st.code("""


        |
        |------ Home: Stroke Predictor
        |
        |
        |------ Cont: Contact and Contents
        |        |------ 1. Contents
        |        |------ 2. Contact
        |
        |
        |------ Chatbot
        |
        |
        |------ Info: Information about the dataset
        |        |------ 1. Data Analysis on people who had a stroke
        |        |        |------ 1.1. Gender
        |        |        |------ 1.2. Hypertension
        |        |        |------ 1.3. Marital Status
        |        |        |------ 1.4. Residence Type
        |        |        |------ 1.5. Heart Disease
        |        |        |------ 1.6. Work Type
        |        |        |------ 1.7. Smoking Status
        |        |        |------ 1.8. BMI Distribution
        |        |        |------ 1.9. Age Distribution
        |        |        |------ 1.10. Average Glucose Level Distribution
        |        |
        |        |------ 2. Comparison between people who had a stroke and those who did not
        |        |        |------ 2.1. Gender
        |        |        |------ 2.2. Hypertension
        |        |        |------ 2.3. Marital Status
        |        |        |------ 2.4. Residence Type
        |        |        |------ 2.5. Heart Disease
        |        |        |------ 2.6. Work Type
        |        |        |------ 2.7. Smoking Status
        |        |        |------ 2.8. Age Distribution
        |        |        |------ 2.9. Average Glucose Level Distribution
        |        |        |------ 2.10. BMI Distribution
        |        |
        |        |------ 3. Analysis with 30% fake data
        |                 |------ 3.1. Gender
        |                 |------ 3.2. Hypertension
        |                 |------ 3.3. Marital Status
        |                 |------ 3.4. Residence Type
        |                 |------ 3.5. Heart Disease
        |                 |------ 3.6. Work Type
        |                 |------ 3.7. Smoking Status
        |                 |------ 3.8. Age Distribution
        |                 |------ 3.9. Average Glucose Level Distribution
        |                 |------ 3.10. BMI Distribution
        |
        |
        |
        |------ Pre: Preprocessing, ML Models, and Effects of Fake Data
        |        |
        |        |------ 1. Preprocessing
        |        |        |------ 1.1. Null Values
        |        |        |------ 1.2. Label Encoder
        |        |        |------ 1.3. Oversampling/Undersampling
        |        |
        |        |------ 2. Machine Learning Models
        |        |        |------ 2.1. Support Vector Machine
        |        |        |        |------ 2.1.1 Cross Fold Method
        |        |        |        |------ 2.1.2 Test-Train Split Method
        |        |        |------ 2.2. XGBoost
        |        |                 |------ 2.2.1 Cross Fold Method
        |        |                 |------ 2.2.2 Test-Train Split Method
        |        |                 |------ 2.2.3 Testing the Final model with half of the dataset
        |        |                 |------ 2.2.4 Testing the Final model with only Stroke dataset (Where stroke==1)
        |        |
        |        |------ 3. Fake Data
        |                 |------ 3.1 Fake Data Generator
        |                 |------ 3.2 Effects of Fake Data on the Model Performance
        |                          |------ 3.2.1 Cross Fold Method with XGBoost
        |                          |------ 3.2.2 Test Train Split Method with XGBoost
        |

            
    """)
    st.subheader(" ")
    st.header("2. Contact")
    st.write('For any queries or feedback, please contact me at:')
    st.write('Email: aaditya.neupane@stud.th-deg.de')
