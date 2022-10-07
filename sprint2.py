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
    subheader = '<p style="font-size: 80px; font-weight:800; text-align: center;">Morissette: A New “Birit” Era</p>'
    st.markdown(subheader, unsafe_allow_html=True)

    st.markdown(' ')
    st.markdown(' ')
    st.markdown(' ')

    col1, col2 = st.columns(2)

    col1.image('images\mori-singing.jpg')

    col2.markdown(' ')
    col2.markdown(' ')
    captions = '<p style="font-size: 50px; font-weight:700; color:#1DB954; text-align: center;">Why Morissette?</p>'
    col2.markdown(captions, unsafe_allow_html=True)
    col2.markdown(' ')
    col2.markdown(' ')

    reasons = '''
    <p style="font-size: 24px; font-weight:300; text-align: left;">    Despite being dubbed as <b style="color:#1DB954;">“Asia’s Phoenix”</b>, seasoned singer Morissette Amon only charted once in Spotify’s Top 200 and only for five days. </p>
    <p style="font-size: 24px; font-weight:300; text-align: left;">    A singer, songwriter, producer, actress, and artist, Morissette is almost like a household name. But why is she not topping charts as one would expect?</p>
    '''
    col2.markdown(reasons, unsafe_allow_html=True)

def artist():
    st.image("images\morissette.jpg", width=1500)
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
    <p style="font-size: 20px; font-weight:300; text-align: left;"> - Profile a </p>
    <p style="font-size: 20px; font-weight:300; text-align: left;"> - Profile b </p>
    <p style="font-size: 20px; font-weight:300; text-align: left;"> - Profile c </p>
    '''
    st.markdown(profile, unsafe_allow_html=True)

    related_artist = '<p style="font-size: 36px; font-weight:700; text-align: left;">Competitors:</p>'
    st.markdown(related_artist, unsafe_allow_html=True)
    col1, col2, col3, col4, col5= st.columns(5)

    col1.markdown(' ')
    col2.image("images/angeline.png", width=250, caption='Angeline Quinto')
    col3.image("images\jona.png", width=250, caption="Jona")
    col4.image("images\sarah.png", width=250, caption="Sarah Geronimo")
    col5.markdown(' ')
 

    st.write("[Tiktok](https://www.tiktok.com/@itsmorissette?lang=en)")
    st.write("[Facebook](https://www.facebook.com/MorissettePh/?_rdc=1&_rdr)")
    st.write("[Instagram](https://www.instagram.com/itsmorissette/)")
    st.write("[Website](https://amap.to/morissette/)")
   # st.write("https://open.spotify.com/track/0Dljpp52vCmtXi0E94qjfo?si=08ecbbca56f14f44")
    
def artist_spotify():
    #Munimuni info
    col1, col2 = st.columns(2)
    col1.image("images\morissette2.jpg")
    muni = '<p style="font-size: 50px; font-weight:700; text-align: center;">Morissette</p>'
    col2.markdown(muni, unsafe_allow_html=True)
    spotify = '<p style="font-size: 18px; font-weight:400; text-align: left;"><b>Spotify: </b> </p>'
    col2.markdown(spotify, unsafe_allow_html=True)
    twitter = '<p style="font-size: 18px; font-weight:400; text-align: left;"><b>Twitter:</b> </p>'
    col2.markdown(twitter, unsafe_allow_html=True)
    facebook = '<p style="font-size: 18px; font-weight:400; text-align: left;"><b>Facebook:</b> </p>'
    col2.markdown(facebook, unsafe_allow_html=True)
    instagram = '<p style="font-size: 18px; font-weight:400; text-align: left;"><b>Instagram:</b> </p>'
    col2.markdown(instagram, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")
    st.markdown("")

    related = '<p style="font-size: 50px; font-weight:800; text-align: center;">Related Artists</p>'
    st.markdown(related, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    #Ben&Ben info
    #col1.image("ben2.jpg")
    #ben = '<p style="font-size: 36px; font-weight:700; text-align: center;">Ben&Ben</p>'
    #col1.markdown(ben, unsafe_allow_html=True)
    #spotify = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>Spotify:</b> </p>'
    #col1.markdown(spotify, unsafe_allow_html=True)
    #twitter = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>Twitter:</b> </p>'
    #col1.markdown(twitter, unsafe_allow_html=True)
    #facebook = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>Facebook:</b> </p>'
    #col1.markdown(facebook, unsafe_allow_html=True)
    #instagram = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>Instagram:</b> </p>'
    #col1.markdown(instagram, unsafe_allow_html=True)

    #Autotelic info
    #col2.image("autotelic2.jpg")
    #auto = '<p style="font-size: 36px; font-weight:700; text-align: center;">Autotelic</p>'
    #col2.markdown(auto, unsafe_allow_html=True)
    #spotify = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>     Spotify:</b> </p>'
    #col2.markdown(spotify, unsafe_allow_html=True)
    #twitter = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>     Twitter:</b> </p>'
    #col2.markdown(twitter, unsafe_allow_html=True)
    #facebook = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>     Facebook:</b> </p>'
    #col2.markdown(facebook, unsafe_allow_html=True)
    #instagram = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>     Instagram:</b> </p>'
    #col2.markdown(instagram, unsafe_allow_html=True)

    #Up Dharma info
    #col3.image("up-dharma2.jpg")
    #dharma = '<p style="font-size: 36px; font-weight:700; text-align: center;">Up Dharma Down</p>'
    #col3.markdown(dharma, unsafe_allow_html=True)
    #spotify = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>Spotify:</b> </p>'
    #col3.markdown(spotify, unsafe_allow_html=True)
    #twitter = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>Twitter:</b> </p>'
    ##col3.markdown(twitter, unsafe_allow_html=True)
    #facebook = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>Facebook:</b> </p>'
    #col3.markdown(facebook, unsafe_allow_html=True)
    #instagram = '<p style="font-size: 16px; font-weight:400; text-align: left;"><b>Instagram:</b> </p>'
    #col3.markdown(instagram, unsafe_allow_html=True)

def eda():
    #st.image("taylor.jpg")
    data = load_data()
    #make duration ms to minutes
    taylor_df=data[
        data["artist_name"]=="Taylor Swift"]
    taylor_df['duration_mins']=taylor_df['duration']/60000

    plt.figure(figsize=(6,3), dpi=200)

    #Plot distribution chart
    ax = sns.distplot(taylor_df['duration_mins'], color='#1DB954')
    plt.title('Duration in Minutes', color='#1DB954', weight=700,fontsize=22)

    plt.ylabel('Frequency')
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    plot = plt.show()
    st.pyplot(plot)

    #Setting index for data
    streams_df = data.set_index('date')

    plt.figure(figsize=(6,3), dpi=200)

    #Histogram Plot
    ariana_df = streams_df[streams_df['artist'] == 'Ariana Grande']['2019-01-01':'2019-12-31']
    plt.hist(ariana_df['position'].values, 
            bins=np.arange(0, 210, 10),
            histtype='stepfilled', 
            label='Ariana Grande', 
            alpha=0.35,
            color="#1DB954")

    plt.title('Frequency in Position', color='#1DB954', weight=700,fontsize=22)
    plt.ylabel('Frequency')
    plt.xlabel('Position')

    plt.xticks([1]+np.arange(0, 210, 10).tolist(), size=10)
    plt.yticks(size=10)
    plt.xlim([200, 1])
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    plot = plt.show()
    st.pyplot(plot)

    #Multiple Histograms
    plt.figure(figsize=(6,3))
    ax = plt.subplot(111)

    for artist_name in ["Ariana Grande", "Dua Lipa", "Lady Gaga"]:
        artists_df = streams_df[(streams_df['artist'] == artist_name)]['2019-01-01':'2019-12-31']
        plt.hist(artists_df['position'].values, bins=np.arange(0, 210, 10),
                histtype='stepfilled', label=artist_name, alpha=0.35
                )

    plt.xticks([1]+np.arange(0, 210, 10).tolist())
    plt.xlim([200, 1])

    plt.ylabel('Frequency')
    plt.xlabel('Position')
    plt.legend(frameon=False)

    plot = plt.show()
    st.pyplot(plot)

    #Box plots
    kpop_girl_grps = ["BLACKPINK", "Girls' Generation-Oh!GG", "Girls' Generation-TTS",
                  "ITZY", "IZ*ONE", "MOMOLAND", "Red Velvet", "TWICE"]
    features = ["danceability", "energy", "valence", "tempo", "loudness"]

    columns_to_view = ['artist_name', 'track_name'] + features

    df_features = data[columns_to_view].copy()

    df_features['is_gg'] = ['kpop girl group' if artist in kpop_girl_grps else 'all else'
                        for artist in df_features['artist_name'].values]
    print(df_features.columns)

    # get max value for normalization
    max_tempo = df_features['tempo'].max()
    max_loudness = df_features['loudness'].min()

    # normalize tempo and loudness
    df_features['tempo']= df_features['tempo']/max_tempo
    df_features['loudness']= df_features['loudness']/max_loudness

    # set multiindex
    df_features = df_features.set_index(['track_name', 'artist_name', 'is_gg'])
    #df_features.stack()
    # reshape by pd.stack to achieve shape demanded by boxplot
    df_features_stacked = pd.DataFrame({'value': df_features.stack()})
    # # reset index
    df_features_stacked = df_features_stacked.reset_index()
    # # rename level_3
    df_features_stacked = df_features_stacked.rename(columns={'level_3': 'feature'})
    #df_features_stacked.head()

    plt.figure(figsize=(8, 6))
    ax = plt.subplot(111)

    sns.boxplot(data=df_features_stacked, x='feature', y='value',  hue='is_gg', ax=ax,
                hue_order=['kpop girl group', 'all else'],palette=['#f037a5', '#19e68c'],
                capprops=dict(color='white'),
                whiskerprops=dict(color='white'),
                flierprops=dict(color='white', markeredgecolor='white'),
                medianprops=dict(color='white')
                )

    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), frameon=False, ncol=3)

    show = plt.show()
    st.pyplot(show)

    #Heatmap
    df_bb = streams_df[streams_df['artist'] == "Ben&Ben"].groupby('track_name')[['streams']]\
    .resample('M').sum()
    df_bb = df_bb.reset_index()
    df_bb = df_bb[df_bb['date'] < '2021-01-31']
    # clean long titles
    df_bb['track_name'] = df_bb['track_name'].apply(lambda x: x.split('(')[0])\
        .apply(lambda x: x.split(' - ')[0])
    
    arr_df = df_bb.pivot(index='track_name', columns='date', values='streams')
    # divide by 1M to show streams in millions
    arr_df = arr_df/1000000
    arr_df.fillna(0, inplace=True)
    arr_df['total_streams'] = arr_df.sum(axis=1)

    plt.figure(figsize=(8, 6))
    ax = plt.subplot(111)

    # get all month columns and specify format for xticks
    moncols = arr_df.columns[:-1]
    yymm_cols = pd.Series(moncols.values).apply(lambda x: x.strftime('%Y-%m'))

    sns.heatmap(arr_df[moncols], ax=ax,
                cmap='viridis',
                cbar_kws={'label': 'million streams', 'ticks': np.arange(0, 8, 1)},
                xticklabels=yymm_cols, yticklabels=True)

    plt.ylabel('')
    plt.xlabel('')

    heat = plt.show()
    st.pyplot(heat)

    # get total yearly streams
    yr_df = streams_df['streams'].resample('Y').sum() #M for month
    yr_df.plot(kind='bar', color='#509bf5')
    plt.title("Yearly streams")

    year = plt.show()
    st.pyplot(year)

    #get total monthly streams
    mon_df = streams_df['streams'].resample('MS').sum() #M for month

    #line chart of monthly streams
    fig= plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    #default is line so you can omit kind= parameter
    mon_df.plot(ax=ax, kind='line', color='#eb1e32')

    #Uncomment for cleaner x labels
    #ax.set_xticklabels([x.strftime('%Y-%m') for x in mon_df.index])

    plt.ylabel('streams (in hundred millions)')
    plt.title('Spotify Monthly Total Streams')

    month = plt.show()
    st.pyplot(month)

    # month - previous month
    delta_mon_df = mon_df.diff()
    #line chart of monthly streams

    fig= plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    #default is line so you can omit kind= parameter
    #omit incomplete month
    delta_mon_df[:-1].plot(ax=ax, color='#1DB954')

    #Uncomment for cleaner x labels
    #ax.set_xticklabels([x.strftime('%Y-%m') for x in mon_df.index])

    #add reference line at y=0
    plt.axhline(0, color='#ffffff', ls='--')

    plt.ylabel('streams (in ten millions)')
    plt.title('Spotify Month-on-Month Stream Growth')

    diff = plt.show()
    st.pyplot(diff)

    #cumulative sum
    #line chart of monthly streams
    fig= plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    #default is line so you can omit kind= parameter
    cumsum = streams_df[streams_df['track_name']=='Kathang Isip']['streams'].resample('M').sum().cumsum()

    cumsum.plot(ax=ax,marker='o', color='#1DB954')
    #Uncomment for cleaner x labels
    #ax.set_xticklabels([x.strftime('%Y-%m') for x in mon_df.index])

    plt.ylabel('streams (in hundred millions)')
    plt.title('Spotify Monthly Total Streams')

    csum = plt.show()
    st.pyplot(csum)

    #more than 2 cumulative sum
    #line chart of monthly streams

    fig= plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111)
    #default is line so you can omit kind= parameter
    kathang_isip = streams_df[streams_df['track_name']=='Kathang Isip']['streams'].resample('M').sum().cumsum()
    shape_of_you = streams_df[streams_df['track_name']=='Shape of You']['streams'].resample('M').sum().cumsum()

    kathang_isip.plot(ax=ax, label='Ben&Ben- Kathang isip', color = "#1DB954")
    shape_of_you.plot(ax=ax, label='Ed Sheeran- Shape of You', color = '#eb1e32')
    #Uncomment for cleaner x labels
    #ax.set_xticklabels([x.strftime('%Y-%m') for x in mon_df.index])

    plt.legend()
    plt.ylabel('streams (in hundred millions)')
    plt.title('Spotify Monthly Total Streams')

    cum_sum = plt.show()
    st.pyplot(cum_sum)

    #Rolling sum
    fig = plt.figure(figsize=(13,4))
    ax = fig.add_subplot(111)

    kathang1 = streams_df[streams_df['track_name']=='Kathang Isip']['streams']
    kathang2 = streams_df[streams_df['track_name']=='Kathang Isip']['streams'].rolling(7).mean()

    kathang1.plot(ax=ax, label='raw', color = "#1DB954")
    kathang2.plot(ax=ax, label='smoothed', color = '#eb1e32')

    plt.legend()
    plt.ylabel('streams')
    plt.title('Spotify Daily Streams: Ben&Ben- Kathang isip')

    roll = plt.show()
    st.pyplot(roll)

    #Rolling mean
    fig = plt.figure(figsize=(6,3))
    ax = fig.add_subplot(111)

    kathangisip = streams_df[(streams_df.index.year>=2019)&(streams_df['track_name']=='Kathang Isip')]['streams'].rolling(7).mean()
    lover = streams_df[(streams_df.index.year>=2019)&(streams_df['track_name']=='Lover')]['streams'].rolling(7).mean()

    kathangisip.plot(ax=ax, label='Ben&Ben- Kathang isip', color="#1DB954")
    lover.plot(ax=ax, label='Taylor Swift- Lover', color = '#eb1e32')

    plt.legend()
    plt.ylabel('streams')
    plt.title('Spotify Daily Streams')
    
    roll2 = plt.show()
    st.pyplot(roll2)

    #Bounding margins
    fig,ax = plt.subplots(figsize=(16,4))
    easy_on_me = streams_df[(streams_df.index.year==2021)&(streams_df['track_name']=='Easy On Me')][['streams']]
    easy_on_me = easy_on_me['2021-08-30':]
    complete_dates = pd.DataFrame({'date':pd.date_range(easy_on_me.index.min(), easy_on_me.index.max())}).set_index('date')
    easy_on_me = complete_dates.join(easy_on_me, how='left').fillna(0)

    ax.plot(easy_on_me[:'2021-11-30'], marker='.')
    ax.plot(easy_on_me['2021-11-30':], marker='.')

    plt.ylim([150000,700000])
    ax.set_ylabel('streams')
    ax.set_title('Spotify Daily Streams: Adele - Easy on Me')

    adele = plt.show()
    st.pyplot(adele)

    fig = plt.figure(figsize=(13,4))
    ax = fig.add_subplot(111)

    data_bb = streams_df[(streams_df.index.year>=2019)&(streams_df['track_name']=='Kathang Isip')]['streams']
    ub_data = [data_bb.quantile(0.95)]*len(data_bb)
    lb_data = [data_bb.quantile(0.05)]*len(data_bb)

    plt.plot(data_bb, label='Ben&Ben- Kathang Isip', color="#4100F5")
    plt.fill_between(data_bb.index, lb_data,ub_data, color='#ffffff',alpha=0.5)
    plt.legend()
    plt.ylabel('streams')
    plt.title('Spotify Daily Streams')

    bb = plt.show()
    st.pyplot(bb)
def methodology():
    title = '<p style="font-size: 70px; font-weight:800; text-align: center;">Methodology</p>'
    st.markdown(title, unsafe_allow_html=True)

    st.image('images\methodology.jpg')

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
    components.iframe("https://open.spotify.com/embed/playlist/2rjCAavNHd1vQvWwsfYQw5", height=380, scrolling=True)
    st.markdown(
            "*Vibe With Me* was chosen due" , unsafe_allow_html=True
        )

def conclusion():
    title = '<p style="font-size: 70px; font-weight:800; text-align: center;">Insights and Recommendations</p>'
    st.markdown(title, unsafe_allow_html=True)

st.sidebar.markdown('<p style="font-size: 25px; font-weight:700; color:black; text-align: center;">Main Pages</p>', unsafe_allow_html=True)

list_of_pages = [
    "Morissette:A New “Birit” Era",
    "Morissette",
    "Morissette and competitors",
    "EDA",
    "Methodology",
    "Recommender Engine",
    "Playlist",
    "Insights and Recommendations"
]
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Morissette:A New “Birit” Era":
    introduction()
elif selection == "Morissette":
    artist()
elif selection == "Morissette and competitors":
    artist_spotify()
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
