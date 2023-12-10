#!/usr/bin/python3
"""Module for HBNBCommand class"""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    prompt = '(hbnb)  '

    def do_EOF(self, line):
        """Exits console"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        print("Good Bye!")
        return True

    def help_quit(self):
        """when two arguments involve"""
        print('\n'.join(["Quit command to exit the program"]))

    def emptyline(self):
        """ overwriting the emptyline method """
        return False
if __name__ == '__main__':
    HBNBCommand().cmdloop()
