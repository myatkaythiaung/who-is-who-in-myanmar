from flask import Flask , render_template
app = Flask(__name__)
@app.route("/index")
def index():
  return render_template("index.html")

@app.route("/candidates")
def candidates():
  return render_template("candidates.html")

@app.route("/member")
def member():
  return render_template("member.html")

@app.route("/business")
def business():
  return render_template("business.html")

@app.route("/celebrities")
def celebrities():
  return render_template("celebrities.html")

@app.route("/modern")
def modern():
  return render_template("modern.html")

@app.route("/m1")
def m1():
  return render_template("m1.html")

@app.route("/m2")
def m2():
  return render_template("m2.html")

@app.route("/m3")
def m3():
  return render_template("m3.html")

@app.route("/m4")
def m4():
  return render_template("m4.html")

@app.route("/m5")
def m5():
  return render_template("m5.html")

@app.route("/m6")
def m6():
  return render_template("m6.html")

@app.route("/ff")
def ff():
  return render_template("ff.html")

@app.route("/about")
def about():
  return render_template("about.html")

if __name__ == "__main__":
   app.run(debug=True)
