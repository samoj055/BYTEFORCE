from datetime import datetime

def create_user_document(username, password_hash):
    return {
        "username": username,
        "password": password_hash,
        "created_at": datetime.utcnow()
    }
