from flask import Flask
# from routes import main
from flask_cors import CORS
from routes.salutations_routes import salutations_api

app = Flask(__name__)
CORS(app)

# app.register_blueprint(main)
app.register_blueprint(salutations_api, url_prefix='/salutations')

if __name__ == "__main__":
    app.run(debug=True, port=5001)

