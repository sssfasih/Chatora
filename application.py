import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    data = db.execute("SELECT * from ownership WHERE user_id=(?)", (session["user_id"]))
    cash = db.execute("SELECT cash FROM users WHERE id=(?)", (session["user_id"]))
    counter = 0
    g_total = 0
    for dicts in data:
        counter += 1
        current_data = lookup(dicts["symbol"])
        total = dicts["quantity"] * current_data["price"]
        current_data["total"] = usd(total)
        current_data["price"] = usd(current_data["price"])
        dicts["current_data"] = current_data
        dicts["count"] = counter

        g_total += (total)
    g_total += cash[0]["cash"]
    print(data)
    return render_template("index.html", data=data, cash=usd(cash[0]["cash"]), g_total=usd(g_total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    else:
        s = request.form.get("symbol")
        if not s:
            return apology("Symbol can't be left blaNk")

        elif lookup(s) == None:
            return apology("Invalid Symbol")
        try:
            shares = int(request.form.get("shares"))
            if shares < 1:
                raise ValueError
        except ValueError:
            return apology("Enter positive number")

        userid = session["user_id"]
        data = db.execute("SELECT cash from users WHERE id=(:user)", user=userid)

        cp = lookup(s)["price"]
        cost = cp * shares
        cash = data[0]["cash"]
        if cash < cost:
            return apology("Not Enough Cash")

        db.execute("UPDATE users SET cash=(?) WHERE id =(?)", (cash - cost, userid))
        x = db.execute("SELECT * FROM ownership WHERE symbol = (?) AND user_id = (?)", (s, userid))
        if not x:
            db.execute("INSERT INTO ownership (user_id,symbol,quantity) VALUES (:u,:s,:q)", u=userid, s=s, q=shares)
        else:
            db.execute("UPDATE ownership SET quantity = (?) WHERE symbol=(?) AND user_id = (?) ",
                       (x[0]["quantity"] + shares, s, userid))

        # print(f"u={userid},s={s},v={cp},p={cost}")
        db.execute("INSERT INTO history (user_id,symbol,quantity,value ,price) VALUES (:u,:s,:q,:v,:p)", u=userid, s=s,
                   q=shares, v=cp, p=cost)

        return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    data = db.execute("SELECT * FROM history where user_id = (?) ORDER BY trans_id", (session["user_id"]))
    for d in data:
        d["name"] = lookup(d["symbol"])["name"]
        if d["quantity"] < 0:
            d["quantity"] = -(d["quantity"])
            d["status"] = "SOLD"
        else:
            d["status"] = "BOUGHT"

    return render_template("history.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")
    else:
        sym = request.form.get("symbol")
        data = lookup(sym)
        if data == None:
            return apology("Not exist")
        price = usd(data["price"])

        return render_template("quoted.html", data=data, dollars=price)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("You must enter Username")
        elif not request.form.get("password"):
            return apology("You must enter Password")
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("Passwords didn't match")
        else:
            hashed = generate_password_hash(request.form.get("password"), method='pbkdf2:sha256', salt_length=8)
            db.execute("INSERT INTO users (username,hash) VALUES (:user, :hashed)", user=request.form.get("username"),
                       hashed=hashed)
            return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        data = db.execute("SELECT symbol,quantity FROM ownership WHERE user_id = (?)", session["user_id"])
        for d in data:
            current_data = lookup(d["symbol"])
            d["current_data"] = current_data
        print(data)
        return render_template("sell.html", data=data)

    s = request.form.get("symbol")
    if not s:
        return apology("Missing Symbol")
    try:
        q = int(request.form.get("shares"))
        if q < 1:
            raise ValueError
    except ValueError:
        return apology("Enter positive number")

    x = db.execute("SELECT symbol,quantity FROM ownership WHERE user_id = (?) AND symbol = (?)", session["user_id"], s)

    if not x:
        return apology("You don't own any stock of this company")
    elif x[0]["quantity"] < q:
        return apology("You don't own enough stocks to perform this operation")

    cp = lookup(s)["price"]
    revenue = cp * q
    cash = db.execute("SELECT cash FROM users WHERE id=(?)", session["user_id"])
    tcash = cash[0]["cash"] + revenue
    db.execute("UPDATE users SET cash = (?) WHERE id=(?)", tcash, session["user_id"])
    db.execute("UPDATE ownership SET quantity = (?) WHERE symbol = (?) AND user_id = (?)", x[0]["quantity"] - q, s,
               session["user_id"])
    db.execute("INSERT INTO history (user_id,symbol,quantity,value,price) VALUES (:id,:s,:q,:v,:p)",
               id=session["user_id"], s=s, q=-q, v=cp, p=revenue)

    return redirect("/")


@app.route("/change", methods=["GET", "POST"])
@login_required
def change():
    """Change Password """
    if request.method == "GET":
        return render_template("change.html")

    cpassword = request.form.get("cpassword")
    npassword = request.form.get("npassword")
    confirmation = request.form.get("confirmation")

    if npassword != confirmation:
        return apology("Passwords donot match")

    hashed = db.execute("SELECT hash FROM users WHERE id=(?)", session["user_id"])[0]["hash"]
    if check_password_hash(hashed, cpassword):
        hashed = generate_password_hash(npassword, method='pbkdf2:sha256', salt_length=8)
        db.execute("UPDATE users SET hash=(?) WHERE id=(?)", hashed, session["user_id"])
        return redirect("/")
    return apology("Wrong Current Password")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
