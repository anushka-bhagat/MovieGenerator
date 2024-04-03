import streamlit as st
import pandas as pd


# Import dataset
movie_rating = pd.read_csv('movie_rating.csv')

st.title("🌟Movie Recommendation System🌟")
st.markdown("Feeling indecisive? Let me handle that! Select your favorite genres and a preferred rating, then hit generate! 🍿🌟")

#split up and create set of genres
genres = set()
for genre in movie_rating['genres']:
  genre_list = genre.split("|")
  genres.update(genre_list)

#prompt user to enter filters
st.header("Filters:")
selected_genres = st.multiselect("Select Genre(s)", genres)
selected_rating = float(st.select_slider('Select a Rating', ['0', '0.5', '1', '1.5', '2', '2.5', '3', '3.5', '4', '4.5', '5']))
generate_button = st.button('Generate!')

def display_recommendations(df, selected_genres, selected_rating):
   
    #if user enters both fields
    if selected_genres and selected_rating:
        #convert to float
        selected_rating = float(selected_rating)
        
        #check if all genres are present in a movie and the rating is >= chosen rating
        filtered_movies = df[(df[selected_genres].sum(axis=1) == len(selected_genres)) & (df['rating'] >= selected_rating)]
        
        #display reccomendations if there are results
        if not filtered_movies.empty:

            #balloons to celebrate!
            st.balloons()
            st.write("Your Personalized Reccomendations:")

            #format ratings to 1 decimal place
            filtered_movies['rating'] = filtered_movies['rating'].apply(lambda x: f'{x:.1f}')  # Format to 1 decimal place
            #display a table with the movie titles, genres, and ratings
            st.table(filtered_movies[['title', 'genres', 'rating']])

        else:
            st.error("No Novies Found :(")

    else:
        st.warning("Please select a genre and rating to proceed...")

if generate_button:
    display_recommendations(movie_rating, selected_genres, selected_rating)
   
