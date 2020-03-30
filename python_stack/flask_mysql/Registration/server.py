from flask import Flask, render_template,request,redirect,flash,session
import re
from myconnection import connectToMySQL # import the function that will return an instance of a connection
from flask_bcrypt import Bcrypt



app = Flask(__name__)
app.secret_key="keep it secret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument

@app.route("/")
def index():
    print("hello from users")
    mysql = connectToMySQL('first_flask')
    # call the function, passing in the name of our db
    users = mysql.query_db('SELECT * FROM users;')  
    # call the query_db function, pass in the query as a string
    print(users)
    return render_template("index.html",all_users=users)


@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/home")
def home():
    print(f"session['userid']: {session['userid']}")
    # get all the cities from cities table - select * from co
    # select * from cities c , countries co where c.countries_country_id=co.country_id  
   
    
    mysql = connectToMySQL('first_flask')
    # call the function, passing in the name of our db
    cities = mysql.query_db('select * from cities c , countries co where c.countries_country_id=co.country_id ;')  
    # call the query_db function, pass in the query as a string
    print(cities)
    # get user's Travel details 
    mysql = connectToMySQL('first_flask')
    travel=mysql.query_db(f"select ut.id, u.first_name, c.city_name,ut.comments from user_travel ut, cities c,users u where u.id=ut.users_id and ut.cities_city_id=c.city_id and ut.users_id={session['userid']};")
    print(travel)


    return render_template("home.html",user=session['userid'],cities=cities,travel=travel)

@app.route("/login")
def login():
   
    return render_template("login.html")
@app.route("/logout")
def logout():
    destroy_session()
    return render_template("login.html")

def set_session(id,name):
    session['userid']=id
    session['username']=name

def destroy_session():
    session['userid']=""
    session['username']=""
    

@app.route("/validuser", methods=["POST"])
def validuser():
    # check if this user does exist in db
    mysql = connectToMySQL('first_flask')
    # call the function, passing in the name of our db
    # select count(id) from friends where email like 'p@go.com%';
    query="SELECT * FROM users where email = %(email)s;" 
    data = { "email" : request.form["email"] }
    result = mysql.query_db(query, data)    
    print(result,"-"*80) 

    if len(result) > 0:
        if bcrypt.check_password_hash(result[0]['pass'], request.form['password']):
            # if we get True after checking the password, we may put the user id in session
            # its a valid user 
            # setsession
            set_session(result[0]['id'],result[0]['first_name'])
             

            return redirect('/home')
        else:
            flash("You could not be logged in")
   
    return redirect("/login")


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
    # Genrating a Hash in bcrypt
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(f"This is {pw_hash}","!"*80)
    
    if len(request.form["firstname"])<1:
        is_valid=False
        flash("please enter first name")
    if len(request.form["lastname"])<1:
        is_valid=False
        flash("please enter last name")
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
    if is_valid:
        print("*"*50, "Register new user" ,request.form["firstname"])
        mySql=connectToMySQL("first_flask")
        query="INSERT INTO users (first_name, last_name,email,pass) VALUES (%(fn)s, %(ln)s,%(mail)s,%(pass)s)"
        data={
            "fn":request.form["firstname"],
            "ln":request.form["lastname"],
            "mail":request.form["email"],
            "pass":pw_hash
        }
        mysql = connectToMySQL('first_flask')
        print("Connected to mysql", mysql)
        new_user_id=mysql.query_db(query,data)

        print(f"new_user_id{new_user_id}")
        flash("Sucessfully Added!")
        set_session(new_user_id,request.form["firstname"])
        return redirect("/home")
    else: 
        return redirect("/register.html")

@app.route("/addcitytomymap", methods=["POST"])
def addcitytomymap():
    mySql=connectToMySQL("first_flask")
    print(request.form.get('places'), "9"*60)
    query="INSERT INTO user_travel (users_id, cities_city_id,comments) VALUES (%(uid)s,%(cid)s,%(comm)s)"
    data={
        "uid":session["userid"],
        "cid":request.form.get('places'),
        "comm":request.form["comments"],
           
    }
    mysql = connectToMySQL('first_flask')
    print("Connected to mysql", mysql)
    new_travel_id=mysql.query_db(query,data)

    print(f"new_travel_id{new_travel_id}")
    flash("Sucessfully Added!")
    return redirect("/home")

@app.route("/checkemail", methods=['POST'])
def checkemail():
    found = False
    print(request.form['email'],"*"*80)
    mysql = connectToMySQL('first_flask')        # connect to the database
    query = "SELECT * from users WHERE users.email = %(mail)s;"
    data = { 'mail': request.form['email'] }
    
    result = mysql.query_db(query, data)
    print("***"*60)
    if result:
        found = True
    return render_template('partials/emailMsg.html', found=found)  # render a partial and return it
    # Notice that we are rendering on a post! Why is it okay to render on a post in this scenario?
    # Consider what would happen if the user clicks refresh. Would the form be resubmitted?


#     @app.route("/update_user", methods=["POST"])
#     def update_user():
#         print("*"*50, "creating a new user" ,request.form["firstname"],request.form["id"])
#         id=request.form["id"]
#         mySql=connectToMySQL("first_flask")
#         print("its a update")
#         query="UPDATE friends SET first_name= %(fn)s, last_name = %(ln)s, occupation = %(occ)s  WHERE id= %(id)s;"
#         data={
#             "fn":request.form["firstname"],
#             "ln":request.form["lastname"],
#             "occ":request.form["occupation"],
#             "id":request.form["id"]
#         }
#         mysql = connectToMySQL('first_flask')
#         print("Connected to mysql", mysql)
#         print(data)
#         new_user_id=mysql.query_db(query,data)

#         print(f"new_user_id{new_user_id}")
#         return redirect("/")




@app.route("/<id>/destroy")
def delete_user(id):
    print("delete")
    mySql=connectToMySQL("first_flask")
    query=f"DELETE FROM user_travel WHERE id={id};"
    mysql = connectToMySQL('first_flask')
    print("Connected to mysql", mysql)
    mysql.query_db(query)
    print("deleted","$"*20)
    return redirect("/home")

# @app.route("/users/<id>/update")
# def user_update(id):
#     print("update")
#     mysql=connectToMySQL("first_flask")
#     query=f"select * from friends where id={id}"
#     friend= mysql.query_db(query)
#     print(friend,"@"*70)
#     return render_template("update_user.html", friend=friend,update=True)
   
#     # print("hello from index")
#     # mysql = connectToMySQL('first_flask')
#     # # call the function, passing in the name of our db
#     # friends = mysql.query_db('SELECT * FROM friends;')  
#     # # call the query_db function, pass in the query as a string
#     # print(friends)
#     # return render_template("index.html",all_friends=friends)
   
#     # query=f"UPDATE friends WHERE SET first_name = {firstname}, last_name = {lastname}, occupation = {occupation} id={id};"
#     # mysql = connectToMySQL('first_flask')
#     # print("Connected to mysql", mysql)
#     # mysql.query_db(query)
#     # print("deleted","$"*20)
    

if __name__ == "__main__":
    app.run(debug=True)
