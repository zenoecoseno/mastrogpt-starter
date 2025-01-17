#--kind python:default
#--web true
#--param USERNAME $OPSDEV_USERNAME
#--param HOST $OPSDEV_HOST
import os, json
from pathlib import Path
from urllib.parse import urlparse, urlunparse

def main(args):  
  services = {}    
  current_dir = os.path.dirname(os.path.abspath(__file__))
  files = os.listdir(current_dir)
  files.sort()
  for file in files:
    #file = files[1]
    if not file.endswith(".json"):
      continue
    
    entry = file.rsplit(".", maxsplit=1)[0].split("-", maxsplit=1)[-1]
    if not entry in services:
      services[entry] = []
    dict = json.loads(Path(file).read_text())
    for key in dict:
      services[entry].append(key)
    
  username = args.get("USERNAME", "pinocchio")
  res = {
    "username": username,
    "services": services
  }
  return { "body":  res } 
