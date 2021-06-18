#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  9 20:11:19 2021

@author: victorbuzy
"""

import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter
import csv
from datetime import datetime
import plotly.graph_objects as go




def display_header_Status_TypeAbonnements():
    
       
    st.markdown (f"<div id='linkto_TypeAbonnements'></div>", unsafe_allow_html=True)
    st.markdown ("Quel est le type d'abonnement?")



    df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)
   
    

    Datededebut = df['Start\xa0date'].to_list()
    Datedefin = df['End\xa0date'].to_list()



    Datededebut = [str(x) for x in Datededebut]
    Datededebut = [x for x in Datededebut if x != 'nan']
    


    Datedefin = [str(x) for x in Datedefin]
    Datedefin = [x for x in Datedefin if x != 'nan']
   
    def days_between(d1, d2):
            d1 = datetime.strptime(d1, "%d/%m/%Y")
            d2 = datetime.strptime(d2, "%d/%m/%Y")
            return abs((d2 - d1).days)

    my_list=[]
    for i,j in zip(Datededebut,Datedefin):
        c = days_between(i, j)
        my_list.append(c)
        
    #my_list = [0 if x<32 else 1 for x in my_list]
        
    
    my_list = ["Mensuel" if x<32 else "Annuel" for x in my_list]
    
        
    Data=Counter(my_list)

    Status= ['Mensuel','Annuel']
    M_list=[]
    for i in Status:   
        Number=(Data[i])
        M_list.append(Number)
              
    fig = px.pie(df,values = M_list, names = Status,title='')
    st.plotly_chart(fig)
    
    Mensuel = M_list[0]
    Mensuel = int(Mensuel)*9.99
    Annuel = M_list[1]
    Annuel = int(Annuel)*49
    CATotal= int(Mensuel+Annuel)
    st.markdown ("Chiffre d'affaire sur les abonnements mensuels: **"+str(Mensuel)+"€** et annuels: **"+str(Annuel)+"€**" )
    st.markdown  ("Chiffre d'affaire total: **"+str(CATotal)+"€**")
    st.markdown  ("Qui sont nos abonné(e)s?")

    
    
    list_of_status = df['VoyeyAkaz\xa0status'].to_list()
    
    
    emails = df['E-mail']
    Email=[]
    for i,e in enumerate(list_of_status):
        if e == 'Actif':
            e=emails[i]
            print(e)
            Email.append(e)
            
    Noms = df['Nom']
    N=[]
    for i,e in enumerate(list_of_status):
        if e == 'Actif':
            e=Noms[i]
            print(e)
            N.append(e)
    
    Prénom = df['Prénom']
    P=[]
    for i,e in enumerate(list_of_status):
        if e == 'Actif':
            e=Prénom[i]
            print(e)
            P.append(e)
    
    list_of_status = df['VoyeyAkaz\xa0status'].to_list()
    Island= df['Pays']
    Island_list=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = Island[i]
            Island_list.append(e)
            
    list_of_status = df['VoyeyAkaz\xa0status'].to_list()  
    Start= df['Start\xa0date'].to_list() 
    Start_list=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = Start[i]
            Start_list.append(e)
    End= df['End\xa0date'].to_list() 
    End_list=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = End[i]
            End_list.append(e)
    
    Data=Counter(list_of_status)
    S= ['Actif']
    list=[]
    for i in S:   
        Number=(Data[i])
        list.append(Number)    
        
    e=list[0]
    e=int(e)


    
    
    figure = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Email','Iles', 'Status','Abonnement','Start','End']), 
                               cells=dict(values=[P,N,Email,Island_list,S*e,my_list,Start_list,End_list] ))])
    st.plotly_chart(figure)
    
    df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)

    list_of_status = df['VoyeyAkaz\xa0status'].to_list()

    today=datetime.today().date()




    End= df['End\xa0date'].to_list() 
    End_list=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = End[i]
            End_list.append(e)
        
#print (End_list)

    The_list=[]
    for i in End_list:
        Compte = datetime.strptime(i, "%d/%m/%Y").date()
        #print(Compte)
        Newclients =Compte-today
        Newclients=Newclients.days
        The_list.append(Newclients)
    
    End=[]
    for i,j in zip(The_list,End_list):
        if i<=7:
            End.append(j)
    


    Prenom= df['Prénom']
    P=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = Prenom[i]
            P.append(e)
#print(P)
    P1=[]
    for i,j in zip(The_list,P):
        if i<=7:
            
            P1.append(j)
#print(P1)
    Nom= df['Nom']
    N=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = Nom[i]
            N.append(e)
    N1=[]
    for i,j in zip(The_list,N):
        if i<=7:
            N1.append(j)
#print(N1)

    Nom= df['Nom']
    N=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = Nom[i]
            N.append(e)
    N1=[]
    for i,j in zip(The_list,N):
        if i<=7:
            N1.append(j)

    Email= df['E-mail']
    EM=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = Email[i]
            EM.append(e)
    EM1=[]
    for i,j in zip(The_list,EM):
        if i<=7:
            EM1.append(j)


    Pays= df['Pays']
    Pays1=[]
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            e = Pays[i]
            Pays1.append(e)
    Pays2=[]
    for i,j in zip(The_list,Pays1):
        if i<=7:
            Pays2.append(j)

#print(Pays2)

    Datededebut = df['Start\xa0date'].to_list()
    Datedefin = df['End\xa0date'].to_list()



    Datededebut = [str(x) for x in Datededebut]
    Datededebut = [x for x in Datededebut if x != 'nan']
    Datedefin = [str(x) for x in Datedefin]
    Datedefin = [x for x in Datedefin if x != 'nan']
   
    def days_between(d1, d2):
        d1 = datetime.strptime(d1, "%d/%m/%Y")
        d2 = datetime.strptime(d2, "%d/%m/%Y")
        return abs((d2 - d1).days)

    my_list=[]
    for i,j in zip(Datededebut,Datedefin):
        c = days_between(i, j)
        my_list.append(c)
        
    #my_list = [0 if x<32 else 1 for x in my_list]
        
    
    my_list = ["Mensuel" if x<32 else "Annuel" for x in my_list]
    
    Type_abonnement=[]
    for i,j in zip(The_list,my_list):
        if i<=7:
            Type_abonnement.append(j)
    
    
    st.markdown ("Voici les abonnements se terminant dans la semaine")
    figure = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Email','Iles','Abonnement','End']), 
                               cells=dict(values=[P1,N1,EM1,Pays2,Type_abonnement,End] ))])
    st.plotly_chart(figure)
    

    
    
    st.markdown  ("D'ou viennent nos abonnés?")
    
    list_of_status = df['VoyeyAkaz\xa0status'].to_list()
    list_of_island = df['Pays'].to_list()

    #print(list_of_status)
    Data1=Counter(list_of_island)
    #print(list_of_island)
    Data1=Counter(list_of_status)
    print(Data)
    Island = ['Guadeloupe','Martinique','Guyane française','La Réunion','France','NA','Canada']
# Here green is not in col_count 
# so count of green will be zero

    The_list=[]
    I = []
    for i,e in enumerate(list_of_status):   
        if e == 'Actif':
            Number=(list_of_island[i])
            The_list.append(Number)
            print(The_list)

    Data= Counter(The_list)
    
    
    my_list=[]
    for i in Island:   
        Number=(Data[i])
        my_list.append(Number)
        
        
    fi = px.pie(df,values = my_list, names = Island,title='Représentations des abonné(e)s par iles')
    st.plotly_chart(fi)

    

    return None


