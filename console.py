#!/usr/bin/python3

import cmd, sys

class HBNBCommand(cmd.Cmd):
        intro = 'Welcome to the Python Console.   Type help or ? to list commands.\n'
        prompt = '(hbnb)'

        # ----- basic commands -----
        def do_test(self, arg):
                'Descripción de un test para python console'
                print("Hola soy un test")

        def do_quit(self, arg):
                return True

        def do_EOF(self, arg):
                return True

        def emptyline(self):
                """No realiza ninguna accion"""
                return False

if __name__ == '__main__':
        HBNBCommand().cmdloop()
