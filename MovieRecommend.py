import streamlit as st
import pickle
import requests
import pandas as pd

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=201403eb002084d8e7fdfb32cbe52830&append_to_response=videos'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['poster_path']

def fetch_description(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=201403eb002084d8e7fdfb32cbe52830&append_to_response=videos'.format(movie_id))
    data = response.json()
    description = data.get('overview')
    return description

def fetch_rating(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=201403eb002084d8e7fdfb32cbe52830&append_to_response=videos'.format(movie_id))
    data = response.json()
    rating_taken = data.get('vote_average')
    rating = round(rating_taken,1)
    return rating

def fetch_genre(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=201403eb002084d8e7fdfb32cbe52830&append_to_response=videos')
    data = response.json()
    genres = data.get('genres', [])
    genre_names = [genre['name'] for genre in genres]
    return ", ".join(genre_names)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movies_poster = []
    actors = []
    description = []
    genre = []
    rating = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
#        actors.append(fetch_actor(movie_id))
        description.append(fetch_description(movie_id))
        genre.append(fetch_genre(movie_id))
        rating.append(fetch_rating(movie_id))
    return recommended_movies, recommended_movies_poster,description,genre,rating


st.header('Movie Recommender System')
selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)
if st.button('Recommend',type="primary"):
    recommended_movie_names,recommended_movie_posters,description,genre,rating = recommend(selected_movie)
    col1, col2, col3, col4, col5  = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        with st.popover(recommended_movie_names[0]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[0])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[0])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[0])
    with col2:
        st.image(recommended_movie_posters[1])
        with st.popover(recommended_movie_names[1]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[1])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[1])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[1])
    with col3:
        st.image(recommended_movie_posters[2])
        with st.popover(recommended_movie_names[2]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[2])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[2])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[2])
    with col4:
        st.image(recommended_movie_posters[3])
        with st.popover(recommended_movie_names[3]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[3])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[3])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[3])
    with col5:
        st.image(recommended_movie_posters[4])
        with st.popover(recommended_movie_names[4]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[4])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[4])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[4])
    st.write('  \n')
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.image(recommended_movie_posters[5])
        with st.popover(recommended_movie_names[5]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[5])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[5])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[5])
    with col7:
        st.image(recommended_movie_posters[6])
        with st.popover(recommended_movie_names[6]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[6])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[6])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[6])
    with col8:
        st.image(recommended_movie_posters[7])
        with st.popover(recommended_movie_names[7]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[7])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[7])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[7])
    with col9:
        st.image(recommended_movie_posters[8])
        with st.popover(recommended_movie_names[8]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[8])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[8])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[8])
    with col10:
        st.image(recommended_movie_posters[9])
        with st.popover(recommended_movie_names[9]):
            st.markdown('<u><b>Description</b></u>', unsafe_allow_html=True)
            st.markdown(description[9])
            st.markdown('<u><b>Genres</b></u>', unsafe_allow_html=True)
            st.markdown(genre[9])
            st.markdown('<u><b>Rating</b></u>', unsafe_allow_html=True)
            st.markdown(rating[9])
