import datetime, time
import bcrypt
import jwt
import app_configs

def get_auth_token(fullname, _days, _seconds = 0):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = getPayLoad(fullname, _days, _seconds)
        return True, encode_auth_token_HS256(payload)
    except Exception as e:
        return False, e

def getPayLoad(fullname, _days, _seconds = 0):
    #issuers
    issuer = app_configs.ISSUER
    # the time at which the JWT was issued
    issued_at = datetime.datetime.utcnow()
    # expiration time after nr days/seconds
    exp = issued_at + datetime.timedelta(days=_days, seconds=_seconds)
    payload = {
            "iss": issuer,
            "exp": exp,
            "iat": issued_at,
            "aud": fullname
        }
    return payload
    
def get_secret():
    return app_configs.SECRET_KEY.encode(encoding='UTF-8', errors='strict')


def encode_auth_token_HS256(payload):
    try:
        secret = get_secret()
        encoded =  jwt.encode(payload, secret, 'HS256')
        return encoded.decode('utf-8')
    except Exception as e:
        return e


def decode_auth_token_HS256(encoded, _audience):
    try:
        secret = get_secret()# .decode('utf-8')
        decoded = jwt.decode(encoded, secret, algorithms='HS256', audience= _audience)
        return True,  decoded
    except Exception as e:
        return False, e
