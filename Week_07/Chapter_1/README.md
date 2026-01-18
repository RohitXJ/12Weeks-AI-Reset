# Week 07: Chapter 1 - Introduction to Flask

This chapter introduces the fundamentals of building web applications with Flask, a lightweight Python web framework.

## What's Happening?

We are setting up a very basic web server using Flask. This involves creating the essential files to get a minimal Flask application running and defining a simple "Hello, World!" response for web requests.

## What We Learned

*   **Flask Basics**: How to initialize a Flask application instance.
*   **Routing**: How to define URL routes (e.g., `/` or `/index`) and associate them with Python functions that handle requests.
*   **Project Structure**: The standard way to organize Flask project files, including `server.py` for running the app and an `app` directory for core components like `__init__.py` and `routes.py`.
*   **Environment Configuration**: Using a `.flaskenv` file to set environment variables, such as telling Flask which file contains the application instance.

## How to Do It

1.  **Create Project Files**:
    *   Create a project directory named `Week_07/Chapter_1`.
    *   Inside this directory, create an `app` sub-directory.
    *   In the `app` directory, create two files: `__init__.py` and `routes.py`.
    *   In the main project directory (`Week_07/Chapter_1`), create `server.py`.
    *   Also in the main project directory, create a `.flaskenv` file.

2.  **Add Content to Files**:
    *   **`.flaskenv`**:
        ```
        FLASK_APP=server.py
        ```
    *   **`app/__init__.py`**:
        ```python
        from flask import Flask

        app = Flask(__name__)

        from app import routes
        ```
    *   **`app/routes.py`**:
        ```python
        from app import app

        @app.route('/')
        @app.route('/index')
        def index():
            return "Hello, World!"
        ```
    *   **`server.py`**:
        ```python
        from app import app
        ```

3.  **Run the Application**:
    *   Open your terminal or command prompt.
    *   Navigate to the `Week_07/Chapter_1` directory.
    *   Ensure you have Flask installed (`pip install Flask`).
    *   Run the command: `flask run`
    *   Open your web browser and go to `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/index`. You should see "Hello, World!".

## How It Works

*   **`server.py`**: This file is the entry point that Flask's command-line tools look for. It imports the Flask application instance (`app`) from the `app` package.
*   **`app/__init__.py`**: This file initializes the Flask application. `app = Flask(__name__)` creates an instance of the Flask class. `from app import routes` ensures that the route definitions are registered with the app.
*   **`app/routes.py`**: This file defines the URL endpoints. The `@app.route('/')` decorator tells Flask that the `index()` function should be executed when a user visits the root URL (`/`). The function returns the string "Hello, World!", which Flask sends back to the browser.
*   **`.flaskenv`**: This file is read by tools like `flask run` to set up the environment. `FLASK_APP=server.py` tells Flask where to find your application.

---

**Special Thanks** to Miguel Grinberg for the excellent Flask Mega-Tutorial! His clear and easy-to-follow guide has been invaluable in learning Flask.

Check out his project repository: [https://github.com/miguelgrinberg/microblog](https://github.com/miguelgrinberg/microblog)

---