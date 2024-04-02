import streamlit as st
import pandas as pd

st.title("Movie Reccomendation System")

path = 'MovieLens 20M Dataset/'

#import datatsets
#movie = pd.read_csv(path + 'movie.csv')
#rating = pd.read_csv(path + 'rating.csv')
movie_rating = pd.read_csv(path + 'movie_rating.csv')

#merge
#og_movie_rating = pd.merge(movie,rating, on = 'movieId')
#movie_rating = og_movie_rating.sample(n=1000)

#preprocess data: replace any NaN values with a blank
#movie_rating.fillna('')

#drop duplicates
#movie_rating = movie_rating.drop_duplicates(subset = 'title', keep = 'first')

genres = set()

#add each genre to the empty list 
for genre in movie_rating['genres']:
  genre_list = genre.split("|")
  genres.update(genre_list)

selected_genres = st.multiselect("Select genre(s)", genres)
selected_rating = st.select_slider('Select a rating', ['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5'])
generate_button = st.button('Generate!')

#for genre in genres:
  #movie_rating[genre] = movie_rating['genres'].apply(lambda x:1 if genre in x.split("|") else 0)

def display_recommendations(df, selected_genres, selected_rating):
    if selected_genres and selected_rating:
        selected_rating = float(selected_rating)
        filtered_movies = df[(df[selected_genres].sum(axis=1) > 0) & (df['rating'] >= selected_rating)]
        if not filtered_movies.empty:
            st.write(filtered_movies['title'])
        else:
            st.write("No movies found with the selected criteria.")

if generate_button:
    st.balloons()
    display_recommendations(movie_rating, selected_genres, selected_rating)
   
        
