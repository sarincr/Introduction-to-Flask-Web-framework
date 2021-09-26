from flask import Flask


test = Flask(__name__)


@test.route("/")
def start():
    return "Hello New Page"


@test.route("/second")
def second_page():
   return "Hello second Page"



if __name__ == '__main__':
    test.run()
