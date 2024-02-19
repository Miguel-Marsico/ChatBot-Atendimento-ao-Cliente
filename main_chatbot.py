# Import necessary libraries
from flask import Flask, request, jsonify, render_template
import random
import json
import pickle
import numpy as np
import spacy
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Load NLP model, intents, words, classes, and the chat model
nlp = spacy.load("pt_core_news_sm")
intents = json.loads(open('intents.json', encoding='utf-8').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chat_model.h5')

# Define function to preprocess sentences
def clean_up_sentence(sentence):
    sentence_words = [token.lemma_ for token in nlp(sentence)]
    return sentence_words

# Define function to create a bag of words
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

# Define function to predict the class of a sentence
def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list

# Define function to get a response based on the predicted intent
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

# Define route for the homepage
@app.route('/')
def home():
    return render_template('chat.html')

# Define route for processing chat messages
@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message')
    ints = predict_class(message)
    res = get_response(ints, intents)
    return jsonify({'response': res})  

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
