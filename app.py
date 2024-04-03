#test link - https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Giraffe_Mikumi_National_Park.jpg/1200px-Giraffe_Mikumi_National_Park.jpg
import io
import os
import streamlit as st
import requests
from PIL import Image
from model import get_caption_model, generate_caption


def get_model():
    return get_caption_model()

caption_model = get_model()

from gtts import gTTS
import base64

from gtts import gTTS
from io import BytesIO
import base64

def predict():
    pred_caption = generate_caption('tmp.jpg', caption_model)
    st.markdown('#### Predicted Caption:')
    st.write(pred_caption)
    st.empty()
    # Convert the predicted caption to audio using Google Text-to-Speech API
    tts = gTTS(pred_caption, lang='en-in', tld='co.in')
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_bytes = audio_buffer.getvalue()
    audio_b64 = base64.b64encode(audio_bytes).decode('utf-8')
    audio_html = f'<audio controls autoplay style="background-color: #f63366; color: #FFFFFF; border-radius: 5px;"><source src="data:audio/mp3;base64,{audio_b64}" type="audio/mp3"></audio>'
    st.markdown(audio_html, unsafe_allow_html=True)

# st.title('Image Caption Bot for Assistive Vision')
st.markdown('<h1 style="color:  #f63366; text-align: center;">Image Caption Bot for Assistive Vision</h1>', unsafe_allow_html=True)

img_url = st.text_input(label='Enter Image URL')

if (img_url != "") and (img_url != None):
    img = Image.open(requests.get(img_url, stream=True).raw)
    img = img.convert('RGB')
    st.image(img,width=250)
    img.save('tmp.jpg')
    if st.button('Predict Caption'):
        predict()
        st.empty()
        os.remove('tmp.jpg')

st.markdown('<center style="opacity: 70%">OR</center>', unsafe_allow_html=True)
img_upload = st.file_uploader(label='Upload Image', type=['jpg', 'png', 'jpeg'])

if img_upload != None:
    img = img_upload.read()
    img = Image.open(io.BytesIO(img))
    img = img.convert('RGB')
    img.save('tmp.jpg')
    st.image(img,width=250)
    if st.button('Predict Caption'):
        predict()
        st.empty()
        os.remove('tmp.jpg')
