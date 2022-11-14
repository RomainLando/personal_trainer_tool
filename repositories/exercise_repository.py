from db.run_sql import run_sql
from models.exercise import Exercise

def save(exercise):
    sql = """INSERT INTO exercises 
    (name, muscle_group, duration) 
    VALUES (%s, %s, %s) RETURNING id
    """
    values = [exercise.name, exercise.muscle_group, exercise.duration]
    results = run_sql(sql, values)
    id = results[0]['id']
    exercise.id = id


def select_all():
    exercises = []
    sql = "SELECT * FROM exercises"
    results = run_sql(sql)
    for result in results:
        exercise = Exercise(result["name"], result["muscle_group"], result["duration"], result["id"])
        exercises.append(exercise)
    return exercises


def select(id):
    exercise = None 
    sql = "SELECT * FROM exercises WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        exercise = Exercise(result["name"], result["muscle_group"], result["duration"], result["id"])
    return exercise


def delete_all():
    sql = "DELETE FROM exercises"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM exercises WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(exercise):
    sql = """
    UPDATE exercises SET 
    (name, muscle_group, duration) = 
    (%s, %s, %s) WHERE id = %s
    """
    values = [exercise.name, exercise.muscle_group, exercise.duration, exercise.id]
    run_sql(sql, values)
