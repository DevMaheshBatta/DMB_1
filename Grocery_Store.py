from flask import *
import datetime
import hashlib
from Grocery_Mongodb import MongoDBHelper
from bson.objectid import ObjectId
web_app = Flask("Grocery App")
db_helper = MongoDBHelper()

@web_app.route("/") # Decorator
def index():

    # either you can return plain text
    # message = "Welcome to Patient Management System. Its {}".format(datetime.datetime.now())

    # OR you can return HTML
    message = """
    <html>
    <head>
        <title>Doctors App</title>
    </head>
    <body>
        <center>
            <h3>Welcome to Doctors Appm</h3>
        </center>
    </body>
    </html>
    """

    # return message

    # render_template is used to return web pages (html pages)
    return render_template("Grocery_index.html")

@web_app.route("/register")
def register():
    return render_template("Grocery_register.html")

@web_app.route("/home")
def home():
    if len(session["email"]) != 0:
        return render_template("Grocery_home.html", name=session["name"], email=session["email"])
    else:
        return redirect("/")

@web_app.route("/success")
def success():
    return render_template("success.html", name=session["name"], email=session["email"])

@web_app.route("/error")
def error():
    return render_template("error.html", name=session["name"], email=session["email"])

@web_app.route("/logout")
def logout():
    # Reset the Data in Session Object
    session["email"] = ""
    session["name"] = ""
    return redirect("/")
  
@web_app.route("/add-user", methods=["POST"])
def add_user_in_db():
    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
        "created_on": datetime.datetime.now()
    }
    db_helper.collection = db_helper.db["Grocery_users"]
    # Save user in DataBase i.e. MongoDB
    result = db_helper.insert(user_data)
    # message = "Welcome to Home Page. User ID is: {}".format(result.inserted_id)
    # return message
    # Write the data in the Session Object
    # This data can now be used anywhere in the project
    session['name'] = user_data["name"]
    session['email'] = user_data["email"]
    # return render_template("home.html", name=session['name'], email=session['email'])
    return render_template("Grocery_home.html", name=session['name'], email=session['email'])
@web_app.route("/fetch-user", methods=["POST"])
def feth_user_from_db():
    # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "email": request.form["email"],
        "password": hashlib.sha256(request.form["password"].encode('utf-8')).hexdigest(),
    }
    db_helper.collection = db_helper.db["Grocery_users"]
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=user_data)
    print("result:", result)
    
    if len(result)>0:
        user_data = result[0] # Get the dictionary from List 
        session['email'] = user_data["email"]
        session['name'] = user_data["name"]
        return render_template("Grocery_home.html", name=session['name'], email=session['email'])
    else:
         return render_template("error.html", message="User Not Found. Please Try Again",
                               name=session["name"], email=session["email"])

@web_app.route("/add-coustomers", methods=["POST"])
def add_coustomers_in_db():

    # Create a Dictionary with Data from HTML Register Form
    coustomers_data = {
        "name": request.form["name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "gender": request.form["gender"],
        "address": request.form["address"],
        "doctor_email": session['email'],
        "doctor_name": session['name'],
        "created_on": datetime.datetime.now()
    }

    db_helper.collection = db_helper.db["coustomers"]
    # Save Patient in DataBase i.e. MongoDB
    result = db_helper.insert(coustomers_data)
    return render_template("success.html", message = "Coustomers Added Successfully",
                           name=session["name"], email=session["email"])

@web_app.route("/fetch-coustomers")
def fetch_coustomers_from_db():
    if len(session["email"])==0:
        return redirect("/")

     # Create a Dictionary with Data from HTML Register Form
    user_data = {
        "doctor_email": session["email"]
    }
    db_helper.collection = db_helper.db["coustomers"]
    
    # Fetch user in DataBase i.e. MongoDB
    result = db_helper.fetch(query=user_data)
    # result here, is a list of documents(dictionaries) from MongoDB
    
    if len(result)>0:
        print(result)
        return render_template("Grocery_coustomer.html",Grocery_coustomer=result, 
                               name=session["name"], email=session["email"])
    else:
        return render_template("error.html", message="Coustomers Not Found. Please Try Again",
                               name=session["name"], email=session["email"])

@web_app.route("/product")
def product():
    return render_template("Grocery_product.html")

@web_app.route("/vegetables")
def vegetables():
    return render_template("Grocery_vegetables.html")
@web_app.route("/fruits")
def fruits():
    return render_template("Grocery_fruits.html")

def main():

    # In order to use Session Tracking, create a Secret Key
    web_app.secret_key = "Grocery_App-key-v1"

    # Run the App infinitely, till user wont quite
    web_app.run(port=5001)
    # web_app.run(port=5001) # optionally you can give the port number

if __name__ == "__main__":
    main()