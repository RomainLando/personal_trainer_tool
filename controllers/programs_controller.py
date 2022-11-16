from flask import Blueprint, redirect, render_template, request

from models.program import Program
from models.workout import Workout
import repositories.program_repository as program_repository
import repositories.exercise_repository as exercise_repository
import repositories.workout_repository as workout_repository

programs_blueprint = Blueprint("programs", __name__)

@programs_blueprint.route("/programs")
def programs():
    programs = program_repository.select_all()
    return render_template("/programs/index.html", programs=programs)

@programs_blueprint.route("/programs/<id>")
def show_program(id):
    program = program_repository.select(id)
    exercises = program_repository.show_exercises(program)
    return render_template('programs/program.html', program=program, exercises=exercises)

@programs_blueprint.route("/programs/new")
def new_program():
    exercises = exercise_repository.select_all()
    return render_template("programs/new.html", exercises=exercises)

@programs_blueprint.route("/programs", methods=["POST"])
def create_program():
    title = request.form["title"]
    new_program = Program(title)
    program_repository.save(new_program)
    exercises_id = request.form.getlist('exercises_id')
    for exercise_id in exercises_id:
        new_exercise = exercise_repository.select(int(exercise_id))
        new_workout = Workout(new_program, new_exercise)
        workout_repository.save(new_workout)
    return redirect("/programs")

@programs_blueprint.route("/programs/<id>/delete", methods=["POST"])
def delete_program(id):
    program_repository.delete(id)
    return redirect("/programs")

@programs_blueprint.route("/programs/<id>/edit")
def edit_program(id):
    program = program_repository.select(id)
    exercises = exercise_repository.select_all()
    workout = program_repository.show_exercises(program)
    workout_ids = [program_exercise.id for program_exercise in workout]
    return render_template("programs/edit.html", program=program, exercises=exercises, workout_ids=workout_ids)

@programs_blueprint.route("/programs/<id>", methods=["POST"])
def update_program(id):
    title = request.form["title"]
    new_program = Program(title, id)
    program_repository.update(new_program)
    exercises = program_repository.show_exercises(new_program)
    for exercise in exercises:
        workout = workout_repository.select_by_program_exercise_ids(new_program.id, exercise.id)
        workout_repository.delete(workout.id)
    exercises_id = request.form.getlist('exercises_id')
    for exercise_id in exercises_id:
        new_exercise = exercise_repository.select(int(exercise_id))
        new_workout = Workout(new_program, new_exercise)
        workout_repository.save(new_workout)
    return redirect("/programs")

@programs_blueprint.route("/programs/<program_id>/<exercise_id>/delete", methods=["POST"])
def remove_exercise(program_id, exercise_id):
    workout = workout_repository.select_by_program_exercise_ids(program_id, exercise_id)
    workout_repository.delete(workout.id)
    return redirect(f"/programs/{program_id}")