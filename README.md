<h1>
    Customer-Service-ChatBot 🤖
</h1>

![image](https://github.com/Miguel-Marsico/Customer-Service-ChatBot/assets/158609724/3006dff5-3f15-41e5-a4aa-7370cc9b45b8)
![image](https://github.com/Miguel-Marsico/Customer-Service-ChatBot/assets/158609724/51ed029e-ec9e-4465-aefa-7c3cf215953b)

 ## 📋 Topics
<div>
 • <a href="#-about">About</a> </br>
 • <a href="#-tools">Tools</a> </br>
 • <a href="#-how-to-execute-the-project">How to execute the project</a> </br>    
 • <a href="#-license">License</a></br>
</div>

## 📗 About

This project is a **ChatBot** model trained for **customer service** with **TensorFlow Keras**.

## 🔧 Tools

### 💻 Website ( HTML + CSS + JavaScript )

### 🔄 **API** ([Pyhton](https://www.python.org))

- [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#python-version)
- [Numpy]( https://numpy.org)
- [TensorFlow Keras](https://www.tensorflow.org/guide/keras?hl=pt-br)
- [Spacy](https://spacy.io)
- [Pickle](https://docs.python.org/3/library/pickle.html)

### 🛠️ **Utilities** 

- Compilers: **[Pycharm Community](https://www.jetbrains.com/pt-br/pycharm/)** 

## ▶ How to execute the project
### The project is divided into **3** parts:

 - 🌐 **Frontend** (WebSite HTML, CSS, JavaScript)
 - ⚙️ **Backend: ChatBot and Api** (Python)
 - ⚙️ **Backend: Training** (Python, JSON)

💡 Using a **Python virtual environment (venv)** is essential to isolate and manage project dependencies in a secure and reproducible manner.

### ⚙️ main_chatbot.py:

#### Create a venv:

1 - Navigate to the directory where you want to create the virtual environment:
```bash
 cd /path/to/your/project
```
2 - Create virtual environment:
```bash
 python3 -m venv name
```
3 - Activate the virtual environment:
```bash
 name\Scripts\activate
```

#### Installing libraries:

```bash
 pip install Flask
```
```bash
 pip install numpy
``` 
```bash
 pip install pickle
```
```bash
 pip install spacy
```
```bash
 pip install tensorflow
```

#### Library import:
```bash
 from flask import Flask, request, jsonify, render_template
 import random
 import json
 import pickle
 import numpy as np
 import spacy
 from tensorflow.keras.models import load_model
```
### ⚙️ training.py:

#### Library import:
```bash
 import random
 import json
 import pickle
 import numpy as np
 import spacy
 from tensorflow.keras.models import Sequential
 from tensorflow.keras.layers import Dense, Dropout
 from tensorflow.keras.optimizers import SGD
```

### 📖 intents.json:

In this file all the **questions** and **answers** that will be used to **train the ChatBot**.

### 🌐 Frontend:

An **HTML** file is used as an interface, being automatically recognized by **Flask** and executed when running the **API**.

## 📜 License

### This project is under the MIT license. 
<br>
Developed by Miguel Marsico 👋🏻
