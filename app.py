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
from heart_predict import show_predict_page
from explore_page import show_explore_page
from Home import show_home_page


df = pd.read_csv('heart.csv')

x = df.drop(['target'], axis=1)
y = df['target']


sex_dictionary = {'Male':1, 'Female':0}
fasting_dictionary = {'true':1, 'false':0}
ex_dict = {'yes':1, 'no':0}

page = st.sidebar.selectbox("Explore Or Predict", ("Home","Predict", "Explore"))

if page == "Home":
    show_home_page()
elif page == "Predict":
    show_predict_page()
else:
    show_explore_page()