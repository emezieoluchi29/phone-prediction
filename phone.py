import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import joblib

data = pd.read_csv('train.csv')
model = joblib.load('phone_models.pkl')

st.markdown("<h1 style = 'color: #0C2D57; text-align: center; font-family: helvetica'>C&K MOBILE PRICE PREDICTOR</h1>", unsafe_allow_html = True)
st.markdown("<h4 style = 'margin: -30px; color: #F11A7B; text-align: center; font-family: cursive '>Built By Emezie Oluchi</h4>", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html= True)

st.image('resources/phone_image.png', width= 200)

st.markdown("<h4 style = 'margin: -30px; color: green; text-align: center; font-family: helvetica '>Project Overview</h4>", unsafe_allow_html = True)

st.write("The goal of this project is to develop a predictive model that assesses different phone features and group the prices based on these features. By leveraging machine learning techniques, we aim to provide insights into the factors influencing price range based on features, empowering stakeholders to make informed decisions")

st.markdown("<br>", unsafe_allow_html= True)
st.dataframe(data, use_container_width= True)

st.sidebar.image('resources/pngwing.com (1).png', caption = 'Welcome Dear User')

ram = st.sidebar.number_input('ram')
battery_power = st.sidebar.number_input('battery_power',)
px_height = st.sidebar.number_input('px_height')
px_width = st.sidebar.number_input('px_width')
mobile_wt = st.sidebar.number_input('mobile_wt')
int_memory = st.sidebar.number_input('int_memory')
pc = st.sidebar.number_input('pc')

st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)
st.markdown("<br>", unsafe_allow_html= True)

st.markdown("<h4 style = 'margin: -30px; color: green; text-align: center; font-family: helvetica '>Input Variable</h4>", unsafe_allow_html = True)

inputs = pd.DataFrame()
inputs['ram'] = [ram]
inputs['battery_power'] = [battery_power]
inputs['px_height'] = [px_height]
inputs['px_width'] = [px_width]
inputs['mobile_wt'] = [mobile_wt]
inputs['int_memory'] = [int_memory]
inputs['pc'] = [pc]


st.dataframe(inputs, use_container_width= True)


pusher = st.button('Predict price_range')

# Model Prediction

if pusher:
    predicted = model.predict(inputs)
    if predicted[0]== 0:
        st.success(f'The range is {0-1000}')
      

    elif predicted[0]== 1:
        st.success(f'The range is {1001-1500}')
    
    elif predicted[0]== 2:
        st.success(f'The range is {1501-2500}')
        
  
   
    else: 
        st.error(f'The range is {2501-5000}')
