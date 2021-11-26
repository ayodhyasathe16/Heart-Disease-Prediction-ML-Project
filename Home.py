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



def show_home_page():
 
  df = pd.read_csv('heart.csv')

  x = df.drop(['target'], axis=1)
  y = df['target']
  sex_dictionary = {'Male':1, 'Female':0}
  fasting_dictionary = {'true':1, 'false':0}
  ex_dict = {'yes':1, 'no':0}
  
  st.title("Heart Disease Prediction")
  image = Image.open('img3.jpg')
  st.image(image, caption = 'This is a picture', use_column_width = True) 
  st.title('What is Heart Disease?')
  st.write("Heart Disease or Cardiovascular Disease (CVD) are a class of disease that involves the heart and blood vessels. Cardiovascular Disease includes coronary artery disease (CAD) like angina and myocardinal infraction ( commonly known as the heart attack).")
  st.write("Heart disease describes a range of conditions that affect your heart. Heart diseases include: Blood vessel disease, such as coronary artery disease ,Heart rhythm problems (arrhythmias) ,Heart defects you're born with (congenital heart defects) ,Heart valve disease ,Disease of the heart muscle, Heart infection.")
  st.title("Symptoms of Heart Disease:")
  st.write("1.Chest pain, chest tightness, chest pressure and chest discomfort (angina)")
  st.write("\n")
  st.write("2.Shortness of breath.")
  st.write("\n")
  st.write("3.Pain, numbness, weakness or coldness in your legs or arms if the blood vessels in those parts of your body are narrowed.")
  st.write("\n")
  st.write("4.Pain in the neck, jaw, throat, upper abdomen or back.")
  st.title("Prevention of Heart Disease:")
  st.write("1. Avoid smoking and using tobacco products. The relationship between smoking and lung cancer is known, but smoking can also cause heart disease, stroke and other chronic lung diseases. Cigarette smoking may be to blame for one in five cardiovascular disease deaths. Smoking damages blood vessels and heart tissue, lowers good cholesterol (HDL), and contributes to high blood pressure. Smoking can also increase your risk for cancer of the bladder, throat and mouth, kidneys, cervix and pancreas, and is also linked to insulin resistance and diabetes. Smoking is the most preventable cause of premature death in the United States.")
  st.write("2. Be physically active every day.  Your heart is a muscle that needs to be worked regularly to stay strong and healthy. If you’re not burning calories, you’re storing them – as fat. Too much of this means higher triglycerides and LDL – both bad for your heart. At a minimum, 30 minutes of daily exercise can help prevent cardiovascular disease.")
  st.write("3. Eat a heart-healthy diet.  A healthy diet is one of the best ways to fight cardiovascular disease. A heart-healthy diet should include whole grains, low-fat dairy products, fish & skinless poultry, nuts and legumes and a variety of fruits and vegetables. A recent European study reported that eating eight servings of vegetables and fruits per day reduces the risk of heart disease by 22 percent. Eight servings sounds like a lot, but it’s not when you consider what a portion size really is: one small carrot, half a banana or one small apple. By incorporating a portion or two of vegetables and fruits into each meal or snack, you can easily reach this target.")  
  st.write("4. Keep a healthy weight.  Heart disease is higher in persons who are overweight or obese and can lead to heart attack and death. Carrying extra weight can raise your blood pressure, elevate your triglycerides, decrease HDL (‘good’) cholesterol, and put you at risk for other serious conditions, like diabetes and cancer. To keep your weight down, be mindful about diet and exercise. If you need help, speak with your doctor or consult a nutritionist.")
   

 


