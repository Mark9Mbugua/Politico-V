# Politico

[![Build Status](https://travis-ci.org/Mark9Mbugua/Politico-V.svg?branch=ch-add-readme-badges-%23163818963)](https://travis-ci.org/Mark9Mbugua/Politico-V)     [![Coverage Status](https://coveralls.io/repos/github/Mark9Mbugua/Politico-V/badge.svg?branch=ch-add-readme-badges-%23163818963)](https://coveralls.io/github/Mark9Mbugua/Politico-V?branch=ch-add-readme-badges-%23163818963) [![Maintainability](https://api.codeclimate.com/v1/badges/7216d146615ad26fc082/maintainability)](https://codeclimate.com/github/Mark9Mbugua/Politico-V/maintainability)

Politico is a platform that enables citizens to give their mandate to politicians running for different government offices
while building trust in the process through transparency.

## Getting Started
Clone the repo from GitHub:
    
    git clone: https://github.com/Mark9Mbugua/Politico-V.git

Navigate to root folder
    `cd Politico-V`

Create a virtual environment
    `virtualenv venv`

Activate the virtual environment from the root folder
    `source ./venv/Scripts/activate`

Install the required packages
    `pip install -r requirements.txt`

## Starting the API

On the terminal type `export FLASK_APP=run.py` and type enter. Run `flask run`

## Use the following endpoints to perform the specified tasks
		 
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

## Built with...

* Python
* Flask

### Credits
Coypright (c) [Mark Mbugua](https://github.com/Mark9Mbugua)