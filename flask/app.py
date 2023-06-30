from flask import Flask, request


app = Flask(__name__)


@app.route("/f")
def home():
    return f"<h1>Running on {request.environ.get('SERVER_PORT')}</h1>"

if __name__ == '__main__':
    from waitress import serve
    # app.run(host="0.0.0.0", port=5000)
    serve(app, host="0.0.0.0", port=5000)


# def create_app():
#    return app

# waitress-serve --port=5000 --call app:create_app
