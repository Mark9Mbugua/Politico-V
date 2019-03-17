# Politico

[![Build Status](https://travis-ci.org/Mark9Mbugua/Politico-V.svg?branch=bg-improve-code-quality-%23164551680)](https://travis-ci.org/Mark9Mbugua/Politico-V)     [![Coverage Status](https://coveralls.io/repos/github/Mark9Mbugua/Politico-V/badge.svg?branch=bg-improve-code-quality-%23164551680)](https://coveralls.io/github/Mark9Mbugua/Politico-V?branch=bg-improve-code-quality-%23164551680) [![Maintainability](https://api.codeclimate.com/v1/badges/7216d146615ad26fc082/maintainability)](https://codeclimate.com/github/Mark9Mbugua/Politico-V/maintainability)

Politico is a platform that enables citizens to give their mandate to politicians running for different government offices
while building trust in the process through transparency.

## Documentation
To view this application's documentation go to:
[Politico Documentation](https://politicov2.docs.apiary.io)

## Hosting Link
To interact with Politico API, kindly visit:
[Politico Heroku Link](https://politico-final.herokuapp.com/)

## Getting Started
Clone the repo from GitHub:
    
    git clone: https://github.com/Mark9Mbugua/Politico-V.git    

Navigate to root folder
    `cd Politico-V`

Create a virtual environment
    `virtualenv venv`

Activate the virtual environment from the root folder
    `source ./venv/Scripts/activate`

Install application dependencies
    `pip install -r requirements.txt`

Install postgreSQL
  `sudo apt-get install postgresql`

Create a user account postgres and switch over to it
  `sudo -u postgres psql`

Create a database
  `create database politico_db`

## Starting the API
On .env:

    export DATABASE_URL ="your DATABASE_URL here"
    
    Connect to database:

        export FLASK_APP="run.py"
        export debug="True"
        export APP_SETTINGS="development"

On the terminal, run `flask run`

#### On Postman and Heroku, use the following endpoints to perform the specified tasks

Use this URL below to test the following endpoints: https://politico-final.herokuapp.com/

		 
| 	Endpoint                                |   Functionality                                |    
| ------------------------------------------|------------------------------------------------|
| POST /api/v1/signup                       | Create a user account                          |   
| POST /api/v1/signin                       | Sign in a user                                 |
| POST /api/v1/parties                      | Create a political party                       |
| GET /api/v1/parties                       | Retrieve all political parties                 | 
| GET /api/v1/parties/<int:id>              | Retrieve a specific political party            |
| PUT /api/v1/parties/<int:id>              | Edit a specific political party                |
| DELETE /api/v1/parties/<int:id>           | Delete a specific political party              |
| POST /api/v1/offices                      | Create a  political office                     |
| GET /api/v1/offices                       | Retrieve all political offices                 |
| GET /api/v1/offices/<int:id>              | Retrieve a specific political office           |                      
| POST api/v2/office/1/register             | Register a user as a political candidate       |
| POST api/v2/vote                          | Vote for a particular political candidate      |
| GET api/v2/office/2/result                | Get election results per office                |

## Application Features

1. Users can sign up and log in
2. Admin (electoral body) can create political parties.
3. Admin (electoral body) can delete a political party.
4. Admin (electoral) body can edit a political party.
5. Admin (electoral body) can create different political offices.
6. Users can view all political parties.
7. Users can view a specific political party.
8. Users can view political offices.
9. Users can view a specific political office.
10. Admin (electoral) body can register a user as a political candidate
11. Users can vote for only one politician per political office.
12. Users can see the results of election.

## Built with...

* Python
* Flask

### Credits
Copyright (c) [Mark Mbugua](https://github.com/Mark9Mbugua)