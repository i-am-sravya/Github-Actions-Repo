# app.py
# This is a test commit
def add(a, b):
    c = a+b
    print("printing a+b = ", c)
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
