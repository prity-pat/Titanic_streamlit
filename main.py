import streamlit as st
import pickle

st.set_page_config(page_title= 'Titanic survival prediction')

st.title('Titanic survival Prediction')
st.sidebar.markdown('Enter passenger details to predict survival chance')

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

pclass = st.sidebar.selectbox('passenger class',[1,2,3]) 
age = st.sidebar.slider('Age in years',0,60,30)
sex = st.sidebar.selectbox('Select gender 0=Female,1 = Male', [0,1]) 
fare = st.sidebar.number_input('Fare in USD',0.0,255.0)

if st.sidebar.button('Predict'):
    inputs = [[pclass,age ,sex,fare]]
    prediction = model.predict(inputs)

    if prediction == 1:
        st.success('you are likely to survive')
        st.balloons()
    else:
        st.error('survival chances are very low') 

hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)           

      
