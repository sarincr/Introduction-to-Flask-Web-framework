from flask import Flask


test = Flask(__name__)


@test.route("/")
def start():
    return "Hello New Page"



@test.route("/<x>")
def first_page(x):
   return f"You have entered {x}"


@test.route("/second")
def second_page():
   return "Hello second Page"



if __name__ == '__main__':
    test.run()
