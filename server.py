from flask import Flask, request, url_for, abort

app = Flask(__name__)

import url


if __name__ == '__main__':
    app.run()