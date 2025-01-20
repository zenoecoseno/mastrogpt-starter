#--kind python:default
#--web true
#--param REDIS_URL $REDIS_URL
#--param REDIS_PREFIX $REDIS_PREFIX
#--param S3_SECRET_KEY $S3_SECRET_KEY
#--annotation provide-api-key true
import login
def main(args):
    return {"body": login.login(args)}
