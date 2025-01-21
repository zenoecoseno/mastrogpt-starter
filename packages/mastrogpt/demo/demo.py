USAGE = "Please type one of 'code', 'chess', 'html', 'form', 'message'"

FORM = [
  {
      "name": "why",
      "label": "Why do you recommend Apache OpenServerless?",
      "type": "textarea",
      "required": "true"
  },
  {
    "name": "job",
    "label": "What is your job role?",
    "type": "text",
    "required": "true"
  },
  {
      "name": "tone",
      "label": "What tone should the post have?",
      "type": "text",
      "required": "true"
  }
]

HTML = """<h1>Sample Form</h1>
<form action="/submit-your-form-endpoint" method="post">
  <div>
    <label for="username">Username:</label>
    <input type="text" id="username" name="username" required>
  </div>
  <div>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password" required>
  </div>
  <div>
    <button type="submit">Login</button>
  </div>
</form>
"""

CODE = """
def sum_to(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
"""

CHESS = "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2"

def demo(args):

    print(args)
        
    language = None
    code = None
    chess = None
    message = None
    html = None
    form = None

    # initialize state
    title =  "MastroGPT Display Demo"
    try:
        # get the state if available
        counter = int(args.get("state")) +1
    except:
        # initialize the state
        counter = 1
        
    message =  f"You made {counter} requests"
    state = str(counter)
    
    input = args.get("input", "")

    output = USAGE
    if "why" in args:
        output = "Thanks for submitting a form!"
    elif input == "":
        output = f"Welcome to the Demo chat. {USAGE}"
        message = "Watch here for rich output." 
    elif input == "code":
        code = CODE 
        language = "python"
        output = f"Here is some python code.\n```python\n{code}\n```"
    elif input == "chess":
        chess = CHESS
        output = f"Check this chess position.\n\n{chess}"    
    elif input ==  "html":
        html = HTML
        output = f"Here is some HTML.\n```html\n{html}\n```"
    elif input == "message":
        message = "This is the message."
        title = "This is the title"
        output = "Here is a sample message."
    elif input == "form":
        form = FORM
        output = "please fill the form"
    else:
        output = f"You made {counter} requests. {USAGE}"

    
    # state is a counter incremented at any invocation
    res = {
        "output": output,
    }

    if state: res['state'] =  state
    if language: res['language'] = language
    if message: res['message'] =  message     
    if title: res['title'] = title
    if chess: res['chess'] = chess
    if code: res['code'] = code
    if html: res['html'] = html
    if form: res['form'] = form

    return res