#!/usr/bin/python3
"""The AIRBnB console"""


import cmd
import sys
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity

classes = {
        "User": User, "BaseModel": BaseModel,
        "place": Place, "City": City, "State": State,
        "Amenity": Amenity, "Review": Review
        }


class HBNBCommand(cmd.Cmd):
    """The console"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """does nothing"""
        pass

    def do_create(self, arg):
        """creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """shows an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif not args[0].strip() in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0].strip(), args[1].strip())
            obj = models.storage.all()
            if obj_key in storage.all():
                print(obj[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0].strip(), args[1].strip())
            if obj_key in models.storage.all():
                del models.storage.all()[obj_key]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """prints all string representations of instances"""
        args = arg.split()
        obj_list = []
        if not arg:
            for obj in storage.all().values():
                obj_list.append(str(obj))
            print(obj_list)
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for obj in storage.all().values():
                if type(obj).__name__ == args[0]:
                    obj_list.append(str(obj))
            print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            obj_key = "{}.{}".format(args[0].strip(), args[1].strip())
            if obj_key in storage.all():
                models.storage.all()[obj_key].__dict__[args[2]] = args[3]
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
