import requests

resp = requests.post("https://pytorch-flask-deploy.onrender.com/predict", files={'file': open('seven.png', 'rb')})

print(resp.text)