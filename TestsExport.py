#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 10:39:55 2021

@author: victorbuzy
"""

import pandas as pd
import streamlit as st
from plotly import express as px
from collections import Counter
import csv
import numpy as np
from decimal import Decimal
import plotly.graph_objects as go
from datetime import datetime, date
import base64
from tempfile import NamedTemporaryFile
import orca
from fpdf import FPDF


def display_header_exporter_rapport_pdf():
    st.markdown (f"<div id='linkto_ExporterRapportPDF'></div>", unsafe_allow_html=True)

    figs=[]
    df= pd.read_csv("UtilisateursVoyey.csv", index_col=0, parse_dates=True)


    

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

    report_text ="Il y a "+str(my_list[1])+ " Inscrits et "+str(my_list[0])+" abonnés"
    #a=st.markdown ("Il y a **"+str(my_list[1])+ "** Inscrits et **"+str(my_list[0])+"** abonnés")
    #figs.append(a)    
    
    #b=st.markdown ("**Qui sont les nouveaux clients du jours?**")
    #figs.append(b)   
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
    
    
    report_text1="Il y a eu +"+str(Data1)+" nouveaux inscrits entre hier et aujourd'hui"
    report_text2="Il y a eu +"+str(Data2)+" nouveaux inscrits au cours des 7 derniers jours"
    report_text3="Il y a eu +"+str(Data3)+" nouveaux inscrits au cours des 30 derniers jours"
    fig = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Pays','Email', 'Statut','Compte Crée','Abonnement']), 
                             cells=dict(values=[P,N,Pays1,E,S,C,A] ))])


    fig.update_layout(height=600, width=600, title_text="Nouveaux inscrits entre hier et aujourd'hui")
    figs.append(fig)
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
    
    report_text4=("**Qui sont les nouveaux abonnés du jours?**")
    
    report_text5= ("Il y a eu +"+str(Data)+" nouveaux abonnés entre hier et aujourd'hui")
    report_text6= ("Il y a eu +"+str(Data4)+" nouveaux abonnés au cours des 7 derniers jours")
    report_text7= ("Il y a eu +"+str(Data5)+" nouveaux abonnés au cours des 30 derniers jours")
    figure1 = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Pays','Email','Debut Abonnement','Fin Abonnement','Type Abonnement']), 
                               cells=dict(values=[PA,NA,PaysA,EA,SA,EnA,TypeA] ))])
    
    
    figure1.update_layout(height=600, width=600, title_text="Les Nouveaux abonnés de la semaine")
    figs.append(figure1)
    
####################################################
#st.plotly_chart(figure)





    list_of_island = df['Pays'].to_list()


    Data=Counter(list_of_island)
    #print(Data)
    Island = ['Guadeloupe','Martinique','Guyane française','La Réunion','France','NA','Canada']
  
# Here green is not in col_count 
# so count of green will be zero
    my_list=[]
    for i in Island:   
        Number=(Data[i])
        my_list.append(Number)
    


    fig = px.pie(df,values = my_list, names = Island,title='Nombres de personnes inscrites par iles')
#st.plotly_chart(fig)
    figs.append(fig)
#########################################################

    list_of_status = df['Titre'].to_list()  
   
    Data=Counter(list_of_status)
   

    Status= ['Monsieur','Madame','-']
    my_list=[]
    for i in Status:   
        Number=(Data[i])
        my_list.append(Number)
    
    fig = px.pie(df,values = my_list, names = Status,title='Sexe des individus inscrits')
    
    figs.append(fig)
################################################################################
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
    figs.append(fig)
    
    
################################################################################
    list_of_status = df['Statut'].to_list()

    Data=Counter(list_of_status)

    Status= ['Active','Inactive']
    my_list=[]
    for i in Status:   
        Number=(Data[i])
        my_list.append(Number)
    
    
    
    fig = px.pie(df,values = my_list, names = Status,title='Status de la validité du compte')
    figs.append(fig)
    
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
    
    
    fig = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Email', 'Status']), 
                               cells=dict(values=[P,N,Email,S*e] ))])
    fig.update_layout(height=600, width=600, title_text="Tableau des personnes ayant oubliés de valider leur compte:")
    figs.append(fig)   
########################################################################
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
              
    fig = px.pie(df,values = M_list, names = Status,title='Représentation des types Abonnements choisis par nos abonnés')
    figs.append(fig)
    #st.plotly_chart(fig)
    
    Mensuel = M_list[0]
    Mensuel = int(Mensuel)*9.99
    Annuel = M_list[1]
    Annuel = int(Annuel)*49
    CATotal= int(Mensuel+Annuel)
    #st.markdown ("Chiffre d'affaire sur les abonnements mensuels: **"+str(Mensuel)+"€** et annuels: **"+str(Annuel)+"€**" )
    #st.markdown  ("Chiffre d'affaire total: **"+str(CATotal)+"€**")
    #st.markdown  ("Qui sont nos abonné(e)s?")

    
    
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


    
    
    fig = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Email','Iles','Abonnement','Start','End']), 
                               cells=dict(values=[P,N,Email,Island_list,my_list,Start_list,End_list] ))])
    #st.plotly_chart(figure)
    
    fig.update_layout(height=600, width=600, title_text="Nos actuels abonnés")
    figs.append(fig)
################################################################################
    
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
    
    
    #st.markdown ("Voici les abonnements se terminant dans la semaine")
    fig = go.Figure(data=[go.Table(header=dict(values=['Prénom','Nom','Email','Iles','Abonnement','End']), 
                               cells=dict(values=[P1,N1,EM1,Pays2,Type_abonnement,End] ))])
    fig.update_layout(height=600, width=600, title_text="Voici les abonnements se terminant dans la semaine")
    figs.append(fig)
    

    
    
    #st.markdown  ("D'ou viennent nos abonnés?")
    
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
        
        
    fig = px.pie(df,values = my_list, names = Island,title='Représentations des abonné(e)s par iles')
    #st.plotly_chart(fi)
    figs.append(fig)
#######################################################

    list_of_status = df['VoyeyAkaz\xa0status'].to_list()
    #print(list_of_status)
    
    
    Data=Counter(list_of_status)
    #print()

    Status= ['Actif','Inactive']
    my_list=[]
    for i in Status:   
        Number=(Data[i])
        my_list.append(Number)
   
    fig = px.pie(df,values = my_list, names = Status,title='Pourcentage des abonnés par rapport aux inscrits')
    figs.append(fig)
    
#####################################################

    export_as_pdf = st.button("Export Report")
    
    def create_download_link(val, filename):
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'
    
    if export_as_pdf:   
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(40, 20, report_text,0,1)
        pdf.cell(40, 20, report_text1,0,1)
        pdf.cell(40, 20, report_text2,0,1)
        pdf.cell(40, 20, report_text3,0,1)
        pdf.cell(40, 20, report_text4,0,1)
        pdf.cell(40, 20, report_text5,0,1)
        pdf.cell(40, 20, report_text6,0,1)
        pdf.cell(40,20,report_text7,0,1)
        
        for fig in figs:
            pdf.add_page()
            with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:               
                fig.write_image(tmpfile.name)
                pdf.image(tmpfile.name, 10, 10, 200, 100)
        html = create_download_link(pdf.output(dest="S").encode("latin-1"), "testfile")
        st.markdown(html, unsafe_allow_html=True)
        

    

    return None