from flask import Flask, render_template
app= Flask(__name__)
@app.route("/")
def EightByEight():
    print("in hello")

    return render_template("index.htm",row=int(8),col=int(8))
@app.route("/<x>/<y>")
def xByY(x,y):
    print("in hello")
   
    return render_template("index.htm",row=int(x),col=int(y))

# @app.route("/<name>")
# def hello_person(name):
#     return f"Hello {name} welcome to Flask!!!"

# @app.route("/dojo")
# def dojo():
#     return "dojo"
# @app.route("/say/<name>")
# def say(name):
#     return f"Hello {name}"

# @app.route("/repete/<no>/<word>")
# def repete(no,word):
#        i=int(no)
#        st=''
#        for i in range(int(no)):
#            st+=f"{word}\n"
#        return st


# Playground
@app.route("/play")
def play():
    print("in play")
    return render_template("index.htm",no_box=3)

@app.route("/play/<x>")
def play_box(x=3):
    print("in play")
    return render_template("index.htm",no_box=int(x))
@app.route("/play/<x>/<color>")
def play_box_color(x,color):
    print("in play")
    return render_template("index.htm",no_box=int(x),color=color)

# End playground
if __name__=="__main__":
    app.run(debug=True)
