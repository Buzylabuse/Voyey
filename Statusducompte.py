#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:40:49 2021

@author: victorbuzy
"""

import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter
import plotly.graph_objects as go

def display_header_Status_Compte():
    
       
    st.markdown (f"<div id='linkto_Statusducompte'></div>", unsafe_allow_html=True)
    st.markdown ("Status Validité de l'adresse email")


    df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)

    list_of_status = df['Statut'].to_list()

    Data=Counter(list_of_status)

    Status= ['Active','Inactive']
    my_list=[]
    for i in Status:   
        Number=(Data[i])
        my_list.append(Number)
    
    
    
    fig = px.pie(df,values = my_list, names = Status,title='Status de la validité du compte')
    st.plotly_chart(fig)
    
    emails = df['E-mail']
    Email=[]
    for i,e in enumerate(list_of_status):
        if e == 'Inactive':
            e=emails[i]
            print(e)
            Email.append(e)
            
    Noms = df['Nom']
    N=[]
    for i,e in enumerate(list_of_status):
        if e == 'Inactive':
            e=Noms[i]
            print(e)
            N.append(e)
            
    Prénom = df['Prénom']
    P=[]
    for i,e in enumerate(list_of_status):
        if e == 'Inactive':
            e=Prénom[i]
            print(e)
            P.append(e)
    
    S= ['Inactive']
    list=[]
    for i in S:   
        Number=(Data[i])
        list.append(Number)


    e=list[0]
    e=int(e)
    
    
    figure = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Email', 'Status']), 
                               cells=dict(values=[P,N,Email,S*e] ))])
    st.plotly_chart(figure)

    return None
