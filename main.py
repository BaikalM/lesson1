from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html", name="World")


def magic(s):
    return ''.join([c.upper() if i & 1 == 1 else c.lower() for i, c in enumerate(s)])


@app.route("/dict", methods=["post"])
def process():
    user = None
    if request.method == 'POST':
        print("1111111111111111111")
        user = {'fname': magic(request.form.get('userfname')),
                'lname': magic(request.form.get('userlname'))}
    return render_template('index.html', user=user)


if __name__ == "__main__":
    app.run(debug=True)
