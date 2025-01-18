#--web true
#--docker docker.io/apache/openserverless-runtime-python:v3.12-2501172243
# --kind python:default
import display
def main(args):
    return display.display(args)
