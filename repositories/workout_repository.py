from db.run_sql import run_sql
from models.workout import Workout
from repositories import program_repository, exercise_repository

def save(workout):
    sql = """INSERT INTO workouts 
    (program_id, exercise_id) 
    VALUES (%s, %s) RETURNING id
    """
    values = [workout.program.id, workout.exercise.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    workout.id = id


def select_all():
    workouts = []
    sql = "SELECT * FROM workouts"
    results = run_sql(sql)
    
    for result in results:
        exercise_id = result['exercise_id']
        program_id = result['program_id']
        exercise = exercise_repository.select(exercise_id)
        program = program_repository.select(program_id)
        workout = Workout(program, exercise, result['id'])
        workouts.append(workout)
    return workouts

def select(id):
    workout = None
    sql = """
    SELECT * FROM workouts
    WHERE id = %s
    """
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        exercise_id = result['exercise_id']
        program_id = result['program_id']
        exercise = exercise_repository.select(exercise_id)
        program = program_repository.select(program_id)
        workout = Workout(program, exercise, result['id'])
    return workout

def delete_all():
    sql= "DELETE FROM workouts"
    run_sql(sql)

def delete(id):
    sql = """
    DELETE FROM workouts
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)

def update(workout):
    sql = """
    UPDATE workouts SET (program_id, exercise_id) = (%s, %s) 
    WHERE id = %s
    """
    values = [ workout.program.id, workout.exercise.id, workout.id]
    run_sql(sql, values)