
#popularity based
def get_top_popular_books(df, n=10):
    """
    Returns top n books sorted by average rating.
    """
    popular_books = (
        df[['title', 'authors', 'average_rating','image_url']]
        .sort_values(by='average_rating', ascending=False)
        .head(n)
    )
    return popular_books


#content based
def recommend_books(title, df, cosine_sim, top_n):
    matches = df[df['title'].str.contains(title, case=False, na=False)]

    if matches.empty:
        return "No matching books found."

    idx = matches.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    book_indices = [i[0] for i in sim_scores[1:top_n+1]]

    return df.iloc[book_indices][['title', 'authors', 'average_rating','image_url']]

