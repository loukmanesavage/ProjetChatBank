from Backend import app, db

with app.app_context():
    db.create_all()
    print("✅ Tables créées avec succès dans PostgreSQL!")