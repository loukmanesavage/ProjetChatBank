
import spacy
import re

class SpacyHelper:
    def __init__(self):
        # Charger le modèle français de SpaCy 
        
        try:
            self.nlp = spacy.load("fr_core_news_sm")
        except OSError:
            # ici il verifie si le modèle est installer ou non puis il donne des instructions
            print("Pour verifié si Spacy est installer, Si non. Installez-le avec:")
            print("python -m spacy download fr_core_news_sm")
            self.nlp = None

    def detect_intent_with_spacy(self, text):
        if not self.nlp:
            return None, {}
        
        doc = self.nlp(text.lower())
        entities = {}
        intent = None

        # Extraction des entités avec SpaCy
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

        # 2. les Intentions au niveau de transactions 
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

        # 4. FAQ - avec une logique très simple
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
    ##Nouveau
    
    def extract_account_number(self, text):
        """Extrait et valide les numéros de compte"""
        # Patterns pour numéros de compte (16 chiffres)
        patterns = [
            r'\b\d{16}\b',  # 16 chiffres consécutifs
            r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'  # Format avec séparateurs
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            if matches:
                # Nettoyer le numéro (enlever espaces et tirets)
                clean_number = re.sub(r'[\s-]', '', matches[0])
                return clean_number
             
            return None
    
   
spacy_helper = SpacyHelper()
