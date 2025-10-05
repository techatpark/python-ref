# test_main.py
from src.main import greet


def test_greet_world():
    assert greet("World") == "Hello, World!"
