 # Exemple de gestion de questions fréquentes

def get_faq_answer(user_input):
    msg = user_input.lower().strip()

    ##L'acceuil
    acceuil = ["Bonjour", "Hello", "Salut", "salut", "Morning", "services" , "infos", "service", "bonjour", "hello"

    ]
    for kw in acceuil :
        if kw in msg :
            return "OUI Bonjour comment allez vous? Merci de nous avoir contacter, Que pouvons nous faire pour vous? ou Comment nous pouvons vous aider?"

    # FAQ :Pour les heures d'ouverture
    horaires_keywords = [
        "heure", "horaires", "ouvre", "ouverture", "fermé", "quand êtes vous ouvert"
    ]
    for kw in horaires_keywords:
        if kw in msg:
            return "Nos heures d'ouverture sont de 9h à 17h, du lundi au vendredi et  Fermé les week-ends"

    # FAQ :Pour l'ouverture de compte
    open_account_keywords = [
        "ouvrir un compte", "nouveau compte", "compte bancaire", "inscription", "créer un compte", "creer un compte"
    ]
    for kw in open_account_keywords:
        if kw in msg:
            return "Vous pouvez ouvrir un compte en ligne ou en vous rendant dans une de nos agences muni d'une pièce d'identité et un justificatif de domicile."
    #Pour demander les frais
    information_bank =[ "frais", "tarif", "coût", "combien coûte", "prix du compte"
    ]
    for kw in information_bank :
        if kw in msg:
            return "Nos principaux frais bancaires sont : Pour une Carte bancaire : 4 000 FCFA / mois ,Banque en ligne : Gratuit, Tenue de compte : 1 500 FCFA / mois.Pour plus de détails, consultez notre grille tarifaire."
    #Pour les mot de passe oublié

    compte_probleme=["mot de passe", "mdp", "oublié", "réinitialiser", "password"

    ]
    for kw in compte_probleme :
        if kw in msg :
            return "Pour réinitialiser votre mot de passe : Accédez à l'application bancaire puis Cliquez sur 'Mot de passe oublié et enfin Suivez les instructions envoyées par SMS"
        
   ##Carte perdu ou volé
    carte_perdu=["carte avalée", "avalée", "distributeur a avalé", "perdu ma carte", "carte perdue"

    ]
    for kw in carte_perdu:
        if kw in msg :
            return "Si votre carte a été avalée ou perdue :1-Contactez immédiatement le service client : +226 XX XX XX XX 2-Bloquez la carte via l'application 3-Une nouvelle carte pourra être émise en agence si vous vous rendez."


    #S'il y'a aucune FAQ reconnue
    return "Je ne suis pas sûr de la réponse à cette question. Pouvez-vous reformuler ?ou contacter un conseiller au +226 XX XX XX XX"

