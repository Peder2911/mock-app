
import json
import flask

app = flask.Flask(__name__)

@app.route("/",methods = ["GET"])
def home():
    return flask.Response(json.dumps({"message":"Hello world!"}),content_type = "application/json")

if __name__ == "__main__":
    app.run("0.0.0.0",8080)

