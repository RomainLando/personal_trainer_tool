import pdb

from models.goal import Goal
from models.exercise import Exercise
from models.program import Program

import repositories.goal_repository as goal_repository
import repositories.exercise_repository as exercise_repository
import repositories.program_repository as program_repository

program_repository.delete_all()
# goal_repository.delete_all()
# exercise_repository.delete_all()


goal1 = Goal("General fitness", 8, 9, 3)
goal2 = Goal("Hypertrophy", 6, 12, 4)
goal3 = Goal("Strength", 2, 6, 4)
goal4 = Goal("Endurance", 12, 20, 3)

# goal_repository.save(goal1)
# goal_repository.save(goal2)
# goal_repository.save(goal3)
# goal_repository.save(goal4)


exercise1 = Exercise("Squats", "Lower Body")
exercise2 = Exercise("Jogging", "Full Body", 30)
exercise3 = Exercise("Push-ups", "Upper Body")
exercise4 = Exercise("Crunches", "Core")
exercise5 = Exercise("Plank", "Core", 1)
exercise6 = Exercise("Back Extensions", "Core")
exercise7 = Exercise("Pull-ups", "Upper Body")
exercise8 = Exercise("Deadlifts", "Legs")
exercise9 = Exercise("Lateral Raises", "Upper Body")
exercise10 = Exercise("Rows", "Upper Body")

# exercise_repository.save(exercise1)
# exercise_repository.save(exercise2)
# exercise_repository.save(exercise3)
# exercise_repository.save(exercise4)
# exercise_repository.save(exercise5)
# exercise_repository.save(exercise6)
# exercise_repository.save(exercise7)
# exercise_repository.save(exercise8)
# exercise_repository.save(exercise9)
# exercise_repository.save(exercise10)


program1 = Program("Legs")
program2 = Program("Push")
program3 = Program("Pull")
program4 = Program("Full Body")

# program_repository.save(program1)
# program_repository.save(program2)
# program_repository.save(program3)
# program_repository.save(program4)




pdb.set_trace()