import streamlit as st
import requests
import pandas as pd

# Function to fetch games from RAWG API
@st.cache_data
def fetch_games(genre):
    api_key = st.secrets['api_key']
    url = f"https://api.rawg.io/api/games?key={api_key}&genres={genre}"
    response = requests.get(url)
    return response.json()

# Streamlit app layout
st.title('Competitive Video Games Dashboard')

# Select genre
genre = st.selectbox("Select a Game Genre:", ['action', 'strategy', 'shooter', 'sports'])

# Fetch and display games
data = fetch_games(genre)
if 'results' in data:
    games = data['results']
    for game in games:
        st.subheader(game['name'])
        st.write(f"Released: {game['released']}")
        st.write(f"Rating: {game['rating']}/5")
        if game['background_image']:
            st.image(game['background_image'])
