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