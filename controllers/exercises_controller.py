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


@exercises_blueprint.route("/exercises", methods=["POST"])
def create_exercise():
    name = request.form["name"]
    muscle_group = request.form["muscle_group"]
    if request.form["duration"]:
        duration = request.form["duration"]
        new_exercise = Exercise(name, muscle_group, duration)
    else:
        new_exercise = Exercise(name, muscle_group)
    exercise_repository.save(new_exercise)
    return redirect("exercises")


@exercises_blueprint.route("/exercises/<id>/delete", methods=["POST"])
def delete_exercise(id):
    exercise_repository.delete(id)
    return redirect("/exercises")