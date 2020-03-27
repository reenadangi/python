from flask import Flask, render_template,request,redirect,flash
import re
	

from myconnection import connectToMySQL
# import the function that will return an instance of a connection
app = Flask(__name__)
app.secret_key="keep it secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route("/")
def index():
    print("Hello from index!!")
    mysql = connectToMySQL('first_flask')
    # call the function, passing in the name of our db
    friends = mysql.query_db('SELECT * FROM friends;')  
    # call the query_db function, pass in the query as a string
    print(friends)
    return render_template("index.html",all_friends=friends)

@app.route("/Add_newuser.html")
def add_newuser():
    return render_template("add_newuser.html")

def unique_email(email):
    
    # check from db if that email is already excist 
    mysql = connectToMySQL('first_flask')
    # call the function, passing in the name of our db
    # select count(id) from friends where email like 'p@go.com%';
    notUnique= mysql.query_db(f"SELECT count(*) FROM friends where email like '{email}';")  
    # {friend[0]['first_name']
    print(notUnique[0]["count(*)"])
    if notUnique[0]["count(*)"]>0:
        print("your email is not unique" ,"%"*50)
        return False
        
    else:
        print("your email is  unique" ,"%"*50)
        return True

@app.route("/create_user", methods=["POST"])
def create_user():
    is_valid=True
    
    if len(request.form["firstname"])<1:
        is_valid=False
        flash("please enter first name")
    if len(request.form["lastname"])<1:
        is_valid=False
        flash("please enter last name")
    if len(request.form["occupation"])<1:
        is_valid=False
        flash("please enter occupation")
    if len(request.form["email"])<1:
        is_valid=False
        flash("please enter Email")
    if not EMAIL_REGEX.match(request.form['email']):    # test whether a field matches the pattern
        is_valid=False
        flash("Invalid email address!")
    if unique_email(request.form['email']):
        print("your email is unique" ,"%"*50)
    else:
        is_valid=False
        flash("Email already taken!")
        print("your email is not unique" ,"%"*50)

    if is_valid:
        print("*"*50, "creating a new user" ,request.form["firstname"])
        mySql=connectToMySQL("first_flask")
        query="INSERT INTO friends (first_name, last_name, occupation,email) VALUES (%(fn)s, %(ln)s, %(occ)s,%(mail)s);"
        data={
            "fn":request.form["firstname"],
            "ln":request.form["lastname"],
            "occ":request.form["occupation"],
            "mail":request.form["email"]
        }
        mysql = connectToMySQL('first_flask')
        print("Connected to mysql", mysql)
        new_user_id=mysql.query_db(query,data)

        print(f"new_user_id{new_user_id}")
        flash("Sucessfully Added!")
        return redirect("/")
    else:
        return redirect("/Add_newuser.html")

@app.route("/save", methods=["POST"])
def save_user():
    print("In save user")
    print("*"*50, "creating a new user" ,request.form["firstname"],request.form["id"])
    id=request.form["id"]
    mySql=connectToMySQL("first_flask")
    print("its a update")
    query="UPDATE friends SET first_name= %(fn)s, last_name = %(ln)s, occupation = %(occ)s  WHERE id= %(id)s;"
    data={
        "fn":request.form["firstname"],
        "ln":request.form["lastname"],
        "occ":request.form["occupation"],
        "id":request.form["id"]
        }
    mysql = connectToMySQL('first_flask')
    print("Connected to mysql", mysql)
    print(data)
    new_user_id=mysql.query_db(query,data)

    print(f"new_user_id{new_user_id}")
    return redirect("/")





@app.route("/users/<id>/destroy")
def delete_user(id):
    print("delete")
    mySql=connectToMySQL("first_flask")
    query=f"DELETE FROM friends WHERE id={id};"
    mysql = connectToMySQL('first_flask')
    print("Connected to mysql", mysql)
    mysql.query_db(query)
    print("deleted","$"*20)
    return redirect("/")

@app.route("/users/<id>/update")
def user_update(id):
    print("update")
    mysql=connectToMySQL("first_flask")
    query=f"select * from friends where id={id}"
    friend= mysql.query_db(query)
    print(friend,"@"*70)
    return render_template("update_user.html", friend=friend,update=True)
   
    # print("hello from index")
    # mysql = connectToMySQL('first_flask')
    # # call the function, passing in the name of our db
    # friends = mysql.query_db('SELECT * FROM friends;')  
    # # call the query_db function, pass in the query as a string
    # print(friends)
    # return render_template("index.html",all_friends=friends)
   
    # query=f"UPDATE friends WHERE SET first_name = {firstname}, last_name = {lastname}, occupation = {occupation} id={id};"
    # mysql = connectToMySQL('first_flask')
    # print("Connected to mysql", mysql)
    # mysql.query_db(query)
    # print("deleted","$"*20)
    

if __name__ == "__main__":
    app.run(debug=True)
