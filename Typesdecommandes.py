#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 09:24:14 2021

@author: victorbuzy
"""
import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter
import csv
import numpy as np



def display_header_Status_Typesdecommandes():
    st.markdown (f"<div id='linkto_Typesdecommandes'></div>", unsafe_allow_html=True)
    st.markdown ("Quel sont les types de commandes?")


    df= pd.read_csv("requests.csv", index_col=0, parse_dates=True)
    
 
    list_of_type = df['Type'].to_list()

    Data=Counter(list_of_type)

    Status= ['Envoyer','Acheter','Reexpedition']
    my_list=[]
    for i in Status:   
        Number=(Data[i])
        my_list.append(Number)
    

    fig = px.pie(df,values = my_list, names = Status,title='type de commande')
    st.plotly_chart(fig)
    return None