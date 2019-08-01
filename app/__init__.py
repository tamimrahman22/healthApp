from flask import Flask
from flask_googlemaps import GoogleMaps

app = Flask(__name__)

from app import routes