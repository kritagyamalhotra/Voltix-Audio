from textblob import TextBlob

def analyze_review_sentiment(text):
    """
    In a full implementation, this would load a .h5 Keras model.
    For the project demo, we use TextBlob which uses a pre-trained 
    Natural Language Processing model.
    """
    analysis = TextBlob(text)
    # Polarity is a score from -1.0 to 1.0
    if analysis.sentiment.polarity > 0.1:
        return 'Positive'
    elif analysis.sentiment.polarity < -0.1:
        return 'Negative'
    else:
        return 'Neutral'