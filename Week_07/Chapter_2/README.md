# Week 07: Chapter 2 - HTML Templates and Dynamic Content

This chapter builds upon the basic Flask application by introducing HTML templating to create dynamic web pages.

## What's Happening?

We are enhancing our Flask web application to serve dynamic HTML content instead of plain text. This involves creating HTML files (templates) and using Flask to render them, populating them with data.

## What We Learned

*   **HTML Templating**: How to use Jinja2, Flask's default templating engine, to embed Python logic (variables, loops, etc.) within HTML.
*   **`render_template` Function**: How to use Flask's `render_template` function to load and render HTML files from a `templates` directory.
*   **Template Inheritance**: Creating a base layout (`base.html`) that other templates can extend, promoting code reusability and consistency.
*   **Dynamic Data**: Passing Python data (like user information or a list of posts) to HTML templates for dynamic display.

## How to Do It

1.  **Set up Project Structure**:
    *   Follow the steps from Chapter 1 to set up the basic Flask project.
    *   Inside the `app` directory, create a new sub-directory named `templates`.
    *   Inside the `templates` directory, create two files: `base.html` and `index.html`.

2.  **Add Content to Files**:
    *   **`.flaskenv`**: (Same as Chapter 1)
        ```
        FLASK_APP=server.py
        ```
    *   **`app/__init__.py`**: (Same as Chapter 1)
        ```python
        from flask import Flask

        app = Flask(__name__)

        from app import routes
        ```
    *   **`app/routes.py`**:
        ```python
        from flask import render_template
        from app import app

        @app.route('/')
        @app.route('/index')
        def index():
            user = {'username': 'Rohit'}
            posts = [
                {
                    'author': {'username': 'John'},
                    'body': 'Beautiful day in Portland!'
                },
                {
                    'author': {'username': 'Susan'},
                    'body': 'The Avengers movie was so cool!'
                }
            ]
            return render_template('index.html', title = 'Home', user = user, posts = posts)
        ```
    *   **`app/templates/base.html`**:
        ```html
        <!doctype html>
        <html>
            <head>
              {% if title %}
              <title>{{ title }} - Test_Server</title>
              {% else %}
              <title>Welcome to Test_Server</title>
              {% endif %}
            </head>
            <body>
                <div>Test_Server: <a href="/index">Home</a></div>
                <hr>
                {% block content %}{% endblock %}
            </body>
        </html>
        ```
    *   **`app/templates/index.html`**:
        ```html
        {% extends "base.html" %}

        {% block content %}
            <h1>Hi, {{ user.username }}!</h1>
            {% for post in posts %}
            <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
            {% endfor %}
        {% endblock %}
        ```
    *   **`server.py`**: (Same as Chapter 1)
        ```python
        from app import app
        ```

3.  **Run the Application**:
    *   Open your terminal or command prompt.
    *   Navigate to the `Week_07/Chapter_2` directory.
    *   Ensure you have Flask installed (`pip install Flask`).
    *   Run the command: `flask run`
    *   Open your web browser and go to `http://127.0.0.1:5000/` or `http://127.0.0.1:5000/index`. You should see a dynamic page with a greeting and posts.

## How It Works

*   **`app/routes.py`**: This file now uses `render_template('index.html', ...)` to render the `index.html` file. It passes Python variables (`user`, `posts`, `title`) to the template.
*   **`app/templates/base.html`**: This is the parent template. It defines the basic HTML structure, including the `<head>` and `<body>` sections. The `{% block content %}{% endblock %}` part is a placeholder where child templates can insert their specific content.
*   **`app/templates/index.html`**: This template `{% extends "base.html" %}` inherits from `base.html`. The `{% block content %}` section in this file contains the content specific to the home page.
    *   `{{ user.username }}`: This Jinja2 syntax displays the `username` from the `user` dictionary passed from `routes.py`.
    *   `{% for post in posts %}`: This Jinja2 loop iterates over the `posts` list, displaying the author and body for each post.
*   **Flask and Jinja2**: When `render_template` is called, Flask finds the specified HTML file in the `templates` folder, parses it with Jinja2, replaces template variables and executes control structures using the data provided, and then sends the resulting HTML back to the browser.

---

**Special Thanks** to Miguel Grinberg for the excellent Flask Mega-Tutorial! His clear and easy-to-follow guide has been invaluable in learning Flask.

Check out his project repository: [https://github.com/miguelgrinberg/microblog](https://github.com/miguelgrinberg/microblog)

---