import visualisasi, statistical_analysis,mainpage

import streamlit as st
import numpy as np


st.set_page_config(
    page_title="First App",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://gethelp.com/about/',
        'Report a bug': "https://developer.android.com/studio/report-bugs",
        'About': "This is our first milestone"
    }
)


PAGES = {'Data Visualization': visualisasi,
        'Statistical Analysis': statistical_analysis,
        'Main Page': mainpage}

selected =  st.sidebar.selectbox('Select Page:',['Main Page','Data Visualization','Statistical Analysis'],index=0)
page = PAGES[selected]

page.app()