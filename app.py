from flask import Flask
### WSGI Application 
app=Flask(__name__)
@app.route("/")    ### / is home page rule here in string formate
def welcome():
    return "Welcome to flask hellp app"
@app.route("/index") ### This line(/index)will be add to the home address present in the url and our index page will be genrated
def index():
    return "Kaise hai sir index page aa gaya oyee"
if __name__=="__main__":
    app.run(debug=True)  ## debug=True is used to show owr changes directly without restart

 

