from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load your model and vectorizer
model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the tweet from the request
        data = request.get_json()
        tweet = data['tweet']
        print(f"Received tweet: {tweet}")

        # Preprocess the tweet
        if isinstance(tweet, str):
            processed_tweet = tweet.lower()  # Convert to lowercase
            print(f"Processed tweet: {processed_tweet}")
        else:
            raise ValueError("Tweet is not a string.")

        # Vectorize the tweet
        vectorized_tweet = vectorizer.transform([processed_tweet])
        print(f"Vectorized tweet: {vectorized_tweet}")

        # Make prediction
        prediction = model.predict(vectorized_tweet)
        print(f"Prediction: {prediction}")

        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
