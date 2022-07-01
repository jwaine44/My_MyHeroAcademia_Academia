from flask import session, render_template, request, redirect
from flask_app import app

from flask_app.models.villain_model import Villain


@app.route('/villains')
def display_villains():
    villains = Villain.get_all_villains()
    return render_template("villains.html", villains = villains)

@app.route('/villains/<name>')
def get_villain_by_name(name):
    data = {
        "name": name
    }
    villain = Villain.get_one_villain(data)
    return render_template('villain_profile.html', villain = villain)