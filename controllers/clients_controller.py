from flask import Blueprint, redirect, render_template, request

from models.client import Client
import repositories.client_repository as client_repository


clients_blueprint = Blueprint("clients", __name__)

@clients_blueprint.route("/clients")
def clients():
    clients = client_repository.select_all()
    return render_template("/clients/index.html", clients=clients)