#install streamlit, if not already installed using pip
import streamlit as st

#get local machine ip address -> this will be used as password for local tunnel
!wget -q -O - ipv4.icanhazip.com

#run app.py in local tunnel
!streamlit run app.py & npx localtunnel --port 8501