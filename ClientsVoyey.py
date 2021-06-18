#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 19:48:29 2021

@author: victorbuzy
"""
import os
import streamlit as st
import pandas as pd
import altair as alt
from plotly import express as px
from collections import Counter
from Statusducompte import *
from Iles import *
from Abonnement import *
from TypeAbonnements import *
from NbresClientsNbresAbonnés import *
from Sexe import *
from Agedesclients import *
from Typesdecommandes import *
from DefautPaiement import *
from fpdf import FPDF
import base64
from tempfile import NamedTemporaryFile
from TestsExport import *
import orca



st.write(""" 
         # VOYEY plus Grand 
         """
         )

st.sidebar.title("Clients:")


st.sidebar.markdown(f"<a href='#linkto_NbresClientsNbresAbonnés'> Nombre total de clients et d'abonnés</a>",
                        unsafe_allow_html=True)
st.sidebar.markdown(f"<a href='#linkto_ClientsVoyey'> Nombre total de clients par iles</a>",
                        unsafe_allow_html=True)
st.sidebar.markdown(f"<a href='#linkto_Statusducompte'> Activation de l'email </a>",
                        unsafe_allow_html=True)
st.sidebar.markdown(f"<a href='#linkto_Abonnement'> Abonnements</a>",
                        unsafe_allow_html=True)
st.sidebar.markdown(f"<a href='#linkto_TypeAbonnements'> Type d'abonnements et CA</a>",
                        unsafe_allow_html=True)
st.sidebar.markdown(f"<a href='#linkto_Sexe'>Sexes des Inscrits </a>",
                        unsafe_allow_html=True)
st.sidebar.markdown(f"<a href='#linkto_Agedesclients'>Ages des clients </a>",
                        unsafe_allow_html=True)

st.sidebar.title("Commandes:")
st.sidebar.markdown(f"<a href='#linkto_Typesdecommandes'>Type de commandes </a>",
                        unsafe_allow_html=True)
st.sidebar.markdown(f"<a href='#linkto_DefautPaiement'>Problème de paiements </a>",
                        unsafe_allow_html=True)

st.sidebar.title("Exporter Rapport en PDF:")
st.sidebar.markdown(f"<a href='#linkto_ExporterRapportPDF'>Exporter rapport PDF </a>",
                        unsafe_allow_html=True)



display_header_Status_NCNA()
display_header_Status_Iles()
display_header_Status_Compte()
display_header_Status_Abonnement()
display_header_Status_TypeAbonnements()
display_header_Status_Sexe()
display_header_Status_Agesdesclients()
display_header_Status_Typesdecommandes()
display_header_Status_DefautPaiement()
display_header_exporter_rapport_pdf()






