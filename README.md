# akad
islamic finance compliance checker powered by gemini api


# Akad - Islamic Finance Compliance Checker Backend

Akad is a web service designed to help users determine if their financial documents (contracts, agreements, etc.) are Sharia-compliant. The application leverages the power of Google's Gemini API for intelligent document analysis. This repository contains the backend server for the Akad application, built with Flask and SQLite.

**Project Status:** In Development

---

## Features

*   **Secure Configuration:** Manages secrets and configuration via environment variables.
*   **Flask Backend:** A robust server built with the Flask micro-framework.
*   **(Upcoming)** Document Upload API endpoint.
*   **(Upcoming)** Text extraction from PDF and DOCX files.
*   **(Upcoming)** Integration with Gemini API for compliance analysis.
*   **(Upcoming)** SQLite database for storing user and document information.

---

## Tech Stack

*   **Framework:** Flask
*   **Database:** SQLite (initially)
*   **Language:** Python 3
*   **AI Integration:** Google Gemini API
*   **Dependency Management:** Pip & Virtual Environment

---

## Getting Started

Follow these instructions to set up and run the development server on your local machine.

### Prerequisites

*   Python 3.8+
*   Git
*   A GitHub account and a [Personal Access Token (PAT)](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) for command-line authentication.

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/akad.git
    cd akad
    ```

2.  **Create and activate a Python virtual environment:**
    ```bash
    # Create the environment
    python3 -m venv venv

    # Activate it (on Linux/macOS)
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create and configure your environment file:**
    *   Copy the example file to a new `.env` file.
        ```bash
        cp .env.example .env
        ```
    *   Generate a secret key by running the following command and pasting the output into the `SECRET_KEY` field in your new `.env` file.
        ```bash
        python -c 'import secrets; print(secrets.token_hex(24))'
        ```
    *   Your `.env` file should now look something like this:
        ```
        SECRET_KEY='a_very_long_random_string_that_you_pasted_here'
        FLASK_DEBUG=True
        ```

### Running the Application

1.  **Set the `FLASK_APP` environment variable:**
    *This command tells Flask where to find the application instance. You need to run this once per terminal session.*
    ```bash
    export FLASK_APP=akad_backend.app
    ```

2.  **Run the Flask development server:**
    ```bash
    flask run
    ```

3.  The server will now be running at `http://127.0.0.1:5000`. Open this URL in your browser, and you should see the message: `Welcome to the Akad Backend! (Secure Edition)`.

---

## Version Control

We use a conventional commit message format to keep the project history clean and understandable. Examples:
*   `feat(auth): Add user login endpoint`
*   `fix(db): Correct query parameter order`
*   `docs(readme): Update setup instructions`
