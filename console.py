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
    """Defines a class which is the entry point command interpreter"""
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
                filtered_objects = [
                    str(obj)
                    for key, obj in objects.items()
                    if key.startswith(class_name)
                ]
                print(filtered_objects)
            except IndexError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args or args[0] == "":
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            objects = storage.all()
            if key not in objects:
                print("** no instance found **")
                return
            instance = objects[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attr_value = args[3]
            try:
                attr_value = eval(attr_value)
            except:
                pass
            setattr(instance, attr_name, attr_value)
            instance.save()
        except IndexError:
            if len(args) == 1:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
