from flask import Flask

# This is needed so that Flask knows where to look for resources such as templates and static files.
app = Flask(import_name=__name__)


# tell Flask what URL should trigger our function.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
