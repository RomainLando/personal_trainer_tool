from flask import Blueprint, redirect, render_template, request

from models.exercise import Exercise
import repositories.exercise_repository as exercise_repository

exercises_blueprint = Blueprint("exercises", __name__)

# ALL
@exercises_blueprint.route("/exercises")
def exercises():
    exercises = exercise_repository.select_all()
    return render_template("exercises/index.html", exercises=exercises)

# NEW
@exercises_blueprint.route("/exercises/new")
def new_exercise():
    return render_template("exercises/new.html")

# CREATE
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

# DELETE
@exercises_blueprint.route("/exercises/<id>/delete", methods=["POST"])
def delete_exercise(id):
    exercise_repository.delete(id)
    return redirect("/exercises")

# EDIT
@exercises_blueprint.route("/exercises/<id>/edit")
def edit_exercise(id):
    exercise = exercise_repository.select(id)
    return render_template("exercises/edit.html", exercise=exercise)


@exercises_blueprint.route("/exercises/<id>", methods=["POST"])
def update_exercise(id):
    name = request.form["name"]
    muscle_group = request.form["muscle_group"]
    if request.form["duration"]:
        duration = request.form["duration"]
        new_exercise = Exercise(name, muscle_group, duration, id)
    else:
        new_exercise = Exercise(name, muscle_group, None, id)
    exercise_repository.update(new_exercise)
    return redirect("/exercises")

