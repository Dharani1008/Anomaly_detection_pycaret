from pycaret.anomaly import *
from flask import Flask,request, url_for, redirect, render_template, jsonify
import pandas as pd
import pickle
import numpy as np
import random
import uuid
import json
app = Flask(__name__)

model = load_model('Final IForest Model 8feb2021')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = {"success": False}
    task_id = str(uuid.uuid4())
    data ["id"] = task_id
    try:
        content = request.get_json()
        data_unseen = pd.DataFrame(content)
        prediction = predict_model(model, data=data_unseen)
        output_json =prediction.to_json(orient='records')
        data["success"] = True
    except ValueError as e:
        print('ValueError')
        data['Error'] = str(e)
    except Exception as e:
        print('Exception')
        print(e)
        data['Error'] = str(e) 
        
    if "Error" in data.keys():
        print("{} {}".format(task_id, data['Error']))
    return output_json

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5010)
