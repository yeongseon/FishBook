from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

app = Flask(__name__)
Bootstrap(app)
GoogleMaps(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/menu1')
def menu1():
  return render_template('menu1.html')

@app.route('/menu2')
def menu2():
  return render_template('menu2.html')

@app.route('/menu3')
def menu3():
  return render_template('menu3.html')

@app.route('/navigation')
def navigation():
  mymap = Map(
          identifier="view_side",
          lat=34.749064,
          lng=127.655273,
          zoom=15,
          style="height:300px;width:device-width;margin:0;",
          markers=[(34.749063, 127.655273)]
          )
  return render_template('navigation.html', mymap=mymap)

if __name__ == '__main__':
  app.run(debug=True)
