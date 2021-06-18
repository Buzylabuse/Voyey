#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 08:46:28 2021

@author: victorbuzy
"""


import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter
from datetime import datetime, date


def display_header_Status_Agesdesclients():
    st.markdown (f"<div id='linkto_Agedesclients'></div>", unsafe_allow_html=True)
    st.markdown ("Quel est l'age de nos clients?")
    
    df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)


    birthDate = df['Date\xa0de\xa0naissance'].to_list()
    currentDate = datetime.today().date()
#print(currentDate)


#print(birthDate)
    M_list=[]
    for i in birthDate:  
        if i == '-':
        
            continue
        birthDate = datetime.strptime(i, "%d/%m/%Y").date()
        age = currentDate.year - birthDate.year   
        age=int(age)
        M_list.append(age)
    

    df1=pd.DataFrame(M_list,columns=['Age'])
    print(df1)

    df1['Age_groupe']=pd.cut(df1.Age , bins = [0,18,25,30,40,50,60,80,100,10000],labels=['0-18','18-25','25-30','30-40','40-50','50-60','60-80','80-100','100-1000'])

    print(df1)
    list_of_bins = df1['Age_groupe'].to_list()

    print(list_of_bins)
    
    Data=Counter(list_of_bins)
    print(Data)
    Ages=['0-18','18-25','25-30','30-40','40-50','50-60','60-80','80-100','100-1000']
    The_list=[]
    for i in Ages:
        Number=(Data[i])
        The_list.append(Number)
        print(The_list)
    fig = px.pie(df1,values = The_list, names = Ages,title='Ages des clients')
    st.plotly_chart(fig)
        
    return None

#M_list["age groupe"]=pd.cut(M_list , bins = [0,20,40,60,80,100,10000],labels=['0-20','20-40','40-60','60-80','80-100','100-10000'])

#print(M_list)


#fig = px.pie(df,values = M_list, names = tranches,title='Ages de nos clients')
#st.plotly_chart(fig)
    


