import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def show_explore_page():
    st.title("Heart Data Survey###")
    
    df = pd.read_csv("heart.csv")
    df = df[["age", "sex", "cp", "trestbps", "chol","fbs","restecg","thalach","exang","oldpeak","slope","ca", "thal","target"]]

    data = df["target"].value_counts()
    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal") 

    st.write("""#### Based on Survey toatal patient have heart disease(0) and not have heart disease(1) """)

    st.pyplot(fig1)
    
    st.write("""Line Chart """)
    st.line_chart(df)
    st.write("""Bar Chart """)
    st.bar_chart(df)
    st.write("""Area Chart """)
    st.area_chart(df)

    