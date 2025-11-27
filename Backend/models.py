##Ici nous avons crée des classes pour le stockage au niveau de notre Base de données
#Ici nous enregistrons les conversations des utilisateurs sur Postgre
#Nous avons deux classes Conversation et ChatMesssage
from . import db
from datetime import datetime

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), index=True)
    user_message = db.Column(db.Text)
    bot_response = db.Column(db.Text)
    intent = db.Column(db.String(100))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Ici nous avons notre classe ChatMessage
class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_message = db.Column(db.Text)
    bot_response = db.Column(db.Text)