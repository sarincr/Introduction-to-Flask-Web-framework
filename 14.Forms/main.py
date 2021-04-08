from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def student():
   return render_template('home.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      X = request.form
      return render_template("result.html",pass_data = X)

if __name__ == '__main__':
   app.run(debug = True)
