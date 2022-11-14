from db.run_sql import run_sql
from models.program import Program

def save(program):
    sql = """INSERT INTO programs 
    (title) VALUES (%s) RETURNING id
    """
    values = [program.title]
    results = run_sql(sql, values)
    id = results[0]['id']
    program.id = id


def select_all():
    programs = []
    sql = "SELECT * FROM programs"
    results = run_sql(sql)
    for result in results:
        program = Program(result["title"], result["id"])
        programs.append(program)
    return programs


def select(id):
    program = None 
    sql = "SELECT * FROM programs WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        program = Program(result["title"], result["id"])
    return program


def delete_all():
    sql = "DELETE FROM programs"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM programs WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(program):
    sql = """
    UPDATE programs SET 
    title = %s WHERE id = %s
    """
    values = [program.title, program.id]
    run_sql(sql, values)
