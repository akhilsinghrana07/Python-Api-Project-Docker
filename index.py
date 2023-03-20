from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def check_health():
    return 'healthy'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port =int("3000"), debug=True)
