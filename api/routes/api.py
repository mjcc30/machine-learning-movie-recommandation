from flask import request
import pandas as pd
import pickle

data = pd.read_csv('../data/data.csv')

"""
Create routes
"""

def create_routes(app):
    """
    Predict movie params
    """@app.route("/")
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

    @app.route('/api/movie/predict', methods=['POST'])
    def predict():
        loaded_model = pickle.load(open('../notebooks/model', 'rb'))

        body = request.get_json()
        print(body)

        new_data = {
            'index': [body['index']],
            'budget': [body['budget']],
            'genres': [body['genres']],
            'homepage': [body['homepage']],
            'id': [body['id']],
            'keywords': [body['keywords']],
            'original_language': [body['original_language']],
            'original_title': [body['original_title']],
            'overview': [body['overview']],
            'popularity': [body['popularity']],
            'production_companies': [body['production_companies']],
            'production_countries': [body['production_countries']],
            'release_date': [body['release_date']],
            'revenue': [body['revenue']],
            'runtime': [body['runtime']],
            'spoken_languages': [body['spoken_languages']],
            'status': [body['status']],
            'tagline': [body['tagline']],
            'title': [body['title']],
            'vote_average': [body['vote_average']],
            'vote_count': [body['vote_count']],
            'tittle': [body['tittle']],
            'cast': [body['cast']],
            'crew': [body['crew']],
            'director': [body['director']],
            'soup': [body['soup']],
        }

        X_predict = pd.DataFrame(new_data,
                                 columns=[
                                     'index',
                                     'budget',
                                     'genres',
                                     'homepage',
                                     'id',
                                     'keywords',
                                     'original_language',
                                     'original_title',
                                     'overview',
                                     'popularity',
                                     'production_companies',
                                     'production_countries',
                                     'release_date',
                                     'revenue',
                                     'spoken_languages',
                                     'status',
                                     'tagline',
                                     'title',
                                     'vote_average',
                                     'vote_count',
                                     'tittle',
                                     'cast',
                                     'crew',
                                     'director',
                                     'soup',
                                 ])
        result = loaded_model.predict(X_predict)
        return str(result[0])
