import time
import bcrypt

def get_timestamp() -> int:
    return int(time.time() * 1000)

def hash_password(password: str) -> str:
    hashed = bcrypt.hashpw(
        password.encode("utf-8"), 
        bcrypt.gensalt(),
    ).decode()
    return hashed

def check_password(
    password1: str, 
    password2: str,
) -> bool:
    try:
        hashed = bcrypt.checkpw(
            password1.encode("utf-8"), 
            password2.encode("utf-8")
        )
        return hashed
    except:
        return False

def parse_words(path: str):
    result = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            if " - " not in line:
                continue  # skip malformed lines
            en, ru = line.split(" - ", 1)  # split only on first " - "
            result.append({"en": en.strip(), "ru": ru.strip()})
    return result
