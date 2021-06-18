#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 10:11:25 2021

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
from Export_pdf import exporter_pdf

def display_header_Status_DefautPaiement():
    st.markdown (f"<div id='linkto_DefautPaiement'></div>", unsafe_allow_html=True)
    st.markdown ("Quel sont les taxes des commandes non réglées?")
    df= pd.read_csv("requests.csv", index_col=0, parse_dates=True)
#print(df)
#f = open('requests.csv', 'r')
#data = f.read()
    my_data = pd.read_csv('requests.csv', sep=',', header=0, usecols=[0])
#print(my_data)
    df.fillna(0, inplace=True)
#print(df)

        
    list_of_Total = df['Total'].to_list()
    list_of_Payment= df['Payment done'].to_list()
    list_of_Order= my_data['Order Id'].to_list()
    list_of_User = df['User'].to_list()
    list_of_Source = df['Source'].to_list()
    list_of_Destination = df['Destination'].to_list()
    list_of_Total_Price = df['Total price'].to_list()
    list_of_Created_list = df['Created at'].to_list()

    my_list=[]
    for i in list_of_Total:
        i=float(i.replace(',','.'))
        i=int(i)
        my_list.append(i)
    
#print(my_list)

    The_list=[]
    The_list1=[]
    for i,j in zip(my_list,list_of_Payment):
        if i>0 and j=="Unpaid":
            The_list.append(i)
            The_list1.append(j)
    

    
    Order_Id=[]
    for i,j in zip(The_list,list_of_Order):
        if i>0:
            Order_Id.append(j)

    User_Id=[]
    for i,j in zip(The_list,list_of_User):
        if i>0:
            User_Id.append(j)

    Source = []
    for i,j in zip(The_list,list_of_Source):
        if i>0:
            Source.append(j)

    Destination = []
    for i,j in zip(The_list,list_of_Destination):
        if i>0:
            Destination.append(j)
        
    list_of_Total_Price1 = []
    for i in list_of_Total_Price:   
        list_of_Total_Price1.append(i)
    
    Total_Price = []    
    for i,j in zip(The_list,list_of_Total_Price1):
        if i>0:
            Total_Price.append(j)
        
    Created_list = []    
    for i,j in zip(The_list,list_of_Created_list):
        if i>0:
            Created_list.append(j) 
    
        


    figure = go.Figure(data=[go.Table(header=dict(values=['Order Id','User','Source','Destination', 'Total taxes+transport','Payment Done','Total Price',"Created date"]), 
                               cells=dict(values=[Order_Id,User_Id,Source,Destination,The_list,The_list1,Total_Price,Created_list] ))])
    st.plotly_chart(figure)
    

    return None

    



        

