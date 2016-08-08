# FishBook

1.pip install requirements.txt

2.execute
python route.py
gunicorn -b 0.0.0.0:5000 routes:app
(https://community.nitrous.io/tutorials/deploying-a-flask-application-to-heroku)

3.connect 127.0.0.1:5000

# Reference
google map :
https://github.com/rochacbruno/Flask-GoogleMaps
https://pypi.python.org/pypi/Flask-GoogleMaps/

google api key 만들기
https://developers.google.com/maps/documentation/javascript/get-api-key

# TODO
config 파일 따로 만들기
