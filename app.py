import streamlit as st
from fastai.vision.all import *
import plotly.express as px
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath= pathlib.WindowsPath


# title

st.title('Classification of transports')

file= st.file_uploader('Rasm yuklash.', type = ['jpeg', 'png','svg','gif','jfif'])
if file:    
    st.image(file)
    # PIL Image

    img = PILImage.create(file)
    # model' ni yuklab olish
    model = load_learner('transport_model.pkl')

    pred, pred_id, probs = model.predict(img)

    st.success(f'Bashorat: {pred}')
    st.info(f'Ehtimollilik: {probs[pred_id]*100:.1f}%')

    fig = px.bar(x=probs*100,y=model.dls.vocab)
    st.plotly_chart(fig)

