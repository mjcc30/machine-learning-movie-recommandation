from flask import Flask,request
from routes.api import create_routes

# Initialize flask
app = Flask(__name__)

# root for vercel healthcheck
@app.route("/")
def home():
    return "HELLO from vercel use flask"

# Set headers json for all requests
@app.after_request
def apply_caching(response):
    response.headers["Content-Type"] = "application/json"
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Upgrade-Insecure-Requests'] = 1
    return response

# Import routes
create_routes(app)