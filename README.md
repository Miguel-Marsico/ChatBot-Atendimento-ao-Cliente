<h1>
    Chatbot de atendimento ao cliente🤖
</h1>

![image](https://github.com/Miguel-Marsico/Customer-Service-ChatBot/assets/158609724/3006dff5-3f15-41e5-a4aa-7370cc9b45b8)
![image](https://github.com/Miguel-Marsico/Customer-Service-ChatBot/assets/158609724/51ed029e-ec9e-4465-aefa-7c3cf215953b)

 ## 📋 Topics
<div>
 • <a href="#-sobre">Sobre</a> </br>
 • <a href="#-ferramentas">Ferramentas</a> </br>
 • <a href="#-como-executar-esse-projeto">Como Executar esse projeto</a> </br>    
 • <a href="#-licença">Licença</a></br>
</div>

## 📗 Sobre

Este projeto é um modelo de **ChatBot** treinado para **atendimento ao cliente** com **TensorFlow Keras**.

## 🔧 Ferramentas

### 💻 Website ( HTML + CSS + JavaScript )

### 🔄 **API** ([Pyhton](https://www.python.org))

- [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/#python-version)
- [Numpy]( https://numpy.org)
- [TensorFlow Keras](https://www.tensorflow.org/guide/keras?hl=pt-br)
- [Spacy](https://spacy.io)
- [Pickle](https://docs.python.org/3/library/pickle.html)

### 🛠️ **Utilitários** 

- Compiladores: **[Pycharm Community](https://www.jetbrains.com/pt-br/pycharm/)** 

## ▶ Como Executar esse projeto
### O projeto está dividido em **3** partes:

 - 🌐 **Frontend** (WebSite HTML, CSS, JavaScript)
 - ⚙️ **Backend: ChatBot e Api** (Python)
 - ⚙️ **Backend: Treinamento** (Python, JSON)

💡 Usar um **ambiente virtual Python (venv)** é essencial para isolar e gerenciar dependências do projeto de maneira segura e reproduzível.

### ⚙️ main_chatbot.py:

#### Crie um ambiente virtual:

1 - Navegue até o diretório onde deseja criar o ambiente virtual:
```bash
 cd /path/to/your/project
```
2 - Crie um ambiente virtual:
```bash
 python3 -m venv name
```
3 - Ative o ambiente virtual:
```bash
 name\Scripts\activate
```

#### Instalação de bibliotecas:

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

#### Importação de bibliotecas:
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

#### Importação de bibliotecas:
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

Neste arquivo estão todas as **perguntas** e **respostas** que serão utilizadas para **treinar o ChatBot**.

### 🌐 Frontend:

Um arquivo **HTML** é usado como interface, sendo automaticamente reconhecido pelo **Flask** e executado ao executar a **API**.

## 📜 Licença

### Este projeto está sob licença do MIT. 
<br>

Desenvolvido por Miguel Marsico 👋🏻
