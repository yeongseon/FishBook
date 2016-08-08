# FishBook


1.pip install requirements.txt

2.execute
python route.py
gunicorn -b 0.0.0.0:5000 routes:app
(https://community.nitrous.io/tutorials/deploying-a-flask-application-to-heroku)

3.connect 127.0.0.1:5000
