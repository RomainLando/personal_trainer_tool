from flask import Blueprint, redirect, render_template, request

from models.client import Client
from models.client_program import ClientProgram
import repositories.client_repository as client_repository
import repositories.program_repository as program_repository
import repositories.goal_repository as goal_repository
import repositories.client_program_repository as client_program_repository
clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def clients():
    clients = client_repository.select_all()
    return render_template("/clients/index.html", clients=clients)

@clients_blueprint.route("/clients/<id>")
def show_client(id):
    client = client_repository.select(id)
    programs = client_repository.show_programs(client)
    return render_template("clients/client.html", client = client, programs = programs)

@clients_blueprint.route("/clients/new")
def new_client():
    programs = program_repository.select_all()
    goals = goal_repository.select_all()
    return render_template("/clients/new.html", programs = programs, goals = goals)

@clients_blueprint.route("/clients", methods=["POST"])
def create_client():
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    age = request.form["age"]
    weight = request.form["weight"]
    height = request.form["height"]
    goal_id = request.form["goal_id"]
    goal = goal_repository.select(int(goal_id))
    new_client = Client(first_name, last_name, age, height, weight, goal)
    client_repository.save(new_client)
    programs_id = request.form.getlist('programs_id')
    for program_id in programs_id:
        program = program_repository.select(int(program_id))
        new_client_program = ClientProgram(new_client, program)
        print(new_client_program.client)
        print(new_client_program.program)
        print(new_client_program.id)
        client_program_repository.save(new_client_program)
    return redirect("/clients")

@clients_blueprint.route("/clients/<id>/delete", methods=["POST"])
def delete_client(id):
    client_repository.delete(id)
    return redirect("/clients")



@clients_blueprint.route("/clients/<id>/edit")
def edit_client(id):
    client = client_repository.select(id)
    programs = program_repository.select_all()
    client_programs = client_repository.show_programs(client)
    client_programs_ids = [client_program.id for client_program in client_programs]
    return render_template("/clients/edit.html", client = client, programs = programs, client_programs_ids = client_programs_ids)
