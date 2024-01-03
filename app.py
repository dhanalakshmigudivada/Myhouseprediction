from flask import Flask,render_template,request
from args import *
import pickle
import numpy as np
with open('Model.pkl','rb') as mod:
    model=pickle.load(mod)
with open('Scaler.pkl','rb') as mod:
    scaler=pickle.load(mod)
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    #print(request.method)
    #print(request.form)
    #return 'I am in first page'
    if request.method=='POST':
        bedrooms=request.form['bedrooms']
        bathrooms=request.form['bathrooms']
        location=request.form['location']
        sft=request.form['sft']
        status=request.form['status']
        direction=request.form['direction']
        propertytype=request.form['propertytype']
        input_array=np.array([[bedrooms,bathrooms,
                               location,sft,status,
                               direction,propertytype
                               ]])
        data=scaler.transform(input_array)
        prediction=model.predict(data)[0]
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               direction_mapping=direction_mapping,
                               property_type_mapping=property_type_mapping,
                               prediction=prediction)

        
    else:
        return render_template('index.html',location_mapping=location_mapping,
                               status_mapping=status_mapping,
                               direction_mapping=direction_mapping,
                               property_type_mapping=property_type_mapping
                               )
@app.route('/second')
def second():
    return 'I am in second page'
@app.route('/thrid')
def thrid():
    return 'I am in thrid page'
@app.route('/four')
def four():
    return 'I am in four page'

#use_reloader=True means automatic updating the server without restarting the app file
app.run(use_reloader=True,debug=True)