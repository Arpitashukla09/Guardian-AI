# Guardian AI - Hate Speech Detection API

## Project Description
Guardian AI is a Flask-based web service that detects hate speech in tweets. It leverages machine learning models to analyze the content of tweets and provides predictions on whether they contain hate speech or not.

## How to Use the API
You can interact with the API by sending POST requests to the `/predict` endpoint.

## Example Request
```bash
curl -X POST https://guardian-ai.onrender.com/predict -H "Content-Type: application/json" -d '{"tweet": "I hate everyone"}'

## Response
{
    "prediction": [0]  // 0 indicates hate speech, 1 indicates no hate speech
}

## Technologies Used:-
1. Flask: Web framework for building the API
2. scikit-learn: Machine learning library for model training and predictions
3. joblib: For loading pre-trained models
4. Requests: For handling HTTP requests


## Instructions for Running the Project Locally:-
1. Clone the repository:

git clone https://github.com/Arpitashukla09/Guardian-AI.git
cd Guardian-AI

2. Set up a virtual environment:
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On macOS/Linux

3. Install the required packages:
pip install -r requirements.txt

4. Run the Flask app:
python app.py

5. Make a POST request to http://127.0.0.1:5000/predict with a sample tweet.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


