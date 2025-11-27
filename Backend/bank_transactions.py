"""
def get_transaction_info(entities):
    account_number = entities.get('account_number')
    # Logique pour récupérer les détails des transactions
    # Exemple de réponse
    return f"Détails des transactions pour le compte {account_number}."

"""
"""
def get_transaction_info(entities):
    account_number = entities.get('account_number')

    if not account_number:
        return "Veuillez fournir un numéro de compte pour voir les transactions."

    # Exemple de transactions fictives
    fake_transactions = [
        {"date": "2025-11-20", "type": "Retrait", "montant": "-10 000 FCFA"},
        {"date": "2025-11-18", "type": "Dépôt", "montant": "+50 000 FCFA"},
        {"date": "2025-11-16", "type": "Paiement Orange Money", "montant": "-5 000 FCFA"},
    ]

    # Construction de la réponse
    response = f"📄 Transactions récentes pour le compte **{account_number}** :\n"
    for t in fake_transactions:
        response += f"- {t['date']} | {t['type']} | {t['montant']}\n"

    return response
"""
import re

def validate_account_number(account_number):
    """Valide le format du numéro de compte"""
    if not account_number:
        return False, "Aucun numéro de compte fourni."
    
    # Nettoyer le numéro
    clean_account = re.sub(r'[\s-]', '', account_number)
    
    # Vérifier la longueur
    if len(clean_account) != 16:
        return False, f"Le numéro de compte doit contenir 16 chiffres. Vous en avez saisi {len(clean_account)}."
    
    # Vérifier que ce ne sont que des chiffres
    if not clean_account.isdigit():
        return False, "Le numéro de compte ne doit contenir que des chiffres."
    
    return True, clean_account

def get_account_balance(entities, user_input=""):
    """
    Gère spécifiquement les demandes de solde
    entities: les entités extraites par NLP (contient le numéro de compte si détecté)
    user_input: le message original de l'utilisateur (pour détecter les mots-clés de solde)
    """
    
    # nous recherchons le numero de comptes
    account_number = entities.get('account_number')
    
    #Ici nous avons une liste qui peuvent renvoyer au faite que l'utilisateur veus faire reference a son solde
    balance_keywords = ["solde", "balance", "argent disponible", "combien ai-je", "reste", "montant"]
    
    #Ici nous verifions s'il demande un solde spécifique
    is_balance_request = any(word in user_input.lower() for word in balance_keywords)
    
    # En premier s'il fait la requete sans mentionner son numéro de compte nous affichons ce message en lui donner un exemple de numéros de compte
    if is_balance_request and not account_number:
        return "Veuillez fournir votre numéro de compte pour consulter votre solde. Exemple : 5565562322122222"
    
    # En 2eme Lieu s'il donne son numéro de compte
    if is_balance_request and account_number:
        # Nous vérifions s'il est valide
        is_valid, validation_result = validate_account_number(account_number)
        if not is_valid:
            return f"❌ {validation_result}"
        
        # Afficher le solde(Ici nous avons mis quelques chose de simple afin de voir le fonctionnement)
        return f"""
✅ **Solde du compte :** {account_number}

💳 **Solde actuel :** 1,567.89 €

📊 **Dernière transaction :**
• 2025-11-27 | Amazon Market | -45,99 €

_Que souhaitez-vous faire ?_
"""
    
    # Ici s'il fini pour le cas de demande de solde il passe dirrectement au deuxieme parametre pour les transactions
    return get_transaction_info(entities)

def get_transaction_info(entities):
    #Récupère les informations de transaction avec validation
    account_number = entities.get('account_number')
    
    # Si en entrée le numéro de compte n'est pas mentionner, Nous le donnons un exemple de compte valide
    if not account_number:
        return "Veuillez fournir un numéro de compte pour voir les transactions. Exemple : 5565562322122222"

    # Valider le numéro de compte
    is_valid, validation_result = validate_account_number(account_number)
    
    if not is_valid:
        return f"❌ {validation_result}"
    
    # Numéro valide - afficher les transactions
    valid_account = validation_result
    
    # Exemple de transactions fictives(Nous avons ajouter des transaction fictif dans le bus de voir le fonctionnement)
    fake_transactions = [
        {"date": "2025-11-27", "description": "Amazon Market", "montant": "-45,99 €"},
        {"date": "2025-11-26", "description": "Salaire", "montant": "+2,450.00 €"},
        {"date": "2025-11-25", "description": "Supermarché", "montant": "-87,34 €"},
        {"date": "2025-11-24", "description": "Virement émis", "montant": "-200,00 €"},
        {"date": "2025-11-23", "description": "Remise de chèque", "montant": "+150.00 €"},
    ]

    # Mise en place d'une réponse formatée
    response = f"""
<br>✅ Numéro de compte validé :{valid_account}

<br>📊Dernières transactions :

"""
    
    for t in fake_transactions:
        response += f"Date->>{t['date']} | {t['description']} | {t['montant']}<br>"

    response += f"""
<br>💳 Solde actuel : 1,567.89 €

<br>🔍 Options disponibles :
<br>1<-- Faire un virement
<br>2<-- Consulter plus d'historique  
<br>3<-- Voir mes relevés
<br>4<-- Contacter un conseiller

<br>Tapez votre choix ou une nouvelle demande...
"""
    
    return response