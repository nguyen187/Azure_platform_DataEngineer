import pandas as pd
from azureml.core.model import Model
from azureml.core import Workspace
from azureml.core import Run
import json
import os
import numpy as np
import joblib
from keras.models import load_model
from pathlib import Path
from inference_schema.schema_decorators import input_schema, output_schema
from inference_schema.parameter_types.numpy_parameter_type import NumpyParameterType
import joblib

model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'operation_model_nb','9','network.h5')
scale_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'),'scale','9','scale.pkl')

input_sample = np.array([[80,	253.0,53,296.0,13.87591373591667, 73408.0,5.142756158733616	],
                         [80,	253.0,53,296.0,13.87591373591667, 73408.0,5.142756158733616	]])

output_sample = np.array([
    {
        "Sugar feed rate(Fs:L/h)": 0,
        "Water for injection/dilution(Fw:L/h)": 0,
        "Substrate concentration(S:g/L)": 0,
        "Temperature(T:K)": 0,
        "Dissolved oxygen concentration(DO2:mg/L)": 0,
        "Vessel Volume(V:L)": 0,
        "pH(pH:pH)": 0,
        "Predict": 0
    }
])

def init():
    global model
    global scale
    model = load_model(model_path)
    scale = joblib.load(scale_path)
    
@input_schema('Inputs', NumpyParameterType(input_sample))
@output_schema(NumpyParameterType(output_sample))
def run(Inputs):
    data = np.array(Inputs)
    data.T[0] = data.T[0]*data.T[2]
    data = np.delete(data,2,axis=1)
    data = np.insert(data, 6, data.T[2], axis=1)
    print('data:',data)
    data_trans = scale.transform(data)
    y_hat = model.predict(data_trans)
    print('y_pred',y_hat)
    result = []
    for i in range(len(y_hat)):
        row = {
            "Sugar feed rate(Fs:L/h)": float(Inputs[i][0]),
            "Water for injection/dilution(Fw:L/h)": float(Inputs[i][1]),
            "Substrate concentration(S:g/L)": float(Inputs[i][2]),
            "Temperature(T:K)": float(Inputs[i][3]),
            "Dissolved oxygen concentration(DO2:mg/L)": float(Inputs[i][4]),
            "Vessel Volume(V:L)": float(Inputs[i][5]),
            "pH(pH:pH)": float(Inputs[i][6]),
            "Predict": float(y_hat[i][0])
        }
        result.append(row)

    return result