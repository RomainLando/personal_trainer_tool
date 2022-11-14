import pdb

from models.goal import Goal
import repositories.goal_repository as goal_repository

goal1 = Goal("General fitness", 8, 9, 3)
goal2 = Goal("Hypertrophy", 6, 12, 4)
goal3 = Goal("Strength", 2, 6, 4)
goal4 = Goal("Endurance", 12, 20, 3)

goal_repository.save(goal1)
goal_repository.save(goal2)
goal_repository.save(goal3)
goal_repository.save(goal4)

goal4.title = "Weight loss"

goal_repository.update(goal4)
print(goal_repository.select(goal4.id))
pdb.set_trace()