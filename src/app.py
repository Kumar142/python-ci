from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, world! This is kumar Gaurav"


if __name__ == "__main__":
    app.run()
