# Project Title

US President Database

[Link to this repository](https://github.com/susmoi/Presidents-Database)

---

## Project Description

A program which creates a database of presidential information and presents it through a flask application

## How to run

1. First, you should install all requirements with `pip install -r requirements.txt` (still need to make requirements.txt file)
2. Second, you should run `flask_app.py runserver`
3. Copy URL from console into browser of your choosing and explore web app

## How to use

1. While on the homepage read through list of Presidents and select a president and copy link after URL
2. Or click one of the two links at top of page to be taken to either Presidents religion or education table

## Routes in this application

- `/` -> this is the home page-- Displayed here is a list of each of the president's name and their corresponding URL   
- `/table` -> this route shows a table of all the presidents and their information
- `/search/<fname>/<lname>` -> shows information one president in string format
- `/religion` -> shows a table of all the president's religions
- `/education` -> shows a table of all the president's education


## How to run tests
1. type or copy 'python -m unittest SI507project_tests.py' into console

## In this repository:

- FINAL_PROJECT
  - README.md
  - SI507project_tools.py
  - SI507project_tests.py
  - Advanced_expiry_caching.py
  - database_diagram.png
  - db.py
  - db_models.py
  - example_json_file.json
  - flask_app.py
  - requirements.txt

## Sources
https://millercenter.org/president


### General

- [X] Project is submitted as a Github repository
- [X] Project includes a working Flask application that runs locally on a computer
- [X] Project includes at least 1 test suite file with reasonable tests in it.
- [X] Includes a `requirements.txt` file containing all required modules to run program
- [X] Includes a clear and readable README.md that follows this template
- [X] Includes a sample .sqlite/.db file
- [X] Includes a diagram of your database schema
- [X] Includes EVERY file needed in order to run the project
- [X] Includes a clear descriptions of what your project should look like when it is working

### Flask Application

- [X] Includes at least 3 different routes
- [X] View/s a user can see when the application runs that are understandable/legible for someone who has NOT taken this course
- [X] Interactions with a database that has at least 2 tables
- [X] At least 1 relationship between 2 tables in database
- [X] Information stored in the database is viewed or interacted with in some way

### Additional Components (at least 6 required)

- [] Use of a new module
- [ ] Use of a second new module
- [ ] Object definitions using inheritance (indicate if this counts for 2 or 3 of the six requirements in a parenthetical)
- [X] A many-to-many relationship in your database structure
- [ ] At least one form in your Flask application
- [X] Templating in your Flask application
- [X] Inclusion of JavaScript files in the application
- [X] Links in the views of Flask application page/s
- [ ] Relevant use of `itertools` and/or `collections`
- [X] Sourcing of data using web scraping
- [ ] Sourcing of data using web REST API requests
- [ ] Sourcing of data using user input and/or a downloaded .csv or .json dataset
- [X] Caching of data you continually retrieve from the internet in some way

### Submission

- [X] I included a link to my GitHub repository with the correct permissions on Canvas! (Did you though? Did you actually? Are you sure you didn't forget?)
- [X] I included a summary of my project and how I thought it went **in my Canvas submission**!
