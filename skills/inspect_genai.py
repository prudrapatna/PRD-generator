from google import genai
from google.genai import types

try:
    client = genai.Client()
    print("Available models:")
    for m in client.models.list():
        print(m.name)
except Exception as e:
    print(e)
