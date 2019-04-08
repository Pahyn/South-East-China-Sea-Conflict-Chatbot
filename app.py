<<<<<<< HEAD
from flask import Flask
from flask import render_template,jsonify,request
import requests
from models import *
import random

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat',methods=['POST'])
def chat():
    try:
        user_message = request.form["text"]
        response = requests.get("http://localhost:5005/conversations/default/respond",params={"q":user_message})
        response = response.json()  
        print(response)
        x = response[0]

        if len(x)==2:
            text = x['text']
            return jsonify({"status":"success","response":text})
        else:
            text = x['text']
            image = x['image']
            return jsonify({"status":"success","response":text,"image":image})
        #return 'OK'
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)
=======
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", storage_adapter="chatterbot.storage.SQLStorageAdapter")

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()
>>>>>>> 6af9671b43f5ac0055ede7da71e563b59f277d6e
