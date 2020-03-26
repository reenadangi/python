from flask import Flask, render_template,request,redirect
app= Flask(__name__)
@app.route("/")
def main():
    return render_template("index.htm")


@app.route("/process", methods=["post"])
def register_user():
    print(request.form["name"],"*"*60)
    return render_template("user.htm",username=request.form['name'],email=request.form['email'])

if __name__=="__main__":
    app.run(debug=True)
