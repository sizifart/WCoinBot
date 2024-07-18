import hashlib
import random
import string
import base64
import urllib.parse
import jwt
from jwt import InvalidTokenError
from time import time


def escape_html(text: str) -> str:
    return text.replace('<', '\\<').replace('>', '\\>')


def decode_cipher(cipher: str) -> str:
    encoded = cipher[:3] + cipher[4:]
    return base64.b64decode(encoded).decode('utf-8')

def encode_url(url: str) -> str:
    start_index = url.find('&user=') + len('&user=')
    end_index = url.find('&auth_date=')
    part_to_encode = url[start_index:end_index]
    encoded_part = urllib.parse.quote(part_to_encode, safe='')
    encoded_url = url[:start_index] + encoded_part + url[end_index:]

    return encoded_url

def is_jwt_valid(token: str) -> bool:
    try:
        decode = jwt.decode(token, options={"verify_signature": False})
        if int(decode['exp']) < (int(time()) - 60):
            return False
        else:
            return True
    except InvalidTokenError:
        return False