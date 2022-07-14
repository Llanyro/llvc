from sys import exit
from AccessControl import AccessController
from flask_utils import get_args, prepare_cookie_and_template
from flask import Flask, render_template, request, jsonify, redirect, make_response, abort, send_file


app = Flask(__name__)
session = AccessController("users.db", False)
EMAIL: str = "email"
PASSWORD: str = "password"
COOKIE_KEY: str = "ll_git_session"


# region Functions
def save_data(sig, frame):
    exit(0)


def do_by_cookie(function_1, function_2, function_3, function_1_args=None, function_2_args=None, function_3_args=None):
    """
    Function 2 get cookie by first parameter
    """
    cookiesesion = request.cookies.get(COOKIE_KEY)
    if cookiesesion is None:
        if function_1_args is not None:
            result = function_1(function_1_args)
        else:
            result = function_1()
    elif session.is_logged(cookiesesion):
        if function_2_args is not None:
            result = function_2(cookiesesion, function_2_args)
        else:
            result = function_2(cookiesesion)
    else:
        if function_1_args is not None:
            result = function_3(function_3_args)
        else:
            result = function_3()
    return result


# endregion
# region Session
def get_index_or_home_by_cookie() -> any:
    return do_by_cookie(index_html, home_html, index_html, False, False, True)


def session_start(session_function):
    d: dict = get_args(request)
    if d.get(EMAIL) is not None and d.get(PASSWORD) is not None:
        r, cookie = session_function(d.get(EMAIL), d.get(PASSWORD))
        # Si nos devuelve una cookie valida, se ha añadido el usuario
        if r:
            result = home_html(cookie, False)
        else:
            result = index_html(False)
    else:
        result = "Email and password requiered"
    return result


def session_logout(cookie: str):
    session.logout(cookie)
    return index_html(True)


def home_html(cookie: str, expire: bool):
    return prepare_cookie_and_template("home.html", COOKIE_KEY, cookie, expire)


def index_html(expire: bool):
    if expire:
        result = make_response(render_template("index.html"))
        result.set_cookie(COOKIE_KEY, "0", httponly=True, expires=0)
    else:
        result = render_template("index.html")
    return result


@app.route("/signin", methods=["GET", "POST"])
def signin():
    if request.method == "GET":
        result = get_index_or_home_by_cookie()
    elif request.method == "POST":
        """
        If there is no email or pass returns to signin page
        If the user exist returns to signin page
        If the user is added, returns to home page
        """
        result = session_start(session.signin)
    else:
        result = "Invalid method"
    return result


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        result = get_index_or_home_by_cookie()
    elif request.method == "POST":
        result = session_start(session.login)
    else:
        result = "Invalid method"
    return result


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if request.method == "GET":
        result = get_index_or_home_by_cookie()
    elif request.method == "POST":
        # If user doesn't have cookie, returns to index
        # If user has cookie, but it's invalid, returns to index, and reset cookie
        # If user has cookie, and it's valid, returns to index, and reset cookie
        result = do_by_cookie(index_html, session_logout, index_html, function_1_args=False, function_3_args=True)
    else:
        result = "Invalid method"
    return result


# endregion
# region Resources
@app.route('/', methods=["GET"])
def root():
    return redirect("/login")

# endregion


if __name__ == '__main__':
    app.run(port=8080, host='localhost', debug=False)  # , ssl_context='adhoc')