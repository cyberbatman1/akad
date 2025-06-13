# main_app.py

# Import the Flask class from the flask package.
# Flask is the micro-framework we'll use to build our web application.
from flask import Flask

# Create an instance of the Flask class. 
# __name__ is a special Python variable that gets the name of the current module.
# Flask uses this to know where to look for resources like templates and static files.
app = Flask(__name__)

# This is a route decorator. It tells Flask what URL should trigger our function.
# In this case, the root URL ('/') will trigger the home() function.
@app.route("/")
def home():
    """This function runs when someone visits the root URL of our app."""
    # The function returns a simple string that will be displayed in the browser.
    return "Welcome to the Akad Backend!"

# This is a standard Python construct.
# The code inside this 'if' block will only run when the script is executed directly
# (e.g., by running 'python app.py'), not when it's imported by another script.
if __name__ == "__main__":
    # This starts the Flask development server.
    # debug=True enables the debugger, which provides helpful error messages
    # and automatically reloads the server when you make code changes.
    app.run(debug=True)
