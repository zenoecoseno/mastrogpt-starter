import os, requests as req
def test_reverse():
    url = os.environ.get("OPSDEV_HOST") + "/api/my/rikyzany/reverse"
    res = req.get(url).json()
    assert res.get("output") == "reverse"
