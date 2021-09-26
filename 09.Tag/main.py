from flask import Flask


test = Flask(__name__)


@test.route("/")
def start():
    return "Hello Start Page"


@test.route("/home")
def home_page():
   return "Welcome Home page"


@test.route("/blog/<X>")
def blog(X):
   return "Welcome Author %s" % X

@test.route('/<name>')
def base():
   if name =='home':
      return redirect(url_for('home_page'))
   else:
      return redirect(url_for('blog',X = name))

if __name__ == '__main__':
    test.run()
