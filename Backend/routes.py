from flask import request, jsonify, render_template
from Backend import app
from Backend.database_manager import DatabaseManager
import uuid #Identifiants unique


#ici Nous importons les fonctions spécifiques depuis les fichiers present dans mon package Backend
from Backend.nlp import analyze_intent
from Backend.faq import get_faq_answer
from Backend.bank_transactions import get_transaction_info
from Backend.fraude_detection import check_fraud
from Backend.bank_transactions import get_transaction_info, get_account_balance


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

    # FAQ — Ici nous avons mis les Faq en premier position
    if intent == 'faq':
        response = get_faq_answer(user_input)
    
    # Transactions bancaires
   # elif intent == 'bank_transactions':
     #   response = get_transaction_info(entities)


        # Pour les transactions Bancaires
    elif intent == 'bank_transactions':
        # ici Nous demandons a l'utilisateur d'entrée un compte bancaire avec au minimun 16 chiffres
        if not entities.get('account_number') and user_input.strip().isdigit() and len(user_input.strip()) == 16:
            entities['account_number'] = user_input.strip()
        
        #response = get_transaction_info(entities)
        # Utilisons cette fonction pour les soldes
        response = get_account_balance(entities, user_input)

    elif intent == 'account_info':
        # Rediriger vers la gestion des transactions/soldes
        response = get_account_balance(entities, user_input)
    # Détection de fraude
    elif intent == 'fraude_detection':   
        response = check_fraud(entities)

    # Intention inconnue

    else:
        # Vérifier si le message contient un numéro de compte
        from Backend.nlp_enhanced import spacy_helper
        account_number = spacy_helper.extract_account_number(user_input)
        if account_number:
            entities['account_number'] = account_number
            response = get_transaction_info(entities)
        else:
            response = "Désolé, je n'ai pas compris votre demande. Veuillez reformuler ou contacter un conseiller clientèle au +226 XX XX XX XX."
            

     # Sauvegarde de la passe de donnée
    DatabaseManager.save_conversation(user_id, user_input, response, intent)


    return jsonify({"response": response})
