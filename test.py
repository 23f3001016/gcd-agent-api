import requests

BASE_URL = "http://127.0.0.1:8000/task"
task = "Write and run a program that prints the greatest common divisor of 204 and 562."
resp = requests.get(BASE_URL, params={"q": task})

try:
    print("Status:", resp.status_code)
    print("Response JSON:")
    print(resp.json())
except requests.exceptions.RequestException as e:
    print("Error:", e)
