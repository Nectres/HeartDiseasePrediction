from flask import Flask, render_template, request, make_response
import joblib

rfc = joblib.load("rfc.joblib")


def predict_heart_disease(params):
    return rfc.predict([params])[0] == 1


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/")
def index():
    try:
        params = request.args
        p1 = params.get('p1', type=float)
        p2 = params.get('p2', type=float)
        p3 = params.get('p3', type=float)
        p4 = params.get('p4', type=float)
        print(p1, p2, p3, p4)
        return str(predict_heart_disease([p1, p2, p3, p4]))
    except:
        resp = make_response()
        resp.status_code = 401
        return resp


app.run(port=4050)
