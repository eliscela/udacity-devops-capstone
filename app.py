from flask import Flask
from flask import request
from requests import get

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_ip():
    return "Hello Udacity!<br>App Update 2.0"


if __name__ == "__main__":
    from waitress import serve
    server_ip = get('https://api.ipify.org').text
    print(f'My public IP address is: {server_ip}')
    serve(app, host="0.0.0.0", port=80)
