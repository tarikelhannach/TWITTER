
from flask import Flask, render_template
import pandas as pd
from os import environ
import pickle
from flask import request
import os




MODEL='model/sentiment_model'

os.chdir(os.path.dirname(__file__))


app = Flask(__name__)


@app.route("/", methods=['GET'])
def hello():
    return render_template('index 2.html')


@app.route('/predict', methods=['GET'])
def predict():
    model = pickle.load(open(MODEL,'rb'))
    texto = request.args.get('Texto')
    tweets = pd.DataFrame()
    tweets['Texto'] = [texto]
    prediction = model.predict(tweets['Texto'])
    prediction = prediction[0]
    return render_template('predict.html', predict=prediction)