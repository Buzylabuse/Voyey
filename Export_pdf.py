#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:27:01 2021

@author: victorbuzy
"""
import streamlit as st
from fpdf import FPDF
import base64
from tempfile import NamedTemporaryFile
import orca
#from Abonnement import display_header_Status_Abonnement



    

def exporter_pdf(fig):
    def create_download_link(val, filename):
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

    figs=[]
    figs.append(fig)
    export_as_pdf = st.button("Export Report")
    if export_as_pdf:
        pdf = FPDF()
        for fig in figs:
            pdf.add_page()
            with NamedTemporaryFile(delete=False, suffix="#.png") as tmpfile:
                fig.write_image("/Users/victorbuzy/Desktop/Pourcentagesdesabonnements.png")
                pdf.image("/Users/victorbuzy/Desktop/Pourcentagesdesabonnements.png", 10, 10, 200, 100)
        html = create_download_link(pdf.output(dest="S").encode("latin-1"), "testfile")
        st.markdown(html, unsafe_allow_html=True)
    
    return None

