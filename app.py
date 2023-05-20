import streamlit as st 
import streamlit.components.v1 as com
import pandas as pd
import numpy as np
import os
import pickle
import warnings
com.html("""
<div>
<this is my first HTml page
<button> This is a button </button>
</div>
""")
warnings.filterwarnings("ignore", message="Trying to unpickle estimator")

st.set_page_config(page_title="Green Delight", page_icon="https://i.pinimg.com/736x/8f/0e/88/8f0e8808d45745a3e0e7fefc21b452dd.jpg", layout='centered', initial_sidebar_state="collapsed")

def load_model(modelfile):
	loaded_model = pickle.load(open(modelfile, 'rb'))
	return loaded_model

def main():
    # title
    html_temp = """
    <div>
    <h1 style="color:GREEN;text-align:center;"> Choose your Crop With Green Delight </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    col = st.columns(1)[0]

    with col:
        st.subheader("Get best Crop to make your Farm Flourish")
        N = st.number_input("Nitrogen", 1,10000)
        P = st.number_input("Phosporus", 1,10000)
        K = st.number_input("Potassium", 1,10000)
        temp = st.number_input("Temperature in °C",0.0,100000.0)
        humidity = st.number_input("Humidity in %", 0.0,100000.0)
        ph = st.number_input("Ph", 0.0,100000.0)
        rainfall = st.number_input("Rainfall in mm",0.0,100000.0)

        feature_list = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(feature_list).reshape(1,-1)
        
        if st.button('Explore'):

            loaded_model = load_model('model.pkl')
            prediction = loaded_model.predict(single_pred)
            col.write('''
		    ## Results  
		    ''')
            col.success(f"{prediction.item().title()} are recommended by Green Delight")
    hide_menu_style = """
    <style>
    .block-container {padding: 2rem 1rem 3rem;}
    #MainMenu {visibility: hidden;}
    </style>
    """

hide_menu_style = """
        <style>
        .block-container {padding: 2rem 1rem 3rem;}
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	main()
