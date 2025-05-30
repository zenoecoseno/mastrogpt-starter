def reverse(args):
  inp = args.get("input","")
  out = "Please provide an input, i will revert it !"
  if inp != "":
    out = inp[::-1]
  return { "output": out }
