from enigma import enigma
import streamlit as st
from PIL import Image

st.title('Enigma Machine Simulator')

image = Image.open('enigma.png')
st.image(image, caption='Germans Using Enigma During World War-II',
use_column_width=True)
st.write("""
The Enigma Machine is a encryption device that was used by the Nazi Germany during the World Warl-II. Communication of Navy and Airforce
of the german armies were heavily depended on it. Use this simulator to get your message encrypted like it used to be done in World War-II.
""")


st.sidebar.header('User Encryption Settings')

def user_input_features():
    first_rotor_model = st.sidebar.selectbox('Rotor-1 Model:', ('Rotor-I', 'Rotor-II', 'Rotor-III', 'Rotor-IV', 'Rotor-V', 'Rotor-VI', 'Rotor-VII', 'Rotor-VIII', 'Rotor-Beta', 'Rotor-Gamma'))
    second_rotor_model = st.sidebar.selectbox('Rotor-2 Model:',('Rotor-I', 'Rotor-II', 'Rotor-III', 'Rotor-IV', 'Rotor-V', 'Rotor-VI', 'Rotor-VII', 'Rotor-VIII', 'Rotor-Beta', 'Rotor-Gamma'))
    third_rotor_model = st.sidebar.selectbox('Rotor-3 Model:', ('Rotor-I', 'Rotor-II', 'Rotor-III', 'Rotor-IV', 'Rotor-V', 'Rotor-VI', 'Rotor-VII', 'Rotor-VIII', 'Rotor-Beta', 'Rotor-Gamma'))

    reflector_model = st.sidebar.selectbox('Reflector Model:', ('Reflector-B', 'Reflector-C', 'Reflector-B Thin', 'Reflector-C Thin'))

    first_rotor_letter = st.sidebar.selectbox('Rotor-1 Starting Letter:', ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))
    second_rotor_letter = st.sidebar.selectbox('Rotor-2 Starting Letter:', ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))
    third_rotor_letter = st.sidebar.selectbox('Rotor-3 Starting Letter:', ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))
    input_data = {
        'rotor_model' : [first_rotor_model, second_rotor_model, third_rotor_model],
        'reflector_model' : reflector_model,
        'rotor_letter': [first_rotor_letter, second_rotor_letter, third_rotor_letter]
        }


    return input_data

data = user_input_features()


rotor_selection_list = data.get('rotor_model')
reflector = data.get('reflector_model')
starter_list = data.get('rotor_letter')
st.write('___________________________________________________________________________________________')

st.write('**Write Your Secret Message For Encryption:**')
message = st.text_input("Input Message Here Below")

st.write('___________________________________________________________________________________________')

st.write('**Your Encrypted Message Is:**')
st.write(enigma(message, rotor_selection_list, reflector, starter_list))
st.write('___________________________________________________________________________________________')
st.write("""
To see the encrypted message, write the encrypted message on input message above. Make sure to use the same settings used to encrypt 
the message in the first place. 
""")
