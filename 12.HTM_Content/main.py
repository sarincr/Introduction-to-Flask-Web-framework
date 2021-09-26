from flask import *

app = Flask(__name__)

@app.route('/<X>')
def message(X):
    return render_template('index.html', Y = X)

if __name__ == '__main__':
    app.run()  
