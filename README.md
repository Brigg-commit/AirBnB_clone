# AirBnB clone project -The Console

The console is the first segment of the AirBnB project at Holberton School that will collectively cover fundamental concepts of higher level programming. The goal of AirBnB project is to eventually deploy our server a simple copy of the AirBnB Website(HBnB). A command interpreter is created in this segment to manage objects for the AirBnB(HBnB) website.

# Description of this command interpreter:

<ul>
<li> Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc...</li>
<li>Do operations on objects (count, compute stats, etc...)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>

# Table of Content
<li>Environment</li>
<li>Installation</li>
<li>File Descriptions</li>
<li>Usage</li>
<li>Samples of use
<li>Bugs</li></li>
<li>Authors</li>
<li>License</li>

# Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

# Installation

<li>Clone this repository: git clone "https://github.com/MIC11A3L/AirBnB_clone.git"</li>
<li>Access AirBnb directory: cd AirBnB_clone</li>
<li>Run hbnb(interactively): ./console and enter command</li>

<li>Run hbnb(non-interactively): echo "<command>" | ./console.py</li>
</ul>


# File Descriptions
<a href ="">console.py </a>- the console contains the entry point of the command interpreter. List of commands this console current supports:

EOF - exits console

quit - exits console

<emptyline> - overwrites default emptyline method and does nothing

create - Creates a new instance ofBaseModel, saves it (to the JSON file) and prints the id

destroy - Deletes an instance based on the class name and id (save the change into the JSON file).

show - Prints the string representation of an instance based on the class name and id.

all - Prints all string representation of all instances based or not on the class name.

update - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

# models/ directory contains classes used for this project:
<a href ="">base_model.py</a> - The BaseModel class from which future classes will be derived.

def __init__(self, *args, **kwargs) - Initialization of the base model

def __str__(self) - String representation of the BaseModel class

def save(self) - Updates the attribute updated_at with the current datetime

def to_dict(self) - returns a dictionary containing all keys/values of the instance

Classes inherited from Base  Model:
<ul>
<li>user.py</li>
<li>state.py</li>
<li>city.py</li>
<li>place.py</li>
</ul>

# Examples of use
vagrantAirBnB_clone$./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) all BaseModel
[[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}]
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
[BaseModel] (7da56403-cc45-4f1c-ad32-bfafeb2bb050) {'updated_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772167), 'id': '7da56403-cc45-4f1c-ad32-bfafeb2bb050', 'created_at': datetime.datetime(2017, 9, 28, 9, 50, 46, 772123)}
(hbnb) destroy BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
(hbnb) show BaseModel 7da56403-cc45-4f1c-ad32-bfafeb2bb050
** no instance found **
(hbnb) quit

# Bugs
No known bugs at this time.

# Authors
Brigg-commit - <Github>

# License
Public Domain. No copy write  protection
