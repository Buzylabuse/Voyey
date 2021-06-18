#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 26 10:36:58 2021

@author: victorbuzy
"""

import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter
from datetime import datetime, date
import plotly.graph_objects as go


st.markdown (f"<div id='linkto_Statusducompte'></div>", unsafe_allow_html=True)
st.markdown ("Quels sont les nouveaux clients du jour?")
df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)
CompteCree = df['Compte\xa0créé\xa0le'].to_list()

today=datetime.today().date()
#print(today)

The_list=[]
for i in CompteCree:
    Compte = datetime.strptime(i, "%d/%m/%Y").date()
    #print(Compte)
    Newclients =today-Compte
    Newclients=Newclients.days
    The_list.append(Newclients)



Prenom= df['Prénom']
P=[]
for i,j in zip(The_list,Prenom):
    if i==0 or i==1:        
        P.append(j)

Nom = df['Nom']
N=[]
for i,j in zip(The_list,Nom):
    if i==0 or i==1:        
        N.append(j)

Pays = df['Pays']
Pays1=[]
for i,j in zip(The_list,Pays):
    if i==0 or i==1:        
        Pays1.append(j)

Email = df['E-mail']
E=[]
for i,j in zip(The_list,Email):
    if i==0 or i==1:    
        E.append(j)

Statut = df['Statut']
S=[]
for i,j in zip(The_list,Statut):
    if i==0 or i==1:        
        S.append(j)

C=[]
for i,j in zip(The_list,CompteCree):
    if i==0 or i==1:        
        C.append(j)
        
Abonnement = df['VoyeyAkaz\xa0status'].to_list()
A=[]
for i,j in zip(The_list,Abonnement):
    if i==0 or i==1:
        A.append(j)

data=len(C)
print(data)
    

figure = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Pays','Email', 'Statut','Compte Crée','Abonnement']), 
                               cells=dict(values=[P,N,Pays1,E,S,C,A] ))])
st.plotly_chart(figure)