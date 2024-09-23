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

## Live Demo

You can access the live demo of the Hate Speech Detection API at [https://guardian-ai.onrender.com](https://guardian-ai.onrender.com).

## Testing the API with Postman

You can test the Hate Speech Detection API using Postman by following these steps:

1. **Open Postman**.
   
2. **Create a New Request**:
   - Click on the **"New"** button in the top left corner.
   - Select **"Request"** from the dropdown.

3. **Set Request Type to POST**:
   - In the dropdown next to the URL input field, select **"POST"**.

4. **Enter the URL**:
   - Input the following URL in the request URL field: 
     ```
     https://guardian-ai.onrender.com/predict
     ```

5. **Go to the Body Tab**:
   - Click on the **"Body"** tab below the URL input field.

6. **Select Raw and Set Type to JSON**:
   - Choose **"raw"** from the options.
   - In the dropdown next to the raw option, select **"JSON"**.

7. **Enter the JSON Data**:
   - Input the following JSON in the text area:
     ```json
     {
         "tweet": "I hate everyone"
     }
     ```

8. **Click Send**:
   - Press the **"Send"** button to make the request.

9. **Check the Response**:
   - After sending the request, check the response in the lower section of Postman. You should see the prediction returned by the API.

### Deployment Image
![Deployment Image](https://github.com/Arpitashukla09/Guardian-AI/blob/master/Deployment.jpg)

### Sending a Request Using Postman
![Sending Postman Request](https://github.com/Arpitashukla09/Guardian-AI/blob/master/Sending%20Postman%20Request)

### API Generating Page
![API Generating Page](https://github.com/Arpitashukla09/Guardian-AI/blob/master/live%20demo.jpg)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


