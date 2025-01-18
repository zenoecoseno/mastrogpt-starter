import sys
sys.path.append("packages/mastrogpt/hello")
import hello

def test_hello():
    res = hello.hello({})
    assert res["output"] == "Hello, world"
    args = { "input": "Test"}
    res = hello.hello(args)
    assert res["output"] == "Hello, Test"
    
