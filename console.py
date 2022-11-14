import pdb

from models.goal import Goal
from models.exercise import Exercise
import repositories.goal_repository as goal_repository
import repositories.exercise_repository as exercise_repository

exercise_repository.delete_all()


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


pdb.set_trace()