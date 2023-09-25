from flask import Flask
# from routes import main
from flask_cors import CORS
from routes.salutations_routes import salutations_api
from routes.restaurants_routes import restaurants_api
from routes.reponses_possibles_routes import reponses_possibles_api
from routes.notes_structures_routes import notes_structures_api
from routes.legendes_routes import legendes_api
from routes.gestionnaires_routes import gestionnaires_api
from routes.elements_routes import elements_bp
from routes.elements_audites_details_prestations_routes import details_prestations_bp
from routes.clients_routes import clients_bp
from routes.client_contacts_routes import client_contacts_bp
from routes.auditeurs_routes import auditeurs_bp
from routes.audits_routes import audits_api
from routes.constats_routes import constats_api
from routes.create_audit_routes import create_audit_bp



app = Flask(__name__)
CORS(app)

# app.register_blueprint(main)
app.register_blueprint(salutations_api, url_prefix='/salutations')
app.register_blueprint(restaurants_api, url_prefix='/restaurants')
app.register_blueprint(reponses_possibles_api, url_prefix='/reponses_possibles')
app.register_blueprint(notes_structures_api, url_prefix='/notes_structures')
app.register_blueprint(legendes_api, url_prefix='/legendes')
app.register_blueprint(gestionnaires_api, url_prefix='/gestionnaires')
app.register_blueprint(elements_bp, url_prefix='/elements')
app.register_blueprint(details_prestations_bp, url_prefix='/elements_audites_prestations_details')
app.register_blueprint(clients_bp, url_prefix='/clients')
app.register_blueprint(client_contacts_bp, url_prefix='/client_contacts')
app.register_blueprint(auditeurs_bp, url_prefix='/auditeurs')
app.register_blueprint(audits_api, url_prefix='/audits')
app.register_blueprint(constats_api, url_prefix='/constats')
app.register_blueprint(create_audit_bp, url_prefix='/create-audit')


if __name__ == "__main__":
    app.run(debug=True, port=5001)

