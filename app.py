import pickle
import streamlit as st
import numpy as np

# Render page heading
st.header("Book Recommender System using Machine Learning")

# Load pickle files
model = pickle.load(open("artifacts/model.pkl", "rb"))
book_names = pickle.load(open("artifacts/book_names.pkl", "rb"))
final_ratings = pickle.load(open("artifacts/final_ratings.pkl", "rb"))
book_pivot = pickle.load(open("artifacts/book_pivot.pkl", "rb"))

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
    
    for name in book_name[0]:
        ids = np.where(final_ratings["title"] == name)[0][0]
        ids_index.append(ids)
    
    for idx in ids_index:
        url = final_ratings.iloc[idx]["img_url"]
        poster_url.append(url)

    return poster_url

def recommend_book(book_name):
    book_list = []
    book_id  = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fetch_poster(suggestion)


    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            book_list.append(j)

    return book_list, poster_url
selected_books = st.selectbox(
    "Type or select a book",
    book_names
)
if st.button("Get Recommendations"):
    recommendations_books, poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendations_books[1])
        st.image(poster_url[1])
    
    with col2:
        st.text(recommendations_books[2])
        st.image(poster_url[2])

    with col3:
        st.text(recommendations_books[3])
        st.image(poster_url[3])


    with col4:
        st.text(recommendations_books[4])
        st.image(poster_url[4])

    with col5:
        st.text(recommendations_books[5])
        st.image(poster_url[5])

print(selected_books)


