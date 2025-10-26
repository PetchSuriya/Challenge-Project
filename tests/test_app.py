from app import hello

def test_hello_default():
    assert hello() == "Hello, world!"

def test_hello_custom():
    assert hello("MFU") == "Hello, MFU!"
from app import hello

def test_hello_default():
    assert hello() == "Hello, world!"

def test_hello_custom():
    assert hello("MFU") == "Hello, MFU!"
