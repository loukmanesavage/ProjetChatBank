"""from flask import request, jsonify, render_template
from Backend import app

from Backend.nlp import analyze_intent
from Backend.faq import get_faq_answer
from Backend.bank_transactions import get_transaction_info
from Backend.fraude_detection import check_fraud


# Route pour afficher l'interface du chatbot
@app.route("/")
def index():
    return render_template("chat.html")


@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_input = request.json['message']
    intent, entities = analyze_intent(user_input)
    
    # Traitement des intentions
    if intent == 'faq':
        response = get_faq_answer(user_input)
    elif intent == 'transaction_info':
        response = get_transaction_info(entities)
    elif intent == 'fraud_detection':
        response = check_fraud(entities)
    else:
        response = "Désolé, je n'ai pas compris votre demande."

    return jsonify({"response": response})
"""
from flask import request, jsonify, render_template
from Backend import app
from Backend.database_manager import DatabaseManager
import uuid #Identifiants unique



from Backend.nlp import analyze_intent
from Backend.faq import get_faq_answer
from Backend.bank_transactions import get_transaction_info
from Backend.fraude_detection import check_fraud


@app.route("/")
def index():
    return render_template("chat.html")

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    user_input = request.json['message']
    #intent, entities = analyze_intent(user_input.lower())
    intent, entities = analyze_intent(user_input)

    # Générer un ID utilisateur unique chaque fois avec maximum 8 caractères
    user_id = str(uuid.uuid4())[:8]

    # 1️⃣ FAQ — doit être traité EN PREMIER
    if intent == 'faq':
        response = get_faq_answer(user_input)
    
    # 2️⃣ Transactions bancaires
    elif intent == 'bank_transactions':
        response = get_transaction_info(entities)

    # 3️⃣ Détection de fraude (corrigé)
    elif intent == 'fraude_detection':   # ← ICI corrigé
        response = check_fraud(entities)

    # 4️⃣ Intention inconnue

    else:
        response = "Désolé, je n'ai pas compris votre demande. Veuillez reformuler ou contacter un conseiller clientèle au +226 XX XX XX XX."

     # Sauvegarde de la passe de donnée
    DatabaseManager.save_conversation(user_id, user_input, response, intent)


    return jsonify({"response": response})
