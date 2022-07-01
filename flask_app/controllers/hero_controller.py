from flask import session, render_template, request, redirect
from flask_app import app

from flask_app.models.hero_model import Hero



@app.route('/heroes')
def display_heroes():
    heroes = Hero.get_all_heroes()
    return render_template("heroes.html", heroes = heroes)

@app.route('/heroes/<name>')
def get_hero_by_name(name):
    data = {
        "name": name
    }
    hero = Hero.display_hero(data)
    return render_template('hero_profile.html', hero = hero)