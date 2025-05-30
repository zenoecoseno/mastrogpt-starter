import chat

def stateful(args):
  
  inp = args.get("input", "")
  out = f"Hello from {chat.MODEL}"
  res = {}
  

  if inp != "":
    ch = chat.Chat(args)
    #load
    import history
    hi = history.History(args)
    hi.load(ch)
    #add msg
    msg = f"user:{inp}"
    ch.add(msg)
    print(ch.messages)
    out=ch.complete()
    hi.save(msg)
    #complete
    hi.save(f"assistant:{out}")
    res['state']=hi.id()
    
    

  res['output'] = out
  return res
