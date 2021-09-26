from flask import Flask, render_template, request
from translate import get

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", name="World")


def magic(s):
    return ''.join([c.upper() if i & 1 == 1 else c.lower() for i, c in enumerate(s)])


@app.route("/dict", methods=["post"])
def process():
    print(request.form.get('action'))
    return render_template('index.html', source=request.form.get('textarea'),
                           result=get(request.form.get('textarea'), request.form.get('action')))


if __name__ == "__main__":
    app.run(debug=True)
