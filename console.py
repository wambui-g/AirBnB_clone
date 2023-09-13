#!/usr/bin/python3
"""The AIRBnB console"""


import cmd


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


if __name__ == "__main__":
    cmd = HBNBCommand().cmdloop()
