from db.run_sql import run_sql
from models.client_program import ClientProgram

from repositories import program_repository, client_repository

def save(client_program):
    sql = """INSERT INTO client_programs 
    (client_id, program_id) 
    VALUES (%s, %s) RETURNING id
    """
    values = [client_program.client.id, client_program.program.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    client_program.id = id


def select_all():
    client_programs = []
    sql = "SELECT * FROM client_programs"
    results = run_sql(sql)
    
    for result in results:
        client_id = result['client_id']
        program_id = result['program_id']
        client = client_repository.select(client_id)
        program = program_repository.select(program_id)
        client_program = ClientProgram(client, program, result['id'])
        client_programs.append(client_program)
    return client_programs

def select(id):
    client_program = None
    sql = """
    SELECT * FROM client_programs
    WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        client_id = result['client_id']
        program_id = result['program_id']
        client = client_repository.select(client_id)
        program = program_repository.select(program_id)
        client_program = ClientProgram(client, program, result['id'])
    return client_program

def delete_all():
    sql= "DELETE FROM client_programs"
    run_sql(sql)

def delete(id):
    sql = """
    DELETE FROM client_programs
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

def update(client_program):
    sql = """
    UPDATE client_programs SET (client_id, program_id) = (%s, %s) 
    WHERE id = %s
    """
    values = [client_program.client.id, client_program.program.id, client_program.id]
    run_sql(sql, values)

def select_by_client_program_ids(client_id, program_id):
    sql = """
    SELECT * FROM client_programs
    WHERE client_id = %s
    AND program_id = %s
    """
    values = [client_id, program_id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        client_id = result['client_id']
        program_id = result['program_id']
        client = client_repository.select(client_id)
        program = program_repository.select(program_id)
        client_programs = ClientProgram(client, program, result['id'])
    return client_programs

def delete_by_client_id(id):
    sql = """
    DELETE FROM client_programs
    WHERE client_id = %s
    """
    values = [id]
    run_sql(sql, values)