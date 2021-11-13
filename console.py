#!/usr/bin/python3

import cmd
import json
from models.base_model import BaseModel
from models import storage

lists = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
        intro = 'Welcome to the Python Console.   Type help or ? to list commands.\n'
        prompt = '(hbnb)'

        # ----- basic commands -----
        def do_test(self, arg):
                print("Hola soy un test")

        def do_quit(self, arg):
                return True

        def do_EOF(self, arg):
                return True
        
        def do_create(self, arg):
                """
                
                """
                if not arg:
                        print("** class name missing **")
                elif arg not in lists:
                        print("** class doesn't exist **")
                else:
                        my_model = BaseModel()
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
                        if args[0] not in lists:
                                print("** class doesn't exist **")
                        elif args[0] in lists and len(args) != 2:
                                print("** instance id missing **")
                        else:
                                for key, value in storage.all().items():
                                        if args[1] == value.id:
                                                print(value)
                                                return
                                        else:
                                                print("** no instance found **")

if __name__ == '__main__':
        HBNBCommand().cmdloop()
