# AirBnB_clone

![](https://github.com/Ele4327/AirBnB_clone/blob/main/resources/Python-Console.jpg)

👋 Hello Devs

Hello and Welcome to our Holberton AirBnB-Clone console project.
In this repository you will find our own python console, developed by software developers in progress.

For those who dont know a console is basically a command line interpreter that takes input from the user i.e one command at a time and interprets it.

To see help file, just type:

> ./help

PD: First, you need to have downloaded and cloned the repository and entered the repository folder, in case you don't know how, you can click here: [Installation:](#installation-and-execution)

# Features

- Write beautiful code that passes the PEP8 checks.
- All your files should end with a new line
- All your files, classes, functions must be tested with unit tests. Unit tests must also pass in non-interactive mode (check non-interactive apart)

## Python Scripts
- will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your files should be exactly #!/usr/bin/python3
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Python Unit Tests
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')

## List of commands enabled:

> create

Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id

> show

Prints the string representation of an instance based on the class name and id

> destroy

Deletes an instance based on the class name and id (save the change into the JSON file)

> all

Prints all string representation of all instances based or not on the class name




Table of Contents
=================

* [AirBnB_clone](#airbnb_clone)
* [Features](#features)
   * [Python Scripts](#python-scripts)
   * [Python Unit Tests](#python-unit-tests)
   * [List of commands enabled:](#list-of-commands-enabled)
* [Table of Contents](#table-of-contents)
   * [Output](#output)
   * [Installation and Execution:](#installation-and-execution)
   * [Tests](#tests)
      * [Contribuitors](#contribuitors)
      * [Languages and Tools:](#languages-and-tools)
            * [Thanks for your attention, feel free to contribute to the project or contact us if you need something](#thanks-for-your-attention-feel-free-to-contribute-to-the-project-or-contact-us-if-you-need-something)
      * [End](#end)
=================

================================================================
## Output

```
./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) help quit
Quit command to exit the program

(hbnb)
(hbnb) create BaseModel
(hbnb) e768e12b-5953-44fe-82b7-b73530190881
(hbnb) all
["[BaseModel] (e768e12b-5953-44fe-82b7-b73530190881) {'updated_at': datetime.datetime(2021, 11, 15, 9, 50, 13, 36778), 'id': 'e768e12b-5953-44fe-82b7-b73530190881', 'created_at': datetime.datetime(2021, 11, 15, 9, 50, 13, 36768)}", "[BaseModel] (72ed1691-ea88-4987-a494-b972ba09184c) {'updated_at': datetime.datetime(2021, 11, 15, 9, 51, 11, 626565), 'id': '72ed1691-ea88-4987-a494-b972ba09184c', 'created_at': datetime.datetime(2021, 11, 15, 9, 51, 11, 626556)}", "[BaseModel] (66a2d9ef-f417-493b-8d68-8a0ae3a75913) {'updated_at': datetime.datetime(2021, 11, 15, 9, 51, 30, 114219), 'id': '66a2d9ef-f417-493b-8d68-8a0ae3a75913', 'created_at': datetime.datetime(2021, 11, 15, 9, 51, 30, 114209)}", "[BaseModel] (66449d4d-f784-4665-9d6a-ca54f9214be3) {'updated_at': datetime.datetime(2021, 11, 15, 9, 52, 1, 802544), 'id': '66449d4d-f784-4665-9d6a-ca54f9214be3', 'created_at': datetime.datetime(2021, 11, 15, 9, 52, 1, 802533)}"]
(hbnb) show BaseModel 66449d4d-f784-4665-9d6a-ca54f9214be3
[BaseModel] (66449d4d-f784-4665-9d6a-ca54f9214be3) {'updated_at': datetime.datetime(2021, 11, 15, 9, 52, 1, 802544), 'id': '66449d4d-f784-4665-9d6a-ca54f9214be3', 'created_at': datetime.datetime(2021, 11, 15, 9, 52, 1, 802533)}
(hbnb)
(hbnb) quit
```


================================================================
## Installation and Execution:

Clone our repository:

- Go on your machine to the desired location and if you have git installed, type:

> git clone (link to this repository)

Once you have done this, go to the folder that is created, and just type:

> ./console.py

And that´s it, u are already using seeing the propmt and using the console

================================================================
## Tests

Your shell should work like this in interactive mode:

```
python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
```

But also in non-interactive mode:

```
echo "python3 -m unittest discover tests" | bash
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
```
<h3 align="left">Contribuitors</h3>
<p align="left">
<a href="" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="" height="30" width="40" />Shirley Carcamo</a>
</p>
<p align="left">
<a href="https://twitter.com/@jarold42885411" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="" height="30" width="40" />Jarold Hakins</a>
</p>
<p align="left">
<a href="https://twitter.com/@ele5438" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="" height="30" width="40" />Sebastian Garzón</a>
</p>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="" target="_blank"> <img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" alt="python" width="40" height="40"/></a> <a href="" target="_blank" margin-left="4px"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/linux/linux-original.svg" alt="linux" width="40" height="40"/> </a> </p>


================================================================
##### Thanks for your attention, feel free to contribute to the project or contact us if you need something

![](https://github.com/Ele4327/printf/blob/main/img/holb_logo.png)

### End
