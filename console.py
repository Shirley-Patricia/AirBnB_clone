#!/usr/bin/python3

import cmd, sys
from models import storage
from models.base_model import BaseModel
#from models import BaseModel

lists = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
        intro = 'Welcome to the Python Console.   Type help or ? to list commands.\n'
        prompt = '(hbnb)'

        # ----- basic commands -----
        def do_test(self, arg):
                print("Hola soy un test")

        def do_quit(self, arg):
                """Command to exit the program"""
                return True

        def do_EOF(self, arg):
                """Command to exit the program"""
                return True
        
        def do_create(self, arg):
                """
                
                """
                if not arg:
                        print("** class name missing **")
                elif arg not in lists:
                        print("** class doesn't exist **")
                elif arg in lists:
                        print("** class already exists **")
                else:
                        my_model = BaseModel()
                        my_model.save()
                        print(my_model.id)

        def do_show(self,arg):
                if not arg:
                        print("** class name missing **")
                elif arg not in lists:
                        print("** class doesn't exist **")

        def do_destroy(self, arg):
                if not arg:
                        print("** class name missing **")
                elif arg not in lists:
                        print("** class doesn't exist **")
                else:
                        del BaseModel.id


if __name__ == '__main__':
        HBNBCommand().cmdloop()
