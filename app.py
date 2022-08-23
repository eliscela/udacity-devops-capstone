from flask import Flask
from flask import request
from requests import get

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
        client_ip = request.environ['REMOTE_ADDR']
    else:
        client_ip = request.environ['HTTP_X_FORWARDED_FOR']
    return "Hello IP: " + client_ip + "<br> My IP is: " + server_ip


if __name__ == "__main__":
    from waitress import serve
    server_ip = get('https://api.ipify.org').text
    print(f'My public IP address is: {server_ip}')
    serve(app, host="0.0.0.0", port=80)
