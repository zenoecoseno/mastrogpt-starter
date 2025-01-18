#--kind python:default
#--web true
#--param USERNAME $OPSDEV_USERNAME
#--param HOST $OPSDEV_HOST
#--param S3_SECRET_KEY $S3_SECRET_KEY
#--param MASTROGPT_USERNAME $MASTROGPT_USERNAME
#--param MASTROGPT_PASSWORD $MASTROGPT_PASSWORD
import os, json
from pathlib import Path

def main(args):
    
    username = args.get("user")
    password = args.get("password")
    username_check = args.get("MASTROGPT_USERNAME")
    password_check= args.get("MASTROGPT_PASSWORD")
    print("check", username_check, password_check)
    res = { "authenticated": False}
    if username_check != "" and password_check != "":
        if username == username_check and password ==  password_check:
            res = {
                "authenticated": True,
                "s3_key": args.get("S3_SECRET_KEY", "")
            }
    return { "body": res }
  