import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
from colorama import Fore, Style, init

init(autoreset=True)

df = pd.read_csv('imdb_top_1000.csv')

df['Overview'] = df['Overview'].fillna('')

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['Overview'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_index(title):
    return df[df['Series_Title'].str.lower() == title.lower()].index.values[0]

def recommend_movies(movie_title, num_recommendations=5):
    try:
        idx = get_index(movie_title)
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:num_recommendations+1]
        movie_indices = [i[0] for i in sim_scores]

        print(Fore.YELLOW + f"\nTop {num_recommendations} movies similar to '{movie_title}':")
        for i in movie_indices:
            display_movie(i)

    except IndexError:
        print(Fore.RED + "Movie not found. Please check the title.")

def display_movie(index):
    movie = df.iloc[index]
    print(Fore.CYAN + f"\nTitle: {movie['Series_Title']}")
    print(Fore.MAGENTA + f"Genre: {movie['Genre']}")
    print(Fore.GREEN + f"Rating: {movie['IMDB_Rating']}")
    print(Fore.BLUE + f"Overview: {movie['Overview']}")
    sentiment = TextBlob(movie['Overview']).sentiment
    print(Fore.YELLOW + f"Sentiment (Polarity): {sentiment.polarity:.2f}")

def random_movie():
    index = random.randint(0, len(df) - 1)
    print(Fore.LIGHTWHITE_EX + "\n🎲 Random Movie Selected:")
    display_movie(index)

if __name__ == "__main__":
    print(Fore.LIGHTWHITE_EX + "Welcome to the Movie Recommender!")
    user_input = input("Enter a movie title (or type 'random' to get a random movie): ")

    if user_input.strip().lower() == 'random':
        random_movie()
    else:
        recommend_movies(user_input.strip())