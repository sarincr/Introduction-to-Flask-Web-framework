from flask import *  
app = Flask(__name__)
@app.route('/login',methods = ['POST'])
def login():
    X=request.form['X']
    passwrd=request.form['pass']
    if X=="User" and passwrd=="google":
        return "Welcome %s" %X  
       
if __name__ == '__main__':
    app.run(debug = True)  
