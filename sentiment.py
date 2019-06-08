import numpy as np 
import pandas as pd 
import nltk 
import spacy
import gensim
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
from monkeylearn import MonkeyLearn
import json


def TextBlob_Sentiment(sentence):

    '''
    Polarity is float which lies in the range of [-1,1] where 1 means positive statement and -1 means a negative statement. 
    Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information. 
    Subjectivity is also a float which lies in the range of [0,1].
    '''
    sentence_blob = TextBlob(sentence)
    results = sentence_blob.sentiment
    # print(results)
    score = sentence_blob.sentiment.polarity
    label = ''
    if score < 0:
        label = 'Negative'
    elif score == 0:
        label = 'Neutral'

    else:
        label = 'Positive'
    scores = f'{label}, {abs(score)}'
    return(str(scores))

def Vader_Sentiment(sentence):

    '''
    The Positive, Negative and Neutral scores represent the proportion of text that falls in these categories. 
    This means our sentence was rated as 67% Positive, 33% Neutral and 0% Negative. Hence all these should add up to 1.
    The Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between 
    -1(most extreme negative) and +1 (most extreme positive)
    '''
    analyser = SentimentIntensityAnalyzer()
    results = analyser.polarity_scores(sentence)
    # print(results)
    score = results['compound']
    label = ''
    if score < 0:
        label = 'Negative'
    
    elif score == 0:
        label = 'Neutral'
    
    else:
        label = 'Positive'
    
    scores = f'{label}, {abs(score)}'
    return(str(scores))

def NLTK_Setiment(sentence):

    '''
    not offical.
    The english sentiment uses classifiers trained on both twitter sentiment as well as movie reviews from the data sets 
    created by Bo Pang and Lillian Lee using nltk-trainer (also on bitbucket). The dutch sentiment is based on book reviews.
    http://text-processing.com/docs/sentiment.html
    '''

    
    data = f'text={sentence}'
    r = requests.post('http://text-processing.com/api/sentiment/', data=data)

    results = r.json()
    # print(results)
    label = results['label']
    score = results['probability'][label]

    return(str(f'{label.capitalize()}, {score}'))
    


def MonkeyLearn_Sentiment(sentence):
    ml = MonkeyLearn('5264092dbceba6f1addde158d639df73dca9a0a5')
    data = [sentence]
    model_id = 'cl_pi3C7JiL'
    result = ml.classifiers.classify(model_id, data)
    results = result.body
    # print(results)
    label = results[0]['classifications'][0]['tag_name']
    score = results[0]['classifications'][0]['confidence']
    return (str(f'{label}, {score}'))

# if __name__ == "__main__":
    # sentence = "She made fun of him"
    # print(sentence)
    # print('\n')
    # print("Using TEXT BLOB")
    # TextBlob_Sentiment(sentence)

    # print('\n')
    # print("Using Vader")
    # Vader_Sentiment(sentence)

    # print('\n')
    # print("Using NLTK API")
    # NLTK_Setiment(sentence)

    # print('\n')
    # print("Monkey Learn API")
    # MonkeyLearn_Sentiment(sentence)