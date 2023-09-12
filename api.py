from flask import Flask
from routes import salutations_api, main
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(main)
app.register_blueprint(salutations_api)

if __name__ == "__main__":
    app.run(debug=True, port=5001)

