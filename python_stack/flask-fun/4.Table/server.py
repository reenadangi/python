from flask import Flask, render_template
app= Flask(__name__)
@app.route("/")
def main():
    student_info=[
        {"first_name":"Reena","last_name":"Dangi"},
        {"first_name":"Siya","last_name":"Choudhary"},
        {"first_name":"Pankaj","last_name":"Jain"},
        {"first_name":"Bob","last_name":"Funny"}

    ]
    return render_template("index.htm",students=student_info)

if __name__=="__main__":
    app.run(debug=True)
