from flask import Flask,request
from routes.api import create_routes

# Dev = True

# Initialize flask
app = Flask(__name__)
# app.config["DEBUG"] = Dev

@app.route("/")
def home():
    return "HELLO from vercel use flask"

@app.route('/example', methods=['POST'])
def example():
    if request.method == 'POST':
        data = request.form['data']
        print(data)
        return f"The data you sent is: {data}"

@app.route("/about")
def about():
    return "HELLO about"

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

# Run app
# if (Dev):
#     app.run(debug=True, port=5050)