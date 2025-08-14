from datetime import datetime

def create_transaction_document(user_id, amount, type):
    return {
        "user_id": user_id,
        "amount": amount,
        "type": type,  # 'deposit', 'withdrawal', 'contribution'
        "timestamp": datetime.utcnow()
    }
