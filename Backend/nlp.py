import spacy

nlp = spacy.load('fr_core_news_sm')

from .nlp_enhanced import spacy_helper

def analyze_intent(text):
    text = text.lower()
    intent = ""
    entities = {}

    # Ici nous analisons l'intention avec Spacy
    spacy_intent, spacy_entities = spacy_helper.detect_intent_with_spacy(text)
    
    if spacy_intent:
        return spacy_intent, spacy_entities
    
    intent = ""


     # Ici Spacy nous aides a retrouver le numero de compte qui a été entrée par l'utilisateur
    account_number = spacy_helper.extract_account_number(text)
    if account_number:
        entities['account_number'] = account_number
        intent = "bank_transactions"
        return intent, entities




    # Info solde(Nous l'avons dirriger vers transactions)
    if any(word in text for word in ["solde", "balance", "argent disponible"]):
        intent = "bank_transactions"

    # Transactions
    elif any(word in text for word in ["transaction", "transfert", "envoyer de l'argent"]):
        intent = "bank_transactions"

    # Fraude
    elif "fraude" in text or "scam" in text or "arnaque" in text:
        intent = "fraude_detection"

    # FAQ / Ouvrir un compte
    elif any(word in text for word in ["ouvrir un compte", "ouvrir compte", "comment ouvrir", "créer un compte"]):
        intent = "faq"
        ##Ici nous avons definit tout les mots clé qui peuvent avoir pour intention Faq et autres
    elif any(word in text for word in [
        "heure d'ouverture",
        "horaires",
        "heures",
        "ouverture",
        "fermeture",
        "ouvrir un compte",
        "comment ouvrir",
        "information",
        "renseignement",
        "frais",
        "tarif",
        "coût",
        "combien coûte",
        "prix du compte",
        "mot de passe"
        "mdp",
        "oublié",
        "réinitialiser",
        "password",
        "Code oublié",
        "oublier",
        "carte avalée",
        "avalée",
        "distributeur a avalé",
        "perdu ma carte",
        "carte perdue",
        "avaler",
        "horaire"
        "service"
        "services",
        "Bonjour",
        "Hello",
        "hello",
        "Salut",
        "salut",
        "Morming",
        "infos",
        "bonjour",
        "Solde",
        "reste",
        "Reste",
        "Argent disponible",
        "argent disponible",
        " Merci pour l'assitance",
        "Merci",
        "a plus",
        "merci",
        "Parler a un conseiller",
        "Assistance",
        "Assistant",
        "parler a un conseiller",
        "assistance",
        "assistant",
        "conseiller",
        "Conseiller",
        "Bonsoir",
        "bonsoir",
    ]):
        intent = "faq"
   
#Ici s'il n'arrive pas l'intention parmis ceux qui sont en haut il va dire que l'intention est inconnue.
#Ce qui va le poussé a demander a l'utilisateur de reformuler sa question ou il le dit de joindre un conseiller directement.
#Puis il va joindre le Numéro
    else:
        intent = "unknown" 

    return intent, entities

