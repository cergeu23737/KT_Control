import secrets


def generate_kt_id():
    return "KT-" + secrets.token_hex(4).upper()


def generate_security_id():
    return "KTS-" + secrets.token_hex(16).upper()
