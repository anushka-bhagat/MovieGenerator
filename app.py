import streamlit as st
import pandas as pd

st.title("🌟Movie Reccomendation System🌟")
st.markdown("Feeling indecisive? Let me handle that! Select your favorite genres and a preferred rating, then hit generate! 🍿🌟")

#path = 'MovieLens 20M Dataset/'

#import datatsets
#movie = pd.read_csv(path + 'movie.csv')
#rating = pd.read_csv(path + 'rating.csv')
movie_rating = pd.read_csv('movie_rating.csv')

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

st.header("Filters:")
selected_genres = st.multiselect("Select Genre(s)", genres)
selected_rating = float(st.select_slider('Select a Rating', ['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5']))
generate_button = st.button('Generate!')

#for genre in genres:
  #movie_rating[genre] = movie_rating['genres'].apply(lambda x:1 if genre in x.split("|") else 0)

def display_recommendations(df, selected_genres, selected_rating):
    if selected_genres and selected_rating:
        selected_rating = float(selected_rating)
        
        filtered_movies = df[(df[selected_genres].sum(axis=1) == len(selected_genres)) & (df['rating'] >= selected_rating)]
        
        if not filtered_movies.empty:
            st.balloons()
            
            output = filtered_movies[['title','genres','rating']].style.format({'rating': '{:.1f}'}).hide_index()
            st.table(output)
        else:
            st.error("No Novies Found :(")

    else:
        st.warning("Please select a genre and rating to proceed...")

if generate_button:
    display_recommendations(movie_rating, selected_genres, selected_rating)
   
          
