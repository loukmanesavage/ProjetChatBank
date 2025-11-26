from .nlp_enhanced import spacy_helper

def analyze_intent(text):
    text = text.lower()
    intent = ""
    entities = {}

    # ✅ ESSAYER SPACY EN PREMIER
    spacy_intent, spacy_entities = spacy_helper.detect_intent_with_spacy(text)
    
    if spacy_intent:
        return spacy_intent, spacy_entities
    
    intent = ""



    # Info solde
    if any(word in text for word in ["solde", "balance", "argent disponible"]):
        intent = "account_info"

    # Transactions
    elif any(word in text for word in ["transaction", "transfert", "envoyer de l'argent"]):
        intent = "bank_transactions"

    # Fraude
    elif "fraude" in text or "scam" in text or "arnaque" in text:
        intent = "fraude_detection"

    # FAQ / Ouvrir un compte
    elif any(word in text for word in ["ouvrir un compte", "ouvrir compte", "comment ouvrir", "créer un compte"]):
        intent = "faq"
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
    ]):
        intent = "faq"

    else:
        intent = "unknown"

    return intent, entities

