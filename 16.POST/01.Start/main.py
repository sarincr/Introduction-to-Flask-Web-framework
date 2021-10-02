from flask import *

app = Flask(__name__)

X = ['Hello', 1, 4.63, True, "World", 2.0, "False"]


@app.route('/')
def message():
    return render_template('index.html',len = len(X), X=X)

if __name__ == '__main__':
    app.run()
