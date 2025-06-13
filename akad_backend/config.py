# akad_backend/config.py

import os
from dotenv import load_dotenv

# Find the absolute path of the root directory of the project
# This is necessary to locate the .env file correctly.
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Load environment variables from the .env file located in the project root
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """
    Base configuration class. Contains default configuration settings
    and settings loaded from environment variables.
    """
    
    # --- Critical Application Secrets ---
    
    # SECRET_KEY is crucial for cryptographic signing (e.g., session cookies, CSRF protection).
    # It's loaded from the .env file. If it's not set, the application will not start.
    SECRET_KEY = os.getenv('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you create a .env file?")

    # --- Application Environment ---

    # DEBUG mode enables/disables the interactive debugger and other development features.
    # We fetch 'FLASK_DEBUG' as a string and convert it to a boolean.
    # Default to False (safer) if not set.
    DEBUG = str(os.getenv('FLASK_DEBUG')).lower() == 'true'
