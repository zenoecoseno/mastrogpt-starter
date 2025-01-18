# --kind python:default
#--docker docker.io/apache/openserverless-runtime-python:v3.12-2501172243
#--web true
#--param S3_SECRET_KEY $S3_SECRET_KEY
#--annotation provide-api-key true
import login
def main(args):
    return {"body": login.login(args)}