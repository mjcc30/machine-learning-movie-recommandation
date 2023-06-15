from flask import Flask,request, jsonify
# import pandas as pd
import pickle5 as pickle
import os

# data = pd.read_csv('../data/data.csv')

# Initialize flask
app = Flask(__name__)

# Set headers json for all requests
# @app.after_request
# def apply_caching(response):
#     response.headers["Content-Type"] = "application/json"
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     response.headers['Access-Control-Allow-Headers'] = '*'
#     response.headers['Upgrade-Insecure-Requests'] = 1
#     return response

@app.route("/")
def home():
	return "HELLO from vercel use flask"

@app.route("/about")
def about():
	return "HELLO about"

@app.route("/example", methods=["POST"])
def example():
    if request.method == "POST":
        data = request.get_json()  # Parse JSON data from request
        if data and "key" in data:
            return jsonify({"message": f"Received data: {data['key']}"})
        return jsonify({"error": "Invalid JSON data or missing 'key' field."}), 400
    return jsonify({"error": "Invalid request method."}), 405

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        body = request.get_json()  # Parse JSON data from request
        if body and "id" in body:
            current_directory = os.getcwd()
            api_directory = os.path.join(current_directory, 'api')

            items = os.listdir(api_directory)

            for item in items:
                print(item)
            model_path = os.path.join(api_directory, 'model')
            with open(model_path, 'rb') as file:
                loaded_model = pickle.load(file)
            return jsonify(body)
        return jsonify({"error": "Invalid JSON data."}), 400
    return jsonify({"error": "Invalid request method."}), 405

#     data = {
#         'index': [body['index']],
#         'budget': [body['budget']],
#         'genres': [body['genres']],
#         'homepage': [body['homepage']],
#         'id': [body['id']],
#         'keywords': [body['keywords']],
#         'original_language': [body['original_language']],
#         'original_title': [body['original_title']],
#         'overview': [body['overview']],
#         'popularity': [body['popularity']],
#         'production_companies': [body['production_companies']],
#         'production_countries': [body['production_countries']],
#         'release_date': [body['release_date']],
#         'revenue': [body['revenue']],
#         'runtime': [body['runtime']],
#         'spoken_languages': [body['spoken_languages']],
#         'status': [body['status']],
#         'tagline': [body['tagline']],
#         'title': [body['title']],
#         'vote_average': [body['vote_average']],
#         'vote_count': [body['vote_count']],
#         'tittle': [body['tittle']],
#         'cast': [body['cast']],
#         'crew': [body['crew']],
#         'director': [body['director']],
#         'soup': [body['soup']],
#     }

#     X_predict = pd.DataFrame(data,
#                             columns=[
#                                 'index',
#                                 'budget',
#                                 'genres',
#                                 'homepage',
#                                 'id',
#                                 'keywords',
#                                 'original_language',
#                                 'original_title',
#                                 'overview',
#                                 'popularity',
#                                 'production_companies',
#                                 'production_countries',
#                                 'release_date',
#                                 'revenue',
#                                 'spoken_languages',
#                                 'status',
#                                 'tagline',
#                                 'title',
#                                 'vote_average',
#                                 'vote_count',
#                                 'tittle',
#                                 'cast',
#                                 'crew',
#                                 'director',
#                                 'soup',
#                             ])
#     result = loaded_model.predict(X_predict)
#     return str(result[0])


# flask
# gunicorn
# pandas
# numpy
# requests
# pickle-mixin
# joblib
# keras
# scipy
# scikit-learn
# seaborn
# xgboost