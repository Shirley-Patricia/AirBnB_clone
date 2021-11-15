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
    prompt = '(hbnb) '

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
        """Prints a string representation of an instance based
        on the class name and id
        """
        k = ""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            if len(args) > 1:
                k = f'{args[0]}.{args[1]}'
            if args[0] not in lists:
                print("** class doesn't exist **")
            elif args[0] in lists and len(args) < 2:
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
        k = ""
        if not arg:
            print("** class name missing **")
        else:
            line = arg.split()
            obj = storage.all()
            if len(line) > 1:
                k = f'{line[0]}.{line[1]}'
            if line[0] not in lists:
                print("** class doesn't exist **")
            elif line[0] in lists and len(line) < 2:
                print("** instance id missing **")
            elif k in obj:
                del obj[k]
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
            for key, value in storage.all().items():
                list_str.append(value.__str__())
            print(list_str)
        elif line[0] not in lists:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                k = key.split(sep='.')
                if line[0] == k[0]:
                    list_str.append(value.__str__())
            print(list_str)

    def do_update(self, arg):
        """
        Updates an instance based on the class
        name and id by adding or updating attribute
        """
        l_args = arg.split()
        if len(l_args) < 1:
            print("** class name missing **")
            return False
        if l_args[0] in lists:
            if len(l_args) > 1:
                k = l_args[0] + "." + l_args[1]
                if k in storage.all():
                    if len(l_args) > 2:
                        if len(l_args) > 3:
                            setattr(storage.all()[k], l_args[2], l_args[3])
                            storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
