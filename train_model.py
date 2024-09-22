from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Sample data
X = ["i love programming", "i hate bugs", "i enjoy learning", "i dislike errors"]
y = [1, 0, 1, 0]  # Labels: 1 = Positive, 0 = Negative

# Vectorizer and Model
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

# Save model and vectorizer
joblib.dump(model, 'model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')

print("Model and vectorizer saved successfully!")
