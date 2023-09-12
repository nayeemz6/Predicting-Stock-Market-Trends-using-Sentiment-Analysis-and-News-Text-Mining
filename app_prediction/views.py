from django.shortcuts import render
from django.http import JsonResponse
from .forms import PredictionForm
from .models import Prediction
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
from keras.models import load_model
import numpy as np
import nltk
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from joblib import load 
import os
from collections import Counter
import re

module_dir = os.path.dirname(__file__)  # get current directory
lstm_model_path = os.path.join(module_dir, 'new_lstm_model.h5')
feature_scaler_pkl = os.path.join(module_dir, 'feature_scaler.pkl')

def home(request):
    return render(request, 'home.html')

def faq(request):
    return render(request, 'faq.html')

def about(request):
    return render(request, 'about.html')

# Initialize
try:
    sid = SentimentIntensityAnalyzer()
    
except Exception as e:
    print(f"Error in initializing nltk or SentimentIntensityAnalyzer: {e}")

# Load your LSTM model and Scaler
try:
    lstm_model = load_model(lstm_model_path)
    with open(feature_scaler_pkl, 'rb') as f:
        feature_scaler = pickle.load(f)


except FileNotFoundError:
    print("The lstm_model.h5 or scaler.pkl file was not found.")
except Exception as e:
    print(f"An error occurred while loading the LSTM model or scaler: {e}")

def api_predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            try:
                headline = form.cleaned_data['headline']
                open_price = form.cleaned_data['open_price']
                high_price = form.cleaned_data['high_price']
                low_price = form.cleaned_data['low_price']
                volume = form.cleaned_data['volume']
                date = form.cleaned_data['date'] 
                # Sentiment Analysis
                sentiment_score = sid.polarity_scores(headline)
                vader_negative = sentiment_score['neg']
                vader_neutral = sentiment_score['neu']
                vader_positive = sentiment_score['pos']
                vader_compound = sentiment_score['compound']

                lda_topic=0
                # Create the Bag-of-Words representation of the headline
                words = re.findall(r'\w+', headline.lower())  # Tokenize and lowercase
                bag_of_words = Counter(words)

                # Prepare features
                features = np.array([[open_price, high_price, low_price, volume, vader_negative, vader_neutral, vader_positive, vader_compound, lda_topic]])

                # Scale the features
                # Scale the features
                features_scaled = feature_scaler.transform(features)

                # Reshape the features to (1, 1, 9)
                features_reshaped = np.reshape(features_scaled, (1, 1, 9))

                # Make the prediction
                prediction = lstm_model.predict(features_reshaped)

                # Convert NumPy float32 to Python native float
                prediction_float = float(prediction[0][0])
                response_data = {
                    'status': 'success',
                    'prediction': prediction_float,
                    'vader_negative': vader_negative,
                    'vader_neutral': vader_neutral,
                    'vader_positive': vader_positive,
                    'vader_compound': vader_compound,
                    'date': str(date),
                    'open_price': open_price,
                    'high_price': high_price,
                    'low_price': low_price,
                    'volume': volume,
                    'bag_of_words': bag_of_words
                }
                return JsonResponse(response_data)
            except Exception as e:
                return JsonResponse({'status': 'error', 'error': str(e)})
        else:
            return JsonResponse({'status': 'error', 'error': 'Form is not valid'})


