# akad_backend/app.py

# Import Flask and our new Config object
from flask import Flask
from .config import Config

# Create an instance of the Flask class.
app = Flask(__name__)

# Load the application's configuration from the Config object
# This will apply all the settings we defined in config.py
app.config.from_object(Config)

@app.route("/")
def home():
    """This function runs when someone visits the root URL of our app."""
    # For now, we return a simple message.
    return "Welcome to the Akad Backend! (Secure Edition)"

# The 'if' block now checks the configuration to decide whether to run in debug mode.
# We no longer pass `debug=True` directly to `app.run()`.
if __name__ == "__main__":
    # Flask's `app.run()` will automatically use the DEBUG setting from `app.config`.
    # The host='0.0.0.0' makes the server accessible from other devices on the network.
    # The port is explicitly set to 5000.
    app.run(host='0.0.0.0', port=5000)
