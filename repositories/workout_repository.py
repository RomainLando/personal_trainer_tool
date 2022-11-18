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


def delete(id):
    sql = """
    DELETE FROM workouts
    WHERE id = %s
    """
    values = [id]
    run_sql(sql, values)


def select_by_program_exercise_ids(program_id, exercise_id):
    sql = """
    SELECT * FROM workouts
    WHERE program_id = %s
    AND exercise_id = %s
    """
    values = [program_id, exercise_id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        exercise_id = result['exercise_id']
        program_id = result['program_id']
        exercise = exercise_repository.select(exercise_id)
        program = program_repository.select(program_id)
        workout = Workout(program, exercise, result['id'])
    return workout