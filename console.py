#!/usr/bin/python3
"""The AIRBnB console"""


import cmd
import sys
from models.engine.file_storage import storage
from models.base_model import BaseModel


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
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """shows an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in storage.all():
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
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
        elif args[0] not in storage.classes:
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
        elif args[0] not in storage.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in storage.all():
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = storage.all()[obj_key]
                attr_name = args[2]
                attr_value = args[3]
                if hasattr(obj, attr_name):
                    try:
                        attr_value = eval(attr_value)
                    except ValueError:
                        pass
                    setattr(obj, attr_name, attr_value)
                    obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
