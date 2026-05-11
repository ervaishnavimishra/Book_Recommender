import pandas as pd
import pickle
import streamlit as st
from recommender import get_top_popular_books, recommend_books

# Load cleaned dataset
df = pd.read_csv("../data/cleaned_books.csv")

# Load precomputed cosine similarity matrix
with open("../data/cosine_sim.pkl", "rb") as f:
    cosine_sim = pickle.load(f)


#Streamlit UI
st.title("Book Recommendation System")

# Section 1: Trending books
st.header("Trending Books")
top_books = get_top_popular_books(df, n=10)

cols = st.columns(5)  # 5 books per row
for i, (idx, row) in enumerate(top_books.iterrows()):
    with cols[i % 5]:  # wrap every 5 books into a new row
        st.image(row.image_url, width=120)
        st.write(f"**{row.title}**")
        st.write(f"by {row.authors}")
        st.write(f"Rating: {row.average_rating}⭐")
        
st.markdown("---")

# Section 2: Recommended for You
st.header("Recommended for You")
book_input = st.text_input("Enter a book title you like:")

if book_input:
    recommendations = recommend_books(book_input, df, cosine_sim, top_n=20)
    
    if isinstance(recommendations, str):
        st.warning(recommendations)
    else:
        cols = st.columns(5)
        for i, (idx, row) in enumerate(recommendations.iterrows()):
          with cols[i % 5]:
            st.image(row.image_url, width=120)
            st.write(f"**{row.title}**")
            st.write(f"by {row.authors}")
            st.write(f"Rating: {row.average_rating}⭐")

