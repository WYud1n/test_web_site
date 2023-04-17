from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Осторожно!</title>
                  </head>
                  <body>
                    <a href="https://youtu.be/dQw4w9WgXcQ">Вот почему CS:GO = GOVNO</a>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
