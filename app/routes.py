from app import app
from flask import render_template, request
from app.models import model, formopener
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

# you can set key as config
app.config['GOOGLEMAPS_KEY'] = "AIzaSyAKP1rCVhlUayr84Mw2TvWl4NadSrz2wM4"

# Initialize the extension
GoogleMaps(app)

bmiNum = 0
weight_range = 'normal weight'
print(bmiNum)

@app.route('/')
@app.route('/index')
def index():
    global bmiNum
    return render_template('index.html', bmiNum = bmiNum)

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
    
@app.route('/consistency', methods = ['GET','POST'])
def consistency():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=40.7552,
        lng=-73.9741,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat':40.7552,
             'lng':-73.9741,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat':40.7552,
             'lng':-73.9741,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    return render_template('consist.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
    
    