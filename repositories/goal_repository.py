from db.run_sql import run_sql
from models.goal import Goal


def save(goal):
    sql = """INSERT INTO goals 
    (title, rep_start, rep_end, sets) 
    VALUES (%s, %s, %s, %s) RETURNING id
    """
    values = [goal.title, goal.rep_start, goal.rep_end, goal.sets]
    results = run_sql(sql, values)
    id = results[0]['id']
    goal.id = id


def select_all():
    goals = []
    sql = "SELECT * FROM goals"
    results = run_sql(sql)
    for result in results:
        goal = Goal(result["title"], result["rep_start"], result["rep_end"], result["sets"], result["id"])
        goals.append(goal)
    return goals


def select(id):
    goal = None 
    sql = "SELECT * FROM goals WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        goal = Goal(result["title"], result["rep_start"], result["rep_end"], result["sets"], result["id"])
    return goal


def delete_all():
    sql = "DELETE FROM goals"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM goals WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(goal):
    sql = """
    UPDATE goals SET 
    (title, rep_start, rep_end, sets) = 
    (%s, %s, %s, %s) WHERE id = %s
    """
    values = [goal.title, goal.rep_start, goal.rep_end, goal.sets, goal.id]
    run_sql(sql, values)
