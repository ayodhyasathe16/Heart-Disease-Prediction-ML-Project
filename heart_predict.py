import pickle
import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns



def show_predict_page():
 
  df = pd.read_csv('heart.csv')

  x = df.drop(['target'], axis=1)
  y = df['target']
  sex_dictionary = {'Male':1, 'Female':0}
  fasting_dictionary = {'true':1, 'false':0}
  ex_dict = {'yes':1, 'no':0}
  
  st.title("Heart Disease Prediction")
  image = Image.open('img.jpg')
  st.image(image, caption = 'This is a picture', use_column_width = True) 
  st.header('Enter Patient Data')

  

  def user_report():
    age = (
        29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67
        ,68,69,70,71,72,73,74,75,76,77
    )
    sex =  (1,0)
    cp  =  (1,2,3,4)
    fbs = (1,0)
    exng  =  (1,0)
    slp = (1,2,3)
    age = st.selectbox("Age", age)
    sex = st.selectbox("Gender(1 = Male, 0 = Female)", sex)
    cp = st.selectbox("Chest Pain Type (1:typical angina, 2:atypical angina, 3:non-anginal pain, 4:asymptomatic)", cp)
    trtbps = st.slider('Resting Blood Pressure (in mm Hg on admission to the hospital)', 94,200, 120 )
    chol = st.slider('Serum Cholestrol in mg/dl',126, 564, 200)
    fbs = st.selectbox('fasting blood sugar > 120 mg/dl (True = 1, False=0)', fbs)
    restecg = st.slider('Resting electrocardiographic results (values 0,1,2)', 0,2, 0 )
    thalachh = st.slider('Maximum heart rate achieved', 71,202, 110 )
    exng = st.selectbox("exercise induced angina (1 = Yes, 0 = No)", exng)
    oldpeak = st.slider('oldpeak = ST depression induced by exercise relative to rest', 0,6, 2 )
    slp = st.selectbox('the slope of the peak exercise ST segment (Value 1: up sloping , Value 2: flat , Value 3: down sloping )', slp)
    caa = st.slider('number of major vessels (0-3) colored by flourosopy', 0, 4, 0)
    thall = st.slider('maximum heart rate achieved: 3 = normal; 6 = fixed defect; 7 = reversable defect', 0, 3, 0)



    user_report_data = {
      'age': age,
      'sex': sex,
      'cp': cp,
      'trtbps': trtbps,
      'chol': chol,
      'fbs': fbs,
      'restecg': restecg,
      'thalachh': thalachh,
      'exng': exng,
      'oldpeak': oldpeak,
      'slp': slp,
      'caa': caa,
      'thall': thall
    }
    report_data = pd.DataFrame(user_report_data, index=[0])
    return report_data
  
  user_data = user_report()
  ok = st.button("Submit")
  if ok:
    st.subheader('Patient Data')
    st.write(user_data)
    kn = KNeighborsClassifier()
    kn.fit(x, y) 
    user_result = kn.predict(user_data)
  
  # COLOR FUNCTION
    if user_result[0]==0:
      color = 'blue'
    else:
      color = 'red'

  

  # OUTPUT
    st.subheader('Your Report: ')
    output=''
    if user_result[0]==0:
      output = 'You are in Good Condition'
    else:
      output = 'You Have Heart Disease'
    st.title(output)
    




