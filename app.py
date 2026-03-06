import streamlit as st
import pickle
import pandas as pd
import numpy as np

# data and loads
df=pickle.load(open('df.pkl','rb'))
df=pd.DataFrame(df)
similarity=pickle.load(open('similarity.pkl','rb'))

#functions

def recommend(movie):
    index=df[df['title'] == movie].index[0]
    distances=similarity[index]
    movies=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    for i in movies:
        movie_id=df.iloc[i[0]].movie_id
        recommended_movies.append(df.iloc[i[0]].title)
    return recommended_movies    

st.title('Movie Recommendor System')
selected_movie=st.selectbox(
    'Select your movie',df['title'].values)
if st.button('Recommend'):
    recommendations=recommend(selected_movie)
    for i in recommendations:
        st.write(i)