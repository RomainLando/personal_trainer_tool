from flask import Blueprint, redirect, render_template, request

from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository

exercises_blueprint = Blueprint("exercises", __name__)


@exercises_blueprint.route("/exercises")
def exercises():
    exercises = exercise_repository.select_all()
    return render_template("exercises/index.html", exercises=exercises)

@exercises_blueprint.route("/exercises/new")
def new_exercise():
    return render_template("exercises/new.html")