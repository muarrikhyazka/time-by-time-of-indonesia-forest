import pandas as pd
import streamlit as st
from PIL import Image
from bokeh.models.widgets import Div
import plotly.express as px
import base64
import nltk
nltk.download('punkt')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import webbrowser


title = 'Time by Time Indonesia Vegetation'




# Layout
img = Image.open('assets/icon_pink-01.png')
st.set_page_config(page_title=title, page_icon=img, layout='wide')






st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.center {
  display: block;
  margin-left: auto;
  margin-right: auto;
#   width: 50%;
}
</style> """, unsafe_allow_html=True)


padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

file_name='style.css'
with open(file_name) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)






# Content

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s" class="center" width="100" height="100"/>' % b64
    st.write(html, unsafe_allow_html=True)


# Sidebar color
st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #ef4da0;
    }
</style>
""", unsafe_allow_html=True)




with st.sidebar:
    f = open("assets/icon-01.svg","r")
    lines = f.readlines()
    line_string=''.join(lines)

    render_svg(line_string)

    st.write('\n')
    st.write('\n')
    st.write('\n')

    if st.button('🏠 HOME'):
        # js = "window.location.href = 'http://www.muarrikhyazka.com'"  # Current tab
        js = "window.open('http://www.muarrikhyazka.com')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)

    if st.button('🍱 GITHUB'):
        # js = "window.location.href = 'https://www.github.com/muarrikhyazka'"  # Current tab
        js = "window.open('https://www.github.com/muarrikhyazka')"
        html = '<img src onerror="{}">'.format(js)
        div = Div(text=html)
        st.bokeh_chart(div)








st.title(title)


st.subheader('Business Understanding')
st.write(
    """
    As we know, Indonesia has so many fertilized soil and green creatures. I just want to know how is the change of vegetation time by time.
    """
)


st.subheader('Data Understanding')
st.write(
    """
    I pulled the data through [Google Earth Engine API](https://developers.google.com/earth-engine/datasets/catalog). 
    """
)

st.image('png_edited_output/maps_2000-03-01_edited.png')




st.subheader('Method')



st.subheader('Insight')

## show gif

st.write(
    """
    Mostly companies which are needed data person are in Jakarta. Many data job are in big cities in Java. Outside of Java only 2 jobs. There is big gap here.
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2023-01-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2022-01-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2001-01-01_edited.png')



st.image('png_edited_output/maps_2001-01-01_edited.png')
st.image('png_edited_output/maps_2022-01-01_edited.png')
st.image('png_edited_output/maps_2023-01-01_edited.png')







c1, c2 = st.columns(2)
with c1:
    st.info('**[Github Repo](https://github.com/muarrikhyazka/data-role-demand-analysis-in-indonesia)**', icon="🍣")

