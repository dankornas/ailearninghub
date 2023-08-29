import os
from flask import Flask, send_from_directory, redirect, url_for, request, render_template
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user

app = Flask(__name__, static_folder="site")
app.config["SECRET_KEY"] = "your-secret-key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


class User(UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email != "user@example.com":
        return

    user = User()
    user.id = email
    return user


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return """
                <form method='POST'>
                <input type='text' name='email' id='email' placeholder='email'></input>
                <input type='password' name='password' id='password' placeholder='password'></input>
                <input type='submit' name='submit'></input>
                </form>
                """

    email = request.form["email"]
    if request.form["password"] == "password" and email == "user@example.com":
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for("serve"))

    return "Bad login"


@app.route("/logout")
def logout():
    logout_user()
    return "Logged out"


@app.route("/about/", methods=["GET", "POST"])
@login_required
def about():
    print("Inside about route")
    return "You are viewing the about page"


@app.route("/test")
def test():
    return "This is a test route"


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path == "":
        return send_from_directory(app.static_folder, "index.html")
    elif path != "" and os.path.exists(os.path.join(app.static_folder, path, "index.html")):
        return send_from_directory(app.static_folder, os.path.join(path, "index.html"))
    elif os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, "index.html")


if __name__ == "__main__":
    app.run(port=5000)
