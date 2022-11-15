from flask import Blueprint, redirect, render_template, request

from models.goal import Goal
import repositories.goal_repository as goal_repository

goals_blueprint = Blueprint("goals", __name__)

@goals_blueprint.route("/goals")
def goals():
    goals = goal_repository.select_all()
    return render_template("goals/index.html", goals = goals)

@goals_blueprint.route("/goals/new")
def new_goal():
    return render_template("goals/new.html")

@goals_blueprint.route("/goals", methods=["POST"])
def create_goal():
    title = request.form["title"]
    rep_start = request.form["rep_start"]
    rep_end = request.form["rep_end"]
    sets = request.form["sets"]
    new_goal = Goal(title, rep_start, rep_end, sets)
    goal_repository.save(new_goal)
    return redirect("/goals")

@goals_blueprint.route("/goals/<id>/delete", methods=["POST"])
def delete_goal(id):
    goal_repository.delete(id)
    return redirect("/goals")

@goals_blueprint.route("/goals/<id>/edit")
def edit_goal(id):
    goal = goal_repository.select(id)
    return render_template("/goals/edit.html", goal=goal)

@goals_blueprint.route("/goals/<id>", methods=["POST"])
def update_goal(id):
    title = request.form["title"]
    rep_start = request.form["rep_start"]
    rep_end = request.form["rep_end"]
    sets = request.form["sets"]
    new_goal = Goal(title, rep_start, rep_end, sets, id)
    goal_repository.update(new_goal)
    return redirect("/goals")