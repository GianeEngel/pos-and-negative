# -*- coding: utf-8 -*-
"""
APP positivos negativos COVID-19

@author: mirkos@gmail.com
"""

import streamlit as st
import joblib

classes = ['COVID-19 negative','COVID-19 positive']
st.title('AI-Blood - COVID-19 Diagnosis')
modelo = joblib.load('giane-pn.sav')
mono = st.number_input('Monocytes (10^9/L)')
linf = st.number_input('Lymphocytes (10^9/L)')
plaq = st.number_input('Platelets (10^9/L)')
pcr = st.number_input('CRP (mg/dL)')
ferr = st.number_input('Ferritin (μg/mL)')
pac = [mono,linf,plaq,pcr,ferr]

pred = modelo.predict([pac])
if st.button('Analyse'):
    st.write(classes[int(pred)])
