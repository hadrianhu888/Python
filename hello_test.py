import pytest
import hello 
from hello import hello, hello1  # Assuming hello.py is in the same directory

# Test for hello function
def test_hello(capsys):
    hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"

# Test for hello1 function
def test_hello1():
    assert hello1("Alice") == "Hello, Alice!"
    assert hello1("Bob") == "Hello, Bob!"

