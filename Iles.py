#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:22:04 2021

@author: victorbuzy
"""

import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter

def display_header_Status_Iles():
    st.markdown (f"<div id='linkto_ClientsVoyey'></div>", unsafe_allow_html=True)
    st.markdown ("Pourcentage de clients par Iles")
    
    df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)


    list_of_island = df['Pays'].to_list()


    Data=Counter(list_of_island)
    print(Data)

    Island = ['Guadeloupe','Martinique','Guyane française','La Réunion','France','NA','Canada']
  
# Here green is not in col_count 
# so count of green will be zero
    my_list=[]
    for i in Island:   
        Number=(Data[i])
        my_list.append(Number)
    


    fig = px.pie(df,values = my_list, names = Island,title='Nombres de personnes inscrites par iles')
    st.plotly_chart(fig)
    
    return None