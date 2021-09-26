from flask import Flask


test = Flask(__name__)


@test.route("/")
def start():
    return "Hello Start Page"


@test.route("/<name>")
def start_page(name):
	return f"Hello {name}!"



@test.route("/admin")
def second_page():
    return redirect(url_for('start_page',name = "New Page"))

if __name__ == '__main__':
    test.run()
