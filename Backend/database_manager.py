
from . import db  # ici on importe bd depuis le package
from .models import Conversation #iCi nous allons importe la classe conversation au niveau de Models
from datetime import datetime  #Ici pour l'heure et la date exact
import uuid #Ici nous souhaitons des identifiants uniques en fonction de chaque instrucions

class DatabaseManager:
    
    @staticmethod
    def save_conversation(user_id, user_message, bot_response, intent=None):
        try:
            conversation = Conversation(
                user_id=user_id,
                user_message=user_message,
                bot_response=bot_response,
                intent=intent,
                timestamp=datetime.utcnow()
            )
            
            db.session.add(conversation)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erreur sauvegarde: {e}")
            return False
        

