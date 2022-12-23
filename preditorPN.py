# -*- coding: utf-8 -*-
"""
APP positivos negativos COVID-19

@author: mirkos@gmail.com
"""

import streamlit as st
import joblib

classes = ['COVID-19 negative','COVID-19 positive']
st.title('Predict for COVID-19')
modelo = joblib.load('giane-pn.sav')
mono = st.number_input('Monocytes (/mm3)')
linf = st.number_input('Lymphocytes (/mm3)')
plaq = st.number_input('Platelets (/mm3)')
pcr = st.number_input('PCR (mg/dL)')
ferr = st.number_input('ferritin (ng/mL)')
pac = [mono,linf,plaq,pcr,ferr]

pred = modelo.predict([pac])
if st.button('Analyse'):
    st.write(classes[int(pred)])
