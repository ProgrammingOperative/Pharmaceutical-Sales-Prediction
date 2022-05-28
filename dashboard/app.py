import streamlit as st
import pandas as pd
import utils
from PIL import Image


header = st.container()
dataset = st.container()
features = st.container()
trainingModel = st.container()


# Caching the data
@st.cache
def get_data(filename):
    user_data = pd.read_csv(filename)
    return user_data


with header:
    st.title("ROSSMAN PHARMACEUTICAL ")
    st.text("SALES AND CUSTOMER NUMBER PREDICTION")


with dataset:
    st.header("DATASET PREVIEW")
    # st.text("I created this version of the dataset from 10_academy's week 1 project dataset")
    train_store = get_data('data/train_store.csv')
    st.write(train_store.head(5))

    st.subheader('CORRELATION BETWEEN CUSTOMERS AND SALES')
    fig = utils.heatmap(train_store[['Sales', 'Customers']], title='Correlation Between Sales and Customers')
    # data_usage_distribution = pd.DataFrame(train_store['Total_UL_and_DL_(Bytes)'].value_counts()).head(50)
    # st.bar_chart(data_usage_distribution)
    image = Image.open('data/dashboard photo.PNG')
    st.image(image)


with features:
    st.header("IMPORTANT FEATURES FOR PREDICTION")
    # # Creating lists
    # st.markdown('* **First Feature**: The first feature that I created for better user analytics ')
    # st.markdown('* **Second Feature**: The first feature that I created for better user analytics ')
    image = Image.open('data/important features.PNG')
    st.image(image)

with trainingModel:
    st.header("PREDICT")

    #Create columns
    sel_col, disp_col = st.columns(2)
    sel_col.text_input('The following is a list of features you can work with')
    sel_col.write(train_store.columns)

    #Text Input
    input_feature = sel_col.text_input('Which feature would you like to work with', 'Open')



