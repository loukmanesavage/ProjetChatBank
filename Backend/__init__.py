from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os



# Définir les chemins vers Frontend
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Frontend', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Frontend', 'static'))




# Initialiser l'application Flask
app = Flask(__name__,
           template_folder=template_dir,
           static_folder=static_dir)


#Creation d'une clé secrète pour la secuté de mon Chat Bot
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Configurer Ma base de données PostgreSQL avec mes identifiants
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Loukmane_db:Savage@localhost/ma_banque'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



# Importer les routes après l'initialisation de l'app
from . import routes





