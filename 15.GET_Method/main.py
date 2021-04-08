from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route('/login',methods = ['GET'])  
def login():  
      uname=request.args.get('uname')  
      passwrd=request.args.get('pass')  
      if uname=="admin" and passwrd=="password1":  
          return "Welcome %s" %uname  
   
if __name__ == '__main__':  
   app.run(debug = True)  