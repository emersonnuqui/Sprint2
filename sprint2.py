import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as font_manager

#Set font for graphs
fontpath = ['font/spotify']
font = font_manager.findSystemFonts(fontpaths=fontpath)
print(font)
for file in font:
    font_manager.fontManager.addfont(file)

plt.rcParams['font.family'] = 'Gotham'

#Set web page to wide layout 
st.set_page_config(layout="wide",initial_sidebar_state="expanded")
st.set_option('deprecation.showPyplotGlobalUse', False)

#Setting font for all text to Raleway
st.write("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,600;0,700;0,800;1,300&display=swap');
    html, body, [class*="css"]  {
    font-family: 'Raleway', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True) 

def load_data():
    # Load the data for tracks and daily charts
    chart_tracks_df = pd.read_csv('data/spotify_daily_charts_tracks.csv')
    track_df = pd.read_csv('data/spotify_daily_charts.csv')
    #Merge the 2 dataframes
    tracks_df = track_df.merge(chart_tracks_df, on=['track_id','track_name'], how='left')
    tracks_df['date'] = pd.to_datetime(tracks_df['date'])

    #Extract data for specific artist
    artist_data=tracks_df[
        tracks_df["artist_name"]=="Taylor Swift"]

    return artist_data

def introduction():
    # Write the title and the subheader
    subheader = '<p style="font-size: 60px; font-weight:700; text-align: center;">Hello Spotify!</p>'
    st.markdown(subheader, unsafe_allow_html=True)


def artist():
    st.image("taylor.jpg")


    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    about = '<p style="font-size: 24px; font-weight:700; text-align: left;">About:</p>'
    st.markdown(about, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    info = '<p style="font-size: 14px; font-weight:600; text-align: left;">Taylor Alison Swift is an American singer-songwriter. Her discography spans genres and her narrative songwriting—often inspired by her personal life—has received critical praise and</p>'
    st.markdown(info, unsafe_allow_html=True)

    st.write("[Twitter](https://twitter.com/taylorswift13)")
    st.write("[Facebook](https://www.facebook.com/TaylorSwift/)")
    st.write("[Instagram](https://www.instagram.com/taylorswift/)")
    st.write("[Website](https://www.taylorswift.com/)")

def visuals():
    st.image("taylor.jpg")

    data = load_data()


st.sidebar.markdown('<p style="font-size: 25px; font-weight:700; color:black; text-align: center;">Main Pages</p>', unsafe_allow_html=True)

list_of_pages = [
    "Introduction",
    "Artist",
    "Visuals"
]
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Introduction":
    introduction()
elif selection == "Artist":
    artist()