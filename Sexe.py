#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 22:12:26 2021

@author: victorbuzy
"""

import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter

def display_header_Status_Sexe():
    
       
    st.markdown (f"<div id='linkto_Sexe'></div>", unsafe_allow_html=True)
    st.markdown ("Sexe des individus")



    df = pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)
    print(df)

    list_of_status = df['Titre'].to_list()

    print(list_of_status)
    
    Data=Counter(list_of_status)
    print(Data)

    Status= ['Monsieur','Madame','-']
    my_list=[]
    for i in Status:   
        Number=(Data[i])
        my_list.append(Number)
    
    fig = px.pie(df,values = my_list, names = Status,title='Sexe des individus')
    st.plotly_chart(fig)

    return None