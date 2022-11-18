from db.run_sql import run_sql
from models.client_program import ClientProgram


def save(client_program):
    sql = """INSERT INTO client_programs 
    (client_id, program_id) 
    VALUES (%s, %s) RETURNING id
    """
    values = [client_program.client.id, client_program.program.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    client_program.id = id


def delete_by_client_id(id):
    sql = """
    DELETE FROM client_programs
    WHERE client_id = %s
    """
    values = [id]
    run_sql(sql, values)