import cmd, sys

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


if __name__ == '__main__':
        HBNBCommand().cmdloop()
