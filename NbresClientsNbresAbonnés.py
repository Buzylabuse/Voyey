#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 16 10:16:56 2021

@author: victorbuzy
"""

import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter
import csv
from collections import Counter
from datetime import datetime, date
import plotly.graph_objects as go
from Export_pdf import exporter_pdf



def display_header_Status_NCNA():
    
       
    st.markdown (f"<div id='linkto_NbresClientsNbresAbonnés'></div>", unsafe_allow_html=True)




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
#print(my_list)
#print()



    print("Nombres d'inscrits':", my_list[1])
    print("Nombres d'abonnés:", my_list[0])


    st.markdown ("Il y a **"+str(my_list[1])+ "** Inscrits et **"+str(my_list[0])+"** abonnés")
    
    
    st.markdown ("**Qui sont les nouveaux clients du jours?**")
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
        
    Data1= len(C)
    
    ##Pour le nombre d'inscrits dans la  semaine
    C1=[]
    for i,j in zip(The_list,CompteCree):
        if i<= 7:        
            C1.append(j)
    Data2= len(C1)
    
    ##Pour le nombre d'inscrits dans le mois
    C2=[]
    for i,j in zip(The_list,CompteCree):
        if i<= 30:        
            C2.append(j)
    Data3= len(C2)
    
    df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)
    df.fillna('01/01/2200', inplace=True)
#print(df)
    my_data = pd.read_csv("UtilisateursVoyey.csv", sep=',', header=0, usecols=[0])
#print(my_data)
    list_of_actif = my_data['Voyey\xa0ID'].to_list()
#print(list_of_actif)

    Data=Counter(list_of_actif)

#print(Data)
    today=datetime.today().date()
    Startdate = df['Start\xa0date'].to_list()


#print(Startdate)
    Abonne_list=[]
    for i in Startdate:
        Compte = datetime.strptime(i, "%d/%m/%Y").date()
    #print(Compte)
        Newclients =today-Compte
        Newclients=Newclients.days
        Abonne_list.append(Newclients)
    

        
    PrenomAbonne= df['Prénom']
    PA=[]
    for i,j in zip(Abonne_list,PrenomAbonne):
        if 0<i<=7:        
            PA.append(j)
        

    
    NomAbonne = df['Nom']
    NA=[]
    for i,j in zip(Abonne_list,NomAbonne):
        if 0<i<=7:        
            NA.append(j)
            
    PaysAbonne = df['Pays']
    PaysA=[]
    for i,j in zip(Abonne_list,PaysAbonne):
        if 0<i<=7: 
            PaysA.append(j)

    EmailAbonne = df['E-mail']
    EA=[]
    for i,j in zip(Abonne_list,EmailAbonne): 
        if 0<i<=7:        
            EA.append(j)
       
        #print(EA) 
    Start = df['Start\xa0date']
    SA=[]
    for i,j in zip(Abonne_list,Start):
        if 0<i<=7:        
            SA.append(j)
            
    End = df['End\xa0date']
    EnA=[]
    for i,j in zip(Abonne_list,End):
        if 0<i<=7:        
            EnA.append(j)
    
    D=[]
    for i,j in zip(Abonne_list,Startdate):
        if i==1:        
            D.append(j)
    Data= len(D)
    
            
    ##Pour le nombre d'abonnés dans la semaine
    D1=[]
    for i,j in zip(Abonne_list,Startdate):
        if 0<i<=7:        
            D1.append(j)
    Data4= len(D1)
    
    ##Pour le nombre d'abonnés dans le mois
    D2=[]
    for i,j in zip(Abonne_list,Startdate):
        if 0<i<= 30:        
            D2.append(j)
    Data5= len(D2)

#print(Data5)
    
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
#print(my_list)

    my_list = ["Mensuel" if 0<x<32 else  "Annuel"  for x in my_list]
#print(my_list)
    TypeA=[]
    for i,j in zip(Abonne_list,my_list):
        if 0<i<=7:        
            TypeA.append(j)
    

            
    
    
    st.markdown ("Il y a eu **+"+str(Data1)+"** nouveaux inscrits entre hier et aujourd'hui")
    st.markdown ("Il y a eu **+"+str(Data2)+"** nouveaux inscrits au cours des 7 derniers jours")
    st.markdown ("Il y a eu **+"+str(Data3)+"** nouveaux inscrits au cours des 30 derniers jours")
    
    
    figure = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Pays','Email', 'Statut','Compte Crée','Abonnement']), 
                               cells=dict(values=[P,N,Pays1,E,S,C,A] ))])
    st.plotly_chart(figure)
    
    
    st.markdown ("**Qui sont les nouveaux abonnés du jours?**")
    
    st.markdown ("Il y a eu **+"+str(Data)+"** nouveaux abonnés entre hier et aujourd'hui")
    st.markdown ("Il y a eu **+"+str(Data4)+"** nouveaux abonnés au cours des 7 derniers jours")
    st.markdown ("Il y a eu **+"+str(Data5)+"** nouveaux abonnés au cours des 30 derniers jours")
    figure1 = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Pays','Email','Debut Abonnement','Fin Abonnement','Type Abonnement']), 
                               cells=dict(values=[PA,NA,PaysA,EA,SA,EnA,TypeA] ))])
    
    
    
    st.plotly_chart(figure1)
    
    


#fig = px.pie(df,values = my_list, names = Status,title='Abonnement')
#st.plotly_chart(fig)
    return None