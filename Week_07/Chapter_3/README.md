# Week 07: Chapter 3 - Web Forms and Configuration

This chapter enhances the application from Chapter 2 by adding a login form and moving the application's configuration into a separate file.

## What's New?

We introduce the **Flask-WTF** extension to handle web forms. This allows us to define forms in Python, render them in templates, and process user submissions securely with built-in **CSRF protection**.

We also create a `config.py` file to store settings like the `SECRET_KEY`, separating configuration from application logic. User feedback is handled with Flask's `flash()` and `get_flashed_messages()` system.

## File Changes

### New Files

1.  **`config.py`**: A dedicated file for application settings.
    ```python
    import os

    class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    ```

2.  **`app/forms.py`**: Defines the structure and validation for our web forms.
    ```python
    from flask_wtf import FlaskForm
    from wtforms import StringField, PasswordField, BooleanField, SubmitField
    from wtforms.validators import DataRequired

    class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember_me = BooleanField('Remember Me')
        submit = SubmitField('Sign In')
    ```

3.  **`app/templates/login.html`**: The template for rendering the new login form.
    ```html
    {% extends "base.html" %}

    {% block content %}
        <h1>Sign In</h1>
        <form action="" method="post" novalidate>
            {{ form.hidden_tag() }}
            <p>
                {{ form.username.label }}<br>
                {{ form.username(size=32) }}<br>
                {% for error in form.username.errors %}
                <span style="color: red;">[{{ error }}]</span>
                {% endfor %}
            </p>
            <p>
                {{ form.password.label }}<br>
                {{ form.password(size=32) }}<br>
                {% for error in form.password.errors %}
                <span style="color: red;">[{{ error }}]</span>
                {% endfor %}
            </p>
            <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
            <p>{{ form.submit() }}</p>
        </form>
    {% endblock %}
    ```

### Modified Files

1.  **`app/__init__.py`**: Updated to load configuration from the `Config` object.
    ```python
    from flask import Flask
    from config import Config

    app = Flask(__name__)
    app.config.from_object(Config)

    from app import routes
    ```

2.  **`app/routes.py`**: A new `/login` route is added to display and process the form. It handles both `GET` (showing the form) and `POST` (processing data) requests.
    ```python
    from flask import render_template, flash, redirect, url_for
    from app import app
    from app.forms import LoginForm

    # ... index() route is unchanged ...

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            flash('Login requested for user {}, remember_me={}'.format(
                form.username.data, form.remember_me.data))
            return redirect(url_for('index'))
        return render_template('login.html', title='Sign In', form=form)
    ```

3.  **`app/templates/base.html`**: Modified to add a "Login" link and a section to display flashed messages to the user.
    ```html
    ...
    <body>
        <div>
            XR-Blog:
            <a href="{{ url_for('index') }}">Home</a>
            <a href="{{ url_for('login') }}">Login</a>
        </div>
        <hr>
        {% with messages = get_flashed_messages() %}
        {% if messages %}
        <ul>
            {% for message in messages %}
            <li>{{ message }}</li>
            {% endfor %}
        </ul>
        {% endif %}
        {% endwith %}
        {% block content %}{% endblock %}
    </body>
    ...
    ```

## How It Works

*   The `SECRET_KEY` in `config.py` is used by Flask-WTF to create secure CSRF tokens.
*   The `LoginForm` class in `forms.py` defines the fields and validation rules.
*   The `login` route creates an instance of `LoginForm`. If the form is submitted (`POST`) and valid, `form.validate_on_submit()` returns `True`.
*   `flash()` stores a message that will be shown on the *next* page the user visits. `redirect(url_for('index'))` sends them to the index page.
*   The `login.html` template uses the `form` object to render the fields. `{{ form.hidden_tag() }}` is essential for CSRF protection.
*   `base.html` uses `get_flashed_messages()` to retrieve and display any pending messages.

---

**Special Thanks** to Miguel Grinberg for the excellent Flask Mega-Tutorial! His clear and easy-to-follow guide has been invaluable in learning Flask.

Check out his project repository: [https://github.com/miguelgrinberg/microblog](https://github.com/miguelgrinberg/microblog)

---