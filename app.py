import streamlit as st
import pickle
import pandas as pd
import requests

# Load the .pkl files
movies_list = pickle.load(open('movies.plk', 'rb'))
similarity = pickle.load(open('similarity.plk', 'rb'))

# TMDB API Key
API_KEY = "ffec32b4a92eff6bebd735bb78c101ec"

# Function to fetch movie poster
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        response = requests.get(url, timeout=5)  # Timeout to avoid hanging
        response.raise_for_status()
        data = response.json()
        if "poster_path" in data and data["poster_path"]:
            poster_path = data["poster_path"]
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
        else:
            return None  # Return None if the poster is not available
    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred while fetching poster: {e}")
        return None

# Function to recommend movies
def recommend(movie):
    try:
        movie_index = movies_list[movies_list['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list_similar = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_posters = []
        for i in movies_list_similar:
            movie_id = movies_list.iloc[i[0]].movie_id
            if movies_list.iloc[i[0]].title not in recommended_movies:  # Avoid duplicates
                recommended_movies.append(movies_list.iloc[i[0]].title)
                recommended_posters.append(fetch_poster(movie_id))
        return recommended_movies, recommended_posters
    except IndexError:
        st.error("Movie not found in the dataset.")
        return [], []

# Streamlit App
st.title("Movie Recommender System")

# Dropdown to select a movie
selected_movie = st.selectbox(
    "Choose a movie",
    movies_list['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie)

    # Display movies in a single row with posters
    cols = st.columns(len(names))  # Dynamically create columns based on the number of recommendations
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])  # Display movie name
            if posters[idx]:  # If there is a valid poster URL, display the poster image
                st.image(posters[idx], use_container_width=True)  # Use container width instead
            else:
                st.text("Poster not available")  # Display message if poster is not available

