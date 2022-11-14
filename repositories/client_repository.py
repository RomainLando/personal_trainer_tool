from db.run_sql import run_sql
from models.client import Client
from repositories import goal_repository

def save(client):
    sql = """INSERT INTO clients 
    (first_name, last_name, age, height, weight, goal_id) 
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
    """
    values = [client.first_name, client.last_name,
    client.age, client.height, client.weight, client.goal.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    client.id = id


def select_all():
    clients = []
    sql = "SELECT * FROM clients"
    results = run_sql(sql)
    
    for result in results:
        goal_id = result['goal_id']
        goal = goal_repository.select(goal_id)
        client = Client(result["first_name"], result["last_name"],
        result["age"], result["height"], result["weight"], goal, result['id'])
        clients.append(client)
    return clients

def select(id):
    client = None
    sql = """
    SELECT * FROM clients
    WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        goal_id = result['goal_id']
        goal = goal_repository.select(goal_id)
        client = Client(result["first_name"], result["last_name"],
        result["age"], result["height"], result["weight"], goal, result['id'])
    return client

def delete_all():
    sql= "DELETE FROM clients"
    run_sql(sql)

def delete(id):
    sql = """
    DELETE FROM clients
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

def update(client):
    sql = """
    UPDATE clients SET 
    (first_name, last_name, age, height, weight, goal_id)
    = (%s, %s, %s, %s, %s, %s)
    WHERE id = %s
    """
    values = [client.first_name, client.last_name, client.age,
    client.height, client.weight, client.goal.id, client.id]
    run_sql(sql, values)