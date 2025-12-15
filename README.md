# Book Recommendation System

##  Project Overview

This project is a **Book Recommendation System** built using **Machine Learning** techniques and deployed with **Streamlit**. The system recommends books to users based on popularity and content similarity, helping users discover books aligned with their interests.

The focus of this project is on **recommendation logic, data preprocessing, and model implementation**.

---

##  Objectives

* Build a functional book recommendation engine
* Implement **popularity-based** and **content-based** recommendation approaches
* Handle basic **cold-start** scenarios
* Deploy the model using a simple and interactive Streamlit interface

---

##  Recommendation Approaches Used

### 1. Popularity-Based Recommendation

* Recommends books based on average ratings and number of reviews
* Used to show **Trending Books**
* Suitable for new users with no prior interaction data (cold start)

### 2. Content-Based Recommendation

* Uses book metadata (such as title, authors, description)
* Vectorization performed using techniques like **TF-IDF / Count Vectorizer**
* Similarity computed using **Cosine Similarity**
* Recommends books similar to a user-selected book

---

##  Project Structure

```
BOOK_RECOMMENDATION_SYSTEM/
│
├── data/
│   ├── book.csv                  # Raw dataset
│   ├── cleaned_books.csv         # Preprocessed dataset
│   ├── cosine_sim.pkl            # Precomputed cosine similarity matrix
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_data_preprocessing.ipynb
│   ├── 03_popularity_based.ipynb
│   ├── 04_content_based.ipynb
│
├── src/
│   ├── app.py                    # Streamlit application
│   ├── recommender.py            # Recommendation logic
│
├── README.md
├── requirements.txt
```

---

##  Tech Stack

* **Python**
* **Pandas** – data handling
* **NumPy** – numerical operations
* **Scikit-learn** – vectorization & cosine similarity
* **Streamlit** – web application

---

##  How to Run the Project

### Option 1: Run Locally

1. Clone the repository
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run src/app.py
```

4. Open the browser URL shown in the terminal

### Option 2: Live Demo (Deployed)

The application is deployed using **Streamlit Community Cloud**.

**Live Demo:** *Add your Streamlit app link here after deployment*

---

##  Dataset

* The dataset contains information about books such as:

  * Title
  * Authors
  * Average rating
  * Image URL
  * .. and other fields
* The raw dataset is cleaned and preprocessed before model building

---

##  Key Learnings

* Understanding recommendation system design
* Handling cold-start problems using popularity-based methods
* Implementing cosine similarity for content-based filtering
* Structuring ML projects for real-world usage

---

##  Limitations

* No collaborative filtering (requires user interaction data)
* Recommendations depend on available metadata
* UI is intentionally minimal, focusing on ML functionality

---

##  Future Improvements

* Hybrid recommendation system
* User-based collaborative filtering
* User login & interaction tracking
* Improved UI and filtering options

---

##  Author

**Vaishnavi Mishra**

---