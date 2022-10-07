import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.font_manager as font_manager
import streamlit.components.v1 as components

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
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100;0,200;0,300;0,400;0,600;0,700;0,800;1,300&display=swap');
    html, body, [class*="css"]  {
    font-family: 'Montserrat', sans-serif;
    }
    </style>
    """, unsafe_allow_html=True) 

#Set color for seaborn plots
sns.set(rc={'axes.facecolor':'#191414', 
            'axes.edgecolor': '#ffffff',
            'figure.facecolor':'#191414',
            'grid.color': '#191414',
            'text.color': '#ffffff',
            'ytick.color': '#ffffff',
            'xtick.color': '#ffffff',
            'axes.labelcolor': '#ffffff'
            })

def load_data():
    # Load the data for tracks and daily charts
    chart_tracks_df = pd.read_csv('data/spotify_daily_charts_tracks.csv')
    track_df = pd.read_csv('data/spotify_daily_charts.csv')
    #Merge the 2 dataframes
    tracks_df = track_df.merge(chart_tracks_df, on=['track_id','track_name'], how='left')
    tracks_df['date'] = pd.to_datetime(tracks_df['date'])

    return tracks_df

def introduction():
    # Write the title and the subheader
    subheader = '<p style="font-size: 80px; font-weight:800; text-align: center;">Morissette: Towards a new Birit-Era</p>'
    st.markdown(subheader, unsafe_allow_html=True)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    col1, col2 = st.columns(2)

    col1.image('images/mori-singing.jpg')

    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')
    col2.markdown(' ')

    reasons = '''
    <p style="font-size: 36px; font-weight:300; text-align: center;">If you’re pinoy and you have ears,</p>
    <p style="font-size: 36px; font-weight:300; text-align: center;">You’ve definitely heard of <b style="color:#1DB954;">Morissette</b></p>
    '''
    col2.markdown(reasons, unsafe_allow_html=True)

def artist():
    st.image("images/morissette.jpg", width=1500)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    about = '<p style="font-size: 36px; font-weight:700; text-align: left;">Profiling:</p>'
    st.markdown(about, unsafe_allow_html=True)
    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")
    profile = '''
    <p style="font-size: 20px; font-weight:300; text-align: left;"> - Asia’s Phoenix started her mythical rise to stardom back in 2013 when she joined The Voice Philippines under the mentorship of Sarah G.</p>
    <p style="font-size: 20px; font-weight:300; text-align: left;"> - By 2014, she joined the ranks of Angeline Quinto as part of the ASAP Birit Queens.</p>
    '''
    st.markdown(profile, unsafe_allow_html=True)

    st.markdown(" ")
    st.markdown(" ")
    st.markdown(" ")

    related_artist = '<p style="font-size: 36px; font-weight:700; text-align: left;">Competitors:</p>'
    st.markdown(related_artist, unsafe_allow_html=True)
    col1, col2, col3, col4, col5= st.columns(5)

    col1.markdown(' ')
    col2.image("images/angeline.png", width=250, caption='Angeline Quinto')
    col3.markdown(' ')
    col4.image("images/sarah.png", width=250, caption="Sarah Geronimo")
    col5.markdown(' ')
 

    st.write("[Tiktok](https://www.tiktok.com/@itsmorissette?lang=en)")
    st.write("[Facebook](https://www.facebook.com/MorissettePh/?_rdc=1&_rdr)")
    st.write("[Instagram](https://www.instagram.com/itsmorissette/)")
    st.write("[Website](https://amap.to/morissette/)")
   # st.write("https://open.spotify.com/track/0Dljpp52vCmtXi0E94qjfo?si=08ecbbca56f14f44")
    
def artist_spotify():
    subheader = '<p style="font-size: 80px; font-weight:800; text-align: center;">Morissette and competitors</p>'
    st.markdown(subheader, unsafe_allow_html=True)

    #Munimuni info
    col1, col2, col3 = st.columns(3)
    col1.image("images/mori3.jpg", width=500)
    mori = '<p style="font-size: 36px; font-weight:700; text-align: center;">Morissette</p>'
    col1.markdown(mori, unsafe_allow_html=True)
    spotify = '<p style="font-size: 24px; font-weight:400; text-align: center;">1.06 million monthly listeners</p>'
    col1.markdown(spotify, unsafe_allow_html=True)

    col2.image("images/sarah3.jpg",width=500)
    sarah = '<p style="font-size: 36px; font-weight:700; text-align: center;">Sarah Geronimo</p>'
    col2.markdown(sarah, unsafe_allow_html=True)
    spotify = '<p style="font-size: 24px; font-weight:400; text-align: center;">1.04 million monthly listeners</p>'
    col2.markdown(spotify, unsafe_allow_html=True)

    col3.image("images/angeline3.jpg", width=500)
    ange = '<p style="font-size: 36px; font-weight:700; text-align: center;">Angeline Quinto</p>'
    col3.markdown(ange, unsafe_allow_html=True)
    spotify = '<p style="font-size: 24px; font-weight:400; text-align: center;">0.67 million monthly listeners</p>'
    col3.markdown(spotify, unsafe_allow_html=True)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')


    caption = '<p style="font-size: 40px; font-weight:400; text-align: center;"> <b style="color:#1DB954;">Morissette</b> has already out-streamed Sarah G. and Angeline.</p>'
    st.markdown(caption, unsafe_allow_html=True)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    col1, col2 = st.columns(2)
    situation = '<p style="font-size: 40px; font-weight:700; text-align: center;">Situation</p>'
    col1.markdown(situation, unsafe_allow_html=True)
    reasons = '''
    <p style="font-size: 24px; font-weight:300; text-align: center;">If you ask random pinoys on the street:</p>
    <p style="font-size: 24px; font-weight:300; text-align: center;"><i>“What do you think of Morissette?”</i></p>
    <p style="font-size: 24px; font-weight:300; text-align: center;">  </p>
    <p style="font-size: 24px; font-weight:300; text-align: center;">Everyone will tell you <b style="color:#1DB954;">Morissette is great singer!</b></p>
    '''
    col1.markdown(reasons, unsafe_allow_html=True)

    challenge = '<p style="font-size: 40px; font-weight:700; text-align: center;">Challenge</p>'
    col2.markdown(challenge, unsafe_allow_html=True)
    reasons = '''
    <p style="font-size: 24px; font-weight:300; text-align: center;">If you ask random pinoys  on the street:</p>
    <p style="font-size: 24px; font-weight:300; text-align: center;"><i>“What sets Morissette apart from other Biriteras?”</i></p>
    <p style="font-size: 24px; font-weight:300; text-align: center;">  </p>
    <p style="font-size: 24px; font-weight:300; text-align: center; color:#9b3535;"><b>Everyone will give you different answers</b></p>
    '''
    col2.markdown(reasons, unsafe_allow_html=True)

def proposal():
    proposal = '<p style="font-size: 80px; font-weight:800; text-align: center;">Proposal</p>'
    st.markdown(proposal, unsafe_allow_html=True)

    caption = '''
    <p style="font-size: 40px; font-weight:400; text-align: left;">To craft a <b style="color:#1DB954;">sound so distinct</b> that even your lola knows it’s Morissette streaming on the radio.</p>
    <p style="font-size: 40px; font-weight:400; text-align: left;">    </p>
    <p style="font-size: 40px; font-weight:400; text-align: left;">We’ll do this by leveraging on Big Data and an even Bigger Marketing Campaign.</p>
    '''
    st.markdown(caption, unsafe_allow_html=True)

def tools():
    title = '<p style="font-size: 70px; font-weight:800; text-align: center;">Tools used for the project</p>'
    st.markdown(title, unsafe_allow_html=True)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')


    data_collection = '<p style="font-size: 35px; font-weight:800; text-align: left;">Data Collection:</p>'
    st.markdown(data_collection, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.image("images/jupyter.png", width=500)
    col2.image("images/spotify.png", width=500)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')


    eda = '<p style="font-size: 35px; font-weight:800; text-align: left;">Exploratory Data Analysis:</p>'
    st.markdown(eda, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.image("images/pandas.png", width=500)
    col2.image("images/numpy.png", width=500)
    col3.image("images/matplotlib.png", width=500)

    col1, col2 = st.columns(2)
    col1.image("images/jupyter.png", width=500)
    col2.image("images/spotify.png", width=500)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')


    machine_learning = '<p style="font-size: 35px; font-weight:800; text-align: left;">Machine Learning:</p>'
    st.markdown(machine_learning, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    col1.image("images/sklearn.png", width=500)
    col2.image("images/jupyter.png", width=500)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')


    deployment = '<p style="font-size: 35px; font-weight:800; text-align: left;">Deployment:</p>'
    st.markdown(machine_learning, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.image("images/studio code.png", width=500)
    col2.image("images/streamlit.png", width=500)
    col3.image("images/github.png", width=500)

    
def eda():
    playlist = '<p style="font-size: 70px; font-weight:800; text-align: center;">Exploratory Data Analysis</p>'
    st.markdown(playlist, unsafe_allow_html=True)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    col1, col2 = st.columns([1,2])
    col1.markdown(' ')
    col1.markdown(' ')
    col1.markdown(' ')
    col1.markdown(' ')
    col1.image("images/table.jpg")
    col2.image("images/chart.png", width=1000)

    col1, col2= st.columns([1,2])

    col1.markdown(' ')
    col1.markdown(' ')
    col1.markdown(' ')
    col1.markdown(' ')
    col1.markdown(' ')
    col1.markdown(' ')
    col1.markdown(' ')
    col1.markdown(' ')
    caption = '<p style="font-size: 30px; font-weight:400; text-align: center;">Explanation Here</p>'
    col1.markdown(caption, unsafe_allow_html=True)

    with col2:
        option1 = st.selectbox('Select an audio feature:',
            ['danceability', 'energy', 'loudness', 'speechiness', 'acousticness', 'instrumentalness','liveness', 'valence', 'tempo'], key = "0001")
            
        if option1 == "danceability":
            st.image("images/danceability.png", width=900)
            
        elif option1 == "energy":
            st.image("images/energy.png", width=900)

        elif option1 == "loudness":
            st.image("images/loudness.png", width=900)
            
        elif option1 == "speechiness":
            st.image("images/speechiness.png", width=900)
            
        elif option1 == "acousticness":
            st.image("images/acousticess.png", width=900)
            
        elif option1 == "instrumentalness":
            st.image("images/instrumentalness.png", width=900)
            
        elif option1 == "liveness":
            st.image("images/liveness.png", width=900)
            
        elif option1 == "valence":
            st.image("images/valence.png", width=900)
            
        elif option1 == "tempo":
            st.image("images/tempo.png", width=900)
def methodology():
    title = '<p style="font-size: 70px; font-weight:800; text-align: center;">Methodology</p>'
    st.markdown(title, unsafe_allow_html=True)


    st.image('images/methodology.jpg')

def recommender_engine():
    title = '<p style="font-size: 70px; font-weight:800; text-align: center;">Recommender Engine</p>'
    st.markdown(title, unsafe_allow_html=True)

        
def playlist():
    playlist = '<p style="font-size: 70px; font-weight:800; text-align: center;">Playlist</p>'
    st.markdown(playlist, unsafe_allow_html=True)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    st.markdown(
            '<p style="font-size: 36px; font-weight:800; text-align: center;">Playlist 1: Morissette</p>', unsafe_allow_html=True
        )
    st.markdown(
            '<p style="font-size: 24px; font-weight:800; text-align: center;">Seed Track: Akin Ka Na Lang</p>' , unsafe_allow_html=True
        )
    components.iframe("https://open.spotify.com/embed/track/4eNvchiaWf4Glh0AT2exds", height=80)
    components.iframe("https://open.spotify.com/embed/playlist/3wd1CPZgj0WyTCVrcQpqAL", height=380, scrolling=True)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    st.markdown(
            '<p style="font-size: 36px; font-weight:800; text-align: center;">Playlist 2: Taylor Swift</p>', unsafe_allow_html=True
        )
    st.markdown(
            '<p style="font-size: 24px; font-weight:800; text-align: center;">Seed Track: State of Grace (Acoustic Version) (Taylor\'s Version)</p>' , unsafe_allow_html=True
        )
    components.iframe("https://open.spotify.com/embed/track/5jAIouBES8LWMiriuNq170", height=80)
    components.iframe("https://open.spotify.com/embed/playlist/3IN3YG01BTCnPHvpThBs5p", height=380, scrolling=True)
    
def conclusion():
    title = '<p style="font-size: 70px; font-weight:800; text-align: center;">Insights and Recommendations</p>'
    st.markdown(title, unsafe_allow_html=True)

st.sidebar.markdown('<p style="font-size: 25px; font-weight:700; color:black; text-align: center;">Main Pages</p>', unsafe_allow_html=True)

list_of_pages = [
    "Morissette: Towards a new Birit-Era",
    "Morissette",
    "Morissette and competitors",
    "Proposal",
    "Tools",
    "Methodology",
    "EDA",
    "Recommender Engine",
    "Playlist",
    "Insights and Recommendations"
]
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Morissette: Towards a new Birit-Era":
    introduction()
elif selection == "Morissette":
    artist()
elif selection == "Morissette and competitors":
    artist_spotify()
elif selection == "Proposal":
    proposal()
elif selection == "Tools":
    tools()
elif selection == "EDA":
    eda()
elif selection == "Methodology":
    methodology()
elif selection == "Recommender Engine":
    recommender_engine()
elif selection == "Playlist":
    playlist()
elif selection == "Insights and Recommendations":
    conclusion()
