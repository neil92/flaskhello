import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from flaskr import create_app

def test_config():
  assert not create_app().testing
  assert create_app({"TESTING" : True}).testing


def test_hello(client):
  response = client.get("/hello")
  assert response.data == b"Hello, World!"
