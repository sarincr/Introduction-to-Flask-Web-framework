from flask import Flask


test = Flask(__name__)


@test.route("/")
def start():
    return "Hello New Page"



@test.route("/home/<X>")
def first_page(X):
   return 'Hello %s!' % X


@test.route("/second")
def second_page():
   return "Hello second Page"



if __name__ == '__main__':
    test.run()
