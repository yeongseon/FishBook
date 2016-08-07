from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

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
  return render_template('navigation.html')

if __name__ == '__main__':
  app.run(debug=True)
