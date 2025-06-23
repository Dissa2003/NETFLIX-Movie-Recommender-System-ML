import streamlit as st
import pickle
import requests


movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list=movies['title'].values

st.header("Movie Recommender System")

selectvalue=st.selectbox("Select movie from dropdown", movies_list)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path


def recommand(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommand_movie=[]

    for i in distance[0:5]:
          recommand_movie.append(movies.iloc[i[0]].title)

    return recommand_movie

if st.button("Show Recommend"):
    movie_name = recommand(selectvalue)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(movie_name[0])
       
    with col2:
        st.text(movie_name[1])
       
    with col3:
        st.text(movie_name[2])
        
    with col4:
        st.text(movie_name[3])
        
    with col5:
        st.text(movie_name[4])
       