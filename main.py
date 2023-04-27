import requests

url = 'http://127.0.0.1:8000/posts/8/like'
headers = {'Authorization': 'Token d4a8e2f5b02e512f4b554edca8235920a2d90f74'}
r = requests.post(url, headers=headers)

print(r.text)

