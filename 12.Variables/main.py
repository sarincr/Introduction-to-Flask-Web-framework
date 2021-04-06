from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route("/")
@app.route('/home')
def home():
   dict = {'X':10,'Y':20 }
   return render_template('home.html', total = dict)



if __name__ == '__main__':
    app.run(debug=True)
