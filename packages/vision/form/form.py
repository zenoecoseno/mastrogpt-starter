import os, requests as req
import vision2 as vision
import bucket
from datetime import datetime
import base64

USAGE = "Please upload a picture and I will tell you what I see"
FORM = [
  {
    "label": "Load Image",
    "name": "pic",
    "required": "true",
    "type": "file"
  },
]

def form(args):
  res = {}
  out = USAGE
  buc= bucket.Bucket(args)
  inp = args.get("input", "")

  if type(inp) is dict and "form" in inp:
    img = inp.get("form", {}).get("pic", "")
    #display image on screen
    #out = vis.decode(img)
    #res['html'] = f'<img src="data:image/png;base64,{img}">'

    img_decoded = base64.b64decode(img.encode('utf-8'))
    #print('img decoded --> '+str(img_decoded))
    #start homework
    key='img-'+str(datetime.now())
    write_ok = buc.write(key, img_decoded)
    assert write_ok=='OK', write_ok
    url = buc.exturl(key, 3600)

    vis = vision.Vision(args)
    out += vis.decode(img)
    res['html'] = f"<img src='{url}'>"
    print(url)

  res['form'] = FORM
  res['output'] = out
  return res
