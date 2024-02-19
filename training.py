# Import necessary libraries
import random
import json
import pickle
import numpy as np  
import spacy
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

# Load the Portuguese language model from spaCy
nlp = spacy.load("pt_core_news_sm")

# Load intents from a JSON file
with open('intents.json', encoding='utf-8') as file:
    intents = json.load(file)

# Initialize lists to hold words, classes, and document patterns
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

# Process each intent in the JSON file
for intent in intents['intents']:
    for pattern in intent['patterns']:
        doc = nlp(pattern)
        word_list = [token.lemma_ for token in doc if token.text not in ignore_letters]
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Remove duplicates and sort words and classes
words = sorted(set(words))
classes = sorted(set(classes))

# Save words and classes to binary files for later use
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Initialize training data
train_x = []
train_y = []

# Create an empty output list for each class
output_empty = [0] * len(classes)

# Prepare training data
for document in documents:
    bag = []
    pattern_words = [word.lower() for word in document[0]]
    for word in words:
        bag.append(1 if word in pattern_words else 0)

    # Set the appropriate class for each pattern
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1

    # Add the bag of words and class to training data
    train_x.append(bag)
    train_y.append(output_row)

# Shuffle training data and split into inputs and outputs
training_data = list(zip(train_x, train_y))
random.shuffle(training_data)
train_x, train_y = zip(*training_data)

# Convert lists to numpy arrays for training
train_x = np.array(train_x)
train_y = np.array(train_y)

# Define the neural network model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Configure the model for training
sgd = SGD(lr=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# Train the model
hist = model.fit(train_x, train_y, epochs=2700, batch_size=5, verbose=1)

# Save the trained model
model.save('chat_model.h5', hist)

print("Ready")
