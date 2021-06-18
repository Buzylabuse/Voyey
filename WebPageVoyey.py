#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 13:12:19 2021

@author: victorbuzy
"""

import streamlit as st


def display_sidebar_left():
    """
    Displays the sidebar.

    Returns: None

    """
    st.sidebar.title("Dashboard Voyey")
    st.sidebar.markdown(f"<a href='#linkto_incomes_total'> CA total</a>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<a href='#linkto_incomes_technicians'> CA par technicien</a>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<a href='#linkto_incomes_agencies'> CA par agence</a>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<a href='#linkto_client_request'> Nombre total de demandes clients</a>",
                        unsafe_allow_html=True)
    st.sidebar.markdown(f"<a href='#linkto_client_request_agency'> Nombre de demandes par agence</a>",
                        unsafe_allow_html=True)
    st.sidebar.markdown(f"<a href='#linkto_agency_alert'> Agences à recontacter</a>",
                        unsafe_allow_html=True)
    st.sidebar.markdown(f"<a href='#linkto_profitability_mission'> Coût du matériel par mission</a>",
                        unsafe_allow_html=True)
    return None