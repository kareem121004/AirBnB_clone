#!/usr/bin/python3

"""An interactive shell?"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Defines a class which is the entry point command interpreter"""
    intro = "Welcome to the AirBnB clone console! Type 'help' to list commands. \n"
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit the interpreter"""
        return True

    def help_quit(self):
        """help message for quit"""
        print("Quit command to exit the program\n")
        return

    def do_EOF(self, line):
        """Cleanly exits the"""
        print()
        return True

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
