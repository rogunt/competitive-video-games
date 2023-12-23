import streamlit as st
import requests

# Define Giant Bomb API endpoint and your API key
GIANT_BOMB_API_ENDPOINT = "https://www.giantbomb.com/api/games/"
GIANT_BOMB_API_KEY = "7bafcf044a6e38697c4c19b5db7c2f8f085f8f87"  # Replace with your actual Giant Bomb API key

# Function to fetch the top competitive games from Giant Bomb API
def fetch_top_games():
    params = {
        'api_key': '7bafcf044a6e38697c4c19b5db7c2f8f085f8f87',
        'format': 'json',
        'field_list': 'name,site_detail_url',
        'sort': 'original_release_date:desc',
        'filter': 'genres:8',  # Adjust the genre filter as needed (8 corresponds to the 'esports' genre)
        'limit': 10  # Adjust the limit as needed
    }
    response = requests.get(GIANT_BOMB_API_ENDPOINT + 'index/', params=params)
    st.write(response)
    data = response.json()
    return data.get('results', [])

# Streamlit app
def main():
    st.title("Top Competitive Video Games")

    # Fetch top competitive games
    top_games = fetch_top_games()

    # Display the list of games
    if top_games:
        st.write("Here are some of the top competitive video games:")
        for game in top_games:
            st.write(f"[{game['name']}]({game['site_detail_url']})")
    else:
        st.write("No data available. Please check your API key and parameters.")

if __name__ == "__main__":
    main()
