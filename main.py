from flask import Flask, render_template, request
from translate import get

app = Flask(__name__)


@app.route("/", methods=["post", "get"])
def process():
    r = get(request.form.get("textarea", ""), request.form.get("action", ""))
    if "json" in request.form:
        return {"result": r["result"]}
    return render_template("index.html", data=r)


@app.route("/api", methods=["post"])
def api():
    return {"result": get(request.form.get("textarea", ""), request.form.get("action", ""))["result"]}


if __name__ == "__main__":
    app.run(debug=True)
