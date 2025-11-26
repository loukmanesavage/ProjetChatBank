import spacy
import re

class SpacyHelper:
    def __init__(self):
        # Charger le modèle français de SpaCy
        try:
            self.nlp = spacy.load("fr_core_news_sm")
        except OSError:
            # Si le modèle n'est pas installé, donner des instructions
            print("❌ Modèle SpaCy français non trouvé. Installez-le avec:")
            print("python -m spacy download fr_core_news_sm")
            self.nlp = None

    def detect_intent_with_spacy(self, text):
        if not self.nlp:
            return None, {}
        
        doc = self.nlp(text.lower())
        entities = {}
        intent = None

        # Extraction d'entités avec SpaCy
        for ent in doc.ents:
            if ent.label_ in ["MONEY", "CARDINAL"]:
                entities['montant'] = ent.text
            elif ent.label_ == "DATE":
                entities['date'] = ent.text

        # Détection d'intentions avec des motifs linguistiques
        # 1. Intentions liées au solde
        balance_patterns = [
            "solde", "balance", "argent disponible", "combien ai-je", "reste"
        ]
        if any(token.lemma_ in balance_patterns for token in doc):
            intent = "account_info"
            # Extraction du numéro de compte
            account_match = re.search(r'\b\d{8,12}\b', text)
            if account_match:
                entities['account_number'] = account_match.group()

        # 2. Intentions de transactions
        transaction_patterns = [
            "transaction", "transfert", "envoyer", "virement", "paiement"
        ]
        if any(token.lemma_ in transaction_patterns for token in doc):
            intent = "bank_transactions"
            # Extraction des entités transactionnelles
            self._extract_transaction_entities(doc, entities)

        # 3. Intentions de fraude
        fraud_patterns = ["fraude", "arnaque", "suspect", "anormal"]
        if any(token.lemma_ in fraud_patterns for token in doc):
            intent = "fraude_detection"

        # 4. FAQ - avec une logique plus fine
        if self._is_faq_intent(doc):
            intent = "faq"

        return intent, entities

    def _extract_transaction_entities(self, doc, entities):
        """Extrait les entités spécifiques aux transactions"""
        for token in doc:
            # Montants
            if token.like_num and token.text.isdigit():
                next_token = doc[token.i + 1] if token.i + 1 < len(doc) else None
                if next_token and next_token.text in ["euros", "€", "fcfa", "francs"]:
                    entities['montant'] = token.text
            
            # Destinataires (noms propres)
            if token.ent_type_ == "PER":
                entities['destinataire'] = token.text

    def _is_faq_intent(self, doc):
        """Détecte si c'est une intention FAQ avec SpaCy"""
        faq_keywords = {
            "horaire": ["heure", "ouvrir", "fermer", "horaire"],
            "compte": ["ouvrir", "créer", "nouveau", "compte"],
            "frais": ["frais", "tarif", "coût", "prix"],
            "mot_de_passe": ["mot de passe", "mdp", "réinitialiser"],
            "carte": ["carte", "avalée", "perdue", "volée"]
        }
        
        for category, keywords in faq_keywords.items():
            if any(token.lemma_ in keywords for token in doc):
                return True
        return False

# Instance globale
spacy_helper = SpacyHelper()