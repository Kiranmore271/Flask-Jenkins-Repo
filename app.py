from flask import Flask

#create the application Object
app = Flask("myFlaskApp")

#Define the route
@app.route("/sayHello")
def greet():
    return "<h3> Hello from Flask APP - Jenkins </h3> <hr>"


#run the application

app.run('192.168.162.188', 5000, debug=True, use_reloader=True)
