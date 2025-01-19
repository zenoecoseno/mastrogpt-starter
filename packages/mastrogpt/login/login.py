import os, json
from pathlib import Path
import bcrypt

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify if hashed password matches password.

    Args:
        password (str): The plain password to verify
        hashed_password (str): The saved hashed password

    Returns:
        bool: True if hashed password matches password. False otherwise
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

def login(args):
    """
    >>> import login
    >>> args = {}
    >>> login.login(args)
    {'authenticated': False}
    >>> args= {"username":"boh"}
    >>> login.login(args)
    {'authenticated': False}
    >>> args= {"username":"pinocchio", "password": "bad"}
    >>> login.login(args)
    {'authenticated': False}
    >>> args= {"username":"pinocchio", "password": "geppetto", "S3_SECRET_KEY": "123"}
    >>> login.login(args)
    {'authenticated': True, 's3_key': '123'}
    """
        
    res = { "authenticated": False}
    try:
        username = args.get("username")
        password = args.get("password")

        users = json.loads(Path("users.json").read_text())
        if username != "" and password != "":
            if username in users:
                if verify_password(password, users[username]):                                
                    res = {
                        "authenticated": True,
                        "s3_key": args.get("S3_SECRET_KEY", ""),
                        "api_key": os.getenv("__OW_API_KEY")
                    }
                    
    except Exception as e:
        print(str(e))
    
    return res
  