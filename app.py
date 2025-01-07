import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model
model = pickle.load(open('linear_model.pkl', 'rb'))

@app.route('/') #Go to homepage
def home():
    return render_template('home.html') #home.html yet to be created

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    # data is a dictionary. We want its values as a list -> converted to numpy array -> reshaped
    print(np.array(list(data.values())).reshape(1,-1))