DROP TABLE IF EXISTS client_programs;
DROP TABLE IF EXISTS workouts;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS goals;
DROP TABLE IF EXISTS programs;
DROP TABLE IF EXISTS exercises;

CREATE TABLE goals (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    rep_start INT,
    rep_end INT,
    sets INT
);

CREATE TABLE programs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255)
);

CREATE TABLE exercises (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    muscle_group VARCHAR(255),
    duration INT
);

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT NOT NULL,
    height INT,
    weight INT,
    goal_id INT NOT NULL REFERENCES goals(id) ON DELETE CASCADE
);

CREATE TABLE client_programs (
    id SERIAL PRIMARY KEY,
    client_id INT NOT NULL REFERENCES clients(id) ON DELETE CASCADE,
    program_id INT NOT NULL REFERENCES programs(id) ON DELETE CASCADE
);

CREATE TABLE workouts (
    id SERIAL PRIMARY KEY,
    program_id INT NOT NULL REFERENCES programs(id) ON DELETE CASCADE,
    exercise_id INT NOT NULL REFERENCES exercises(id) ON DELETE CASCADE
);