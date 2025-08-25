from flask import Flask,render_template ### render_template it is used to add html in owr fask app 
### WSGI Application 
app=Flask(__name__)
@app.route("/")    
def welcome():
    return "Welcome to flask hellp app"
@app.route("/index") 
def index():
    return render_template('index.html') ## The html file we want to onset in this special page only 
if __name__=="__main__":
    app.run(debug=True) 

 

