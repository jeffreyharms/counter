from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/')
def get_all_visits():
    if session["num_of_visits"]:
        session["num_of_visits"] += 1
    else:
        session["num_of_visits"] = 1
    if request.method == "POST":
        return render_template("index.html")
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session["num_of_visits"] = 0
    return render_template("index.html")