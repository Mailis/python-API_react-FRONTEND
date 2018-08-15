from werkzeug.security import check_password_hash, generate_password_hash

def generate_safe_username(username):
    pw_hash = generate_password_hash(username)
    return pw_hash


def check_if_username_is_safe(plain_username : str, hashed_username):
    return check_password_hash(plain_username, hashed_username)