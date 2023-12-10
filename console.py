#!/usr/bin/python3
"""Module for HBNBCommand class"""

import cmd
import re
import models
from models.base_model import BaseModel
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

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

    def do_create(self, arg):
        """Creates a new instances of a class"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            print(storage.all().get(key, "** no instance found **"))
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            objects = storage.all()
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representation of all instances"""
        args = arg.split()
        objects = storage.all()
        if not args or args[0] == "":
            print([str(obj) for obj in objects.values()])
        else:
            try:
                class_name = args[0]
                print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])
            except IndexError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
