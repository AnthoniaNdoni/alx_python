"""
Write a script that starts a Flask web application:

Your web application must be listening on 0.0.0.0, port 5000
Routes:
/: display “Hello HBNB!”
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask

# define a flask instance
app = Flask(__name__)
# set strict_s;ashes flag to false

# create route for index
@app.route('/')
# a function for 
def hello():
    """
    a function definition that return
    a strin hello... on a get request 
    to a router page
    param: 
        type: NONE
    Return:
        type: String
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """
    a function definition that return
    a strin hello... on a get request 
    to a router page
    param: 
        type: NONE
    Return:
        type: String
    """
    return "HBNB"

if __name__=='__main__':
    # for every route
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0')