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

        if len(response)==1:
            x = response[0]
            text = x['text']
            return jsonify({"type":"single","status":"success","response":text})
        else:
            x = response[0]
            text = x['text']
            y = response[1]
            image = y['image']
            return jsonify({"type":"double","status":"success","response":text,"image":image})
        #return 'OK'
    except Exception as e:
        print(e)
        return jsonify({"status":"success","response":"Sorry I am not trained to do that yet..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(port=8080)