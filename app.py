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


title = 'Time by Time of Indonesia Vegetation'




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

st.write(
    """
    \n
    \n
    """
)


st.subheader('Business Understanding')
st.write(
    """
    As we know, Indonesia has so many fertilized soil and green creatures. I just want to know how is the change of vegetation time by time. In here, we used NDVI or Normalized Difference Vegetation Index.
    """
)

st.write(
    """
    \n
    \n
    """
)

st.subheader('Data Understanding')
st.write(
    """
    I pulled the data through [Google Earth Engine API](https://developers.google.com/earth-engine/datasets/catalog). 
    """
)

st.write(
    """
    The metrics I used is NDVI or Normalized Difference Vegetation Index. And about what NDVI is I took definition from [eos.com](https://eos.com/blog/ndvi-faq-all-you-need-to-know-about-ndvi/)
    """
)

st.code('Simply put, NDVI helps to differentiate vegetation from other types of land cover (artificial) and determine its overall state. It also allows to define and visualize vegetated areas on the map as well as detect abnormal changes in the growth process.')

st.write(
    """
    Below is the color scale of NDVI. 
    """
)

st.image('NDVI_Scale_LDP_rotated.jpg')

st.write(
    """
    Move to right or more green will be higher the NDVI, it means the healthier plants.
    """
)



st.write(
    """
    Below is the sample of data which has been visualized in map. 
    """
)
st.image('png_edited_output/maps_2000-03-01_edited.png')




st.write(
    """
    \n
    \n
    """
)


st.subheader('Method')

st.write(
    """
    I will list down step by step :
    \n1. Data pulling from [Google Earth Engine API](https://developers.google.com/earth-engine/datasets/catalog).
    \n2. Visualize to map.
    \n3. Screenshot using selenium and iterate per month.
    \n4. Edit image and add text on image.
    \n5. Compile all images as video.
    \n6. Export to gif and mp4.
    """
)

st.write(
    """
    \n
    \n
    """
)



st.subheader('Insight')

## show video
st.video('https://youtu.be/GdeF5u-j_aM')

st.write(
    """
    Above is time lapse video to show change of vegetation in Indonesia by monthly from year 2000. Just play and enjoy.
    """
)

st.write(
    """
    I tried to compare the same month on the latest year, last year, and the oldest year, so we can get the difference or change.
    """
)


st.write(
    """
    **January**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2001-01-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2022-01-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2023-01-01_edited.png')

st.write(
    """
    Getting closer to the present, Sumatra and Sulawesi archipelago has more area with bad vegetation. But Java and Papua has fewer.
    """
)

st.write(
    """
    **February**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2001-02-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2022-02-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2023-02-01_edited.png')

st.write(
    """
    Overall in 2022 getting better, but on 2023, it is back getting worser.
    """
)

st.write(
    """
    **March**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2001-03-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2022-03-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2023-03-01_edited.png')

st.write(
    """
    Nothing significant change, except on Sumatra archipelago.
    """
)

st.write(
    """
    **April**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-04-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-04-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-04-01_edited.png')

st.write(
    """
    On April, nothing significant change.
    """
)

st.write(
    """
    **May**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-05-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-05-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-05-01_edited.png')

st.write(
    """
    On Sulawesi archipelago, it has more area with bad vegetation.
    """
)

st.write(
    """
    **June**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-06-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-06-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-06-01_edited.png')

st.write(
    """
    Decreasing of bad vegetation area on Sulawesi.
    """
)

st.write(
    """
    **July**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-07-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-07-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-07-01_edited.png')

st.write(
    """
    There is no significant change
    """
)

st.write(
    """
    **August**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-08-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-08-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-08-01_edited.png')


st.write(
    """
    On Papua, now it's getting better because has more good vegetation area.
    """
)

st.write(
    """
    **September**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-09-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-09-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-09-01_edited.png')

st.write(
    """
    On Papua, same with August, now it's getting better because has more good vegetation area. On Sumatra same as well.
    """
)

st.write(
    """
    **October**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-10-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-10-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-10-01_edited.png')

st.write(
    """
    Bad vegetation area is rising up on Sumatra.
    """
)

st.write(
    """
    **November**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-11-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-11-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-11-01_edited.png')

st.write(
    """
    Bad vegetation area is increasing on Sumatra, but on Java is decreasing.
    """
)

st.write(
    """
    **December**
    """
)

c11, c12, c13 = st.columns(3)
with c11:
    st.image('png_edited_output/maps_2000-12-01_edited.png')
with c12:
    st.image('png_edited_output/maps_2021-12-01_edited.png')
with c13:
    st.image('png_edited_output/maps_2022-12-01_edited.png')

st.write(
    """
    On Sumatra, bad vegetation area is increasing.
    """
)







c1, c2 = st.columns(2)
with c1:
    st.info('**[Github Repo](https://github.com/muarrikhyazka/time-by-time-of-indonesia-vegetation)**', icon="🍣")

