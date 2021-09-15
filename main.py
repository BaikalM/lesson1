from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"
    #return render_template("index.html",name="World")

#@app.route("/<name>")
#def greeting(name):
#    return render_template("index.html",name=name)



if __name__=="__main__":
    app.run()