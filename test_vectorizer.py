import joblib

# Load your vectorizer
vectorizer = joblib.load('G:\\My Drive\\Arpita_Documents\\Guardian AI\\vectorizer.pkl')

# Example tweet for vectorization
processed_tweet = "i love programming!"  # Simulate preprocessed input
vectorized_tweet = vectorizer.transform([processed_tweet])
print(f"Vectorized tweet: {vectorized_tweet}")
