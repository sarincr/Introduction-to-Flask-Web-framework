from flask import Flask


test = Flask(__name__)


@test.route("/")
def start():
    return "Hello New Page"


if __name__ == '__main__':
    test.run()