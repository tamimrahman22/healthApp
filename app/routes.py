from app import app
from flask import render_template, request
from app.models import model, formopener

bmiNum = 0
weight_range = 'normal weight'

@app.route('/')
@app.route('/index')
def index():
    bmiNum = 0
    return render_template('index.html')

@app.route('/bmi_calc', methods = ["GET", "POST"])
def bmi_calc():
    global bmiNum
    global weight_range
    userData = dict(request.form)
    weight = float(userData["weight"])
    height = float(userData["height"])
    bmiNum = model.bmi(weight, height)
    print(bmiNum)
    if bmiNum < 18.5:
        weight_range = 'underweight'
    elif (bmiNum >= 18.5) and (bmiNum < 24.9):
        weight_range = 'normal weight'
    elif (bmiNum >=25) and (bmiNum < 29.9):
        weight_range = 'overweight'
    elif bmiNum >= 30:
        weight_range = 'obese'
    return render_template("index.html", bmiNum = bmiNum, weight_range = weight_range)

@app.route('/diet', methods = ['GET', 'POST'])
def diet():
    global bmiNum
    global weight_range
    return render_template('diet.html', bmiNum = bmiNum, weight_range = weight_range)
@app.route('/exercise', methods = ['GET','POST'])
def exercise():
    global bmiNum
    global weight_range
    return render_template('exercise.html', bmiNum = bmiNum, weight_range = weight_range)
    
    