#!/usr/bin/python3
"""AirBnB console"""
import cmd
import sys

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

lists = ["BaseModel", "User", "Amenity", "Place", "City", "Review"]


class HBNBCommand(cmd.Cmd):
<<<<<<< HEAD
    prompt = '(hbnb)'

    # ----- basic commands -----
    def do_test(self, arg):
        'Descripción de un test para python console'
        print("Hola soy un test")
=======
    intro = 'Welcome! Python Console here. Type help or ? to commands.\n'
    prompt = '(hbnb) '
>>>>>>> 03d7783efdb89b964822c34ee58ab75bad8ccea1

    def do_quit(self, arg):
        'Quit command to exit the console'
        return True

    def do_EOF(self, arg):
        'EOF command -shortcut: ctrl + D- to exit the console'
        print("")
        return True

    def emptyline(self):
        """Do not perform any action"""
        return False

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if not arg:
            print("** class name missing **")
        elif arg not in lists:
            print("** class doesn't exist **")
        else:
            my_model = eval(arg + "()")
            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        """
        Prints a string representation of an instance based
        on the class name and id
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            k = f'{args[0]}.{args[1]}'
            if args[0] not in lists:
                print("** class doesn't exist **")
            elif args[0] in lists and len(args) != 2:
                print("** instance id missing **")
            else:
                for key, value in storage.all().items():
                    if key == k:
                        print(value)
                        return
                    else:
                        print("** no instance found **")

    def do_destroy(self, arg):
<<<<<<< HEAD
        """Deletes an instance based on the class name and id
=======

        """
        Deletes an instance based on the class name and id
>>>>>>> 03d7783efdb89b964822c34ee58ab75bad8ccea1
        (save the change into the JSON file)
        """

        if not arg:
            print("** class name missing **")
        else:
            line = arg.split()
            obj = storage.all()
            key = f'{line[0]}.{line[1]}'

            if line[0] not in lists:
                print("** class doesn't exist **")
            elif line[0] in lists and len(line) != 2:
                print("** instance id missing **")
            elif key in obj:
                del obj[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based 
        or not on the class name.
        """

        list_str = []
        line = arg.split()
        if not arg:
            for key,value in storage.all().items():
                list_str.append(value)
            print(list_str)
        elif line[0] not in lists:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                k = key.split(sep='.')
                if line[0] == k[0]:
                    list_str.append(value)
            print(list_str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
