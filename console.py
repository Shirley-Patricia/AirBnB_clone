#!/usr/bin/python3

import cmd
import sys

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

lists = ["BaseModel"]


class HBNBCommand(cmd.Cmd):
    intro = 'Welcome! Python Console here. Type help or ? to commands.\n'
    prompt = '(hbnb)'

    # ----- basic commands -----
    def do_test(self, arg):
        'Descripción de un test para python console'
        print("Hola soy un test")

    def do_quit(self, arg):
        'Command to exit the console'
        return True

    def do_EOF(self, arg):
        'Command -shortcut: ctrl + D- to exit the console'
        return True

    def emptyline(self):
        """No realiza ninguna accion"""
        return False

    def do_create(self, arg):
        """

        """
        if not arg:
            print("** class name missing **")
        elif arg not in lists:
            print("** class doesn't exist **")
        # elif arg in lists:
        #         print("** class already exists **")
        else:
            my_model = eval(arg + "()")
            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        """Prints a string representation
        of an instance based on the class
        name and id
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

        """Deletes an instance based on the class name and id
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
