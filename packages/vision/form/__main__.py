#--kind python:default
#--web true
#--param OLLAMA_HOST $OLLAMA_HOST
#--param AUTH $AUTH
#--param S3_ACCESS_KEY $S3_ACCESS_KEY
#--param S3_SECRET_KEY $S3_SECRET_KEY
#--param S3_BUCKET_DATA $S3_BUCKET_DATA
#--param S3_API_URL $S3_API_URL
#--param S3_HOST $S3_HOST
#--param S3_PORT $S3_PORT


import form
def main(args):
  return { "body": form.form(args) }
