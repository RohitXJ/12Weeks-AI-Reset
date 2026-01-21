# Week 07: Chapter 2 - HTML Templates and Dynamic Content

This chapter builds on the basic Flask application from Chapter 1 by introducing HTML templating to create dynamic web pages.

## What's New?

Instead of returning plain text, the `index` route now renders an HTML page. We've introduced the **Jinja2 templating engine** to embed dynamic data within the HTML. This involves creating a `templates` folder to store our HTML files and using Flask's `render_template()` function.

We also introduce **template inheritance**, where a `base.html` file provides the main structure, and other pages like `index.html` extend it.

## File Changes

### New Files

1.  **`app/templates/base.html`**: The main site layout. Other templates will inherit from this file.
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

2.  **`app/templates/index.html`**: The home page content, which extends the base layout.
    ```html
    {% extends "base.html" %}

    {% block content %}
        <h1>Hi, {{ user.username }}!</h1>
        {% for post in posts %}
        <div><p>{{ post.author.username }} says: <b>{{ post.body }}</b></p></div>
        {% endfor %}
    {% endblock %}
    ```

### Modified Files

1.  **`app/routes.py`**: Updated to import `render_template` and pass dynamic data (a user dictionary and a list of posts) to the `index.html` template.
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

## How It Works

*   The `index()` function in `routes.py` no longer returns a simple string. It calls `render_template()`, passing the filename of the template and the data to be rendered as keyword arguments.
*   Jinja2 (the template engine) processes the files. `{% extends "base.html" %}` in `index.html` sets up inheritance.
*   Placeholders like `{{ user.username }}` are replaced with the data passed from the route.
*   Control structures like `{% for post in posts %}` allow for complex logic directly in the HTML.

---

**Special Thanks** to Miguel Grinberg for the excellent Flask Mega-Tutorial! His clear and easy-to-follow guide has been invaluable in learning Flask.

Check out his project repository: [https://github.com/miguelgrinberg/microblog](https://github.com/miguelgrinberg/microblog)

---
