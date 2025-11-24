
def get_transaction_info(entities):
    account_number = entities.get('account_number')
    # Logique pour récupérer les détails des transactions
    # Exemple de réponse
    return f"Détails des transactions pour le compte {account_number}."

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