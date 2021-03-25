from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, BooleanField, validators
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = "i493i8nv9854bb95384nfvu948b5v9840v4b0v4f"


class LoginForm(FlaskForm):
    email = StringField(label="Email",
                        validators=[validators.Email(), DataRequired()],
                        render_kw={"placeholder": "admin@email.com"})
    password = PasswordField(label="Password",
                             validators=[validators.Length(min=8, max=25), DataRequired()],
                             render_kw={"placeholder": "12345678"})
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        login_email = login_form.email.data
        login_password = login_form.password.data
        if login_email == "admin@email.com" and login_password == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
