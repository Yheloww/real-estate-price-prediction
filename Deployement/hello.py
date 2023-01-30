from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("login.html")

@app.route("/greet")
def greet():
    return render_template("greet.html", name=request.args.get("name","world"))

if __name__ == '__main__':
    app.run(port=5000, debug=True)