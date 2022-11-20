# personal_trainer_tool

:star: This is a management tool for personal trainers to help them build, edit and allocate training plans and exercises to their clients :star:

![Home page image](/static/images/home_page.png)

Create a database of exercises you feel comfortable teaching to your clients:

![Exercises page](/static/images/exercises.png)

Add new clients as your client-base grows

![New client page](/static//images/new_client.png)

# How to run
First you'll need to create a database called "personal_trainer" using the code `createdb personal_trainer`
This requires posgres to be installed on your machine.

you can then navigate to the repository and run `python3 db/personal_trainer.sql` to create the neccesary tables in the database.

To populate the you will need to install psycopg2 on your device and run the code `python3 console.py`.

once this is done, make sure Flask is installed and run the code `flask --app app.py --debug run` and oppen the IP address on your browser to view the website. Remember to terminate flask once you're done using cmd+c.



## Specifications 

This solution will be built using only:

* HTML / CSS
* Python
* Flask
* PostgreSQL and the psycopg
* unit testing

it is a solo project with the aim being to consolidate learning of TDD, OOP, git and full-stack development.

## Deadline

This timescale for this solution is **1 week** 

## MVP

The app should allow the PT:
* to create and edit clients
* to create and edit programs 
* to allocate programs to clients
* to view all clients
* to view all programs
* to view all programs allocated to a particular client

## Extension

The app could also allow the client:
* to view their programs 
* to edit some of their attributes (only certain attributes)



## Advanced Extension

The app would also have the added funcitonalities of:
* allowing clients to view workouts they need to complete
* allowing trainers to view a client's workouts
* allowing clients to send feedback for a given workout
* allowing clients to mark workouts as done or incomplete
* allow the PT to view a client's workouts and their individual statuses (in the form of a calendar?)

## Super advanced

Create a dashboard for user with:
* BMI
* VO2-max
* weight / time graph
