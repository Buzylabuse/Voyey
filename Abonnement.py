#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:37:41 2021

@author: victorbuzy
"""

import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter
import csv
import numpy as np
import streamlit as st
from fpdf import FPDF
import base64
from tempfile import NamedTemporaryFile
import orca
from Export_pdf import exporter_pdf

def display_header_Status_Abonnement():

       
    st.markdown (f"<div id='linkto_Abonnement'></div>", unsafe_allow_html=True)
    st.markdown ("Les inscrits sont ils abonnés?")



    df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)
    #print(df)
    

    list_of_status = df['VoyeyAkaz\xa0status'].to_list()
    #print(list_of_status)
    
    
    Data=Counter(list_of_status)
    #print()

    Status= ['Actif','Inactive']
    my_list=[]
    for i in Status:   
        Number=(Data[i])
        my_list.append(Number)
   
    fig = px.pie(df,values = my_list, names = Status,title='Abonnement')
    st.plotly_chart(fig)
    
    
    #exporter_pdf(fig)
    #pdf1=exporter_pdf(fig)

                    
    return None






