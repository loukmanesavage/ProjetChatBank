#Ici nous creeons les tables au niveau de PostgreSQL
from Backend import app, db

with app.app_context():
    db.create_all()
    print("Les Tables ont créées avec succès")#après l'exécution ce massage va s'affiche pour montrer que tout s'est bien passer