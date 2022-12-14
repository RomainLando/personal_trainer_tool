from flask import Flask, render_template
from controllers.exercises_controller import exercises_blueprint
from controllers.goals_controller import goals_blueprint
from controllers.programs_controller import programs_blueprint
from controllers.clients_controller import clients_blueprint
app = Flask(__name__)

app.register_blueprint(exercises_blueprint)
app.register_blueprint(goals_blueprint)
app.register_blueprint(programs_blueprint)
app.register_blueprint(clients_blueprint)

@app.route("/")
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
