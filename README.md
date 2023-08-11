# pytorch-flask-deploy

**Test:**
```
pip install requests

import requests
resp = requests.post("https://pytorch-flask-deploy.onrender.com/predict", files={'file': open('seven.png', 'rb')})
print(resp.text)
```
The commands I need to use:

```
mkdir pytorch-flask-deploy
cd pytorch-flask-deploy
py -3 -m venv venv
venv\Scripts\activate
pip install Flask
pip install torch torchvision
mkdir app
code .

cd app
set FLASK_APP=main.py
set FLASK_ENV=development
flask run

pip install requests

mkdir test
cd test
python test.py

pip freeze > requirements.txt
```
