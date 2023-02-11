# HELIX_ASSIGNMENT
This is a Django project for the HELIX_ASSIGNMENT. The project contains an app called backend which provides the core functionality for the backend functionality of the website.

Requirements
Before you can run this project, you will need to install the following software:

Python 3.x
Django
Virtualenv (optional, but recommended)

## Setup

1. Clone the repository:
> git clone https://github.com/sikatram/HELIX_ASSIGNMENT.git

2. Change into the HELIX_ASSIGNMENT directory:
> cd HELIX_ASSIGNMENT

3. Create a virtual environment and activate it (optional, but recommended):
> virtualenv venv
> source venv/bin/activate

4. Install the dependencies:
> pip3 install -r requirements.txt

5. Apply the database migrations:
> python3 manage.py migrate

6. Start the development server:
> python3 manage.py runserver

7. Open a web browser and navigate to http://localhost:8000 to see the application running.

## Logging

As requests are processed through the api, the server will notify you with logs in the terminal


