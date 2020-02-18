#!/usr/bin/python3
'''console file'''
import cmd
from models import *

class HBNBCommand(cmd.Cmd):
    '''Class HBNB Command'''
    prompt = "(hbnb) "

    def emptyline(self):
        '''emptyline'''
        pass

    def do_quit(self, line):
        '''quit'''
        return True

    def do_EOF(self, line):
        '''EOF'''
        return True

    def do_create(self,line):
        '''create new instance'''
        try:
            if line:
                ClassName = line.split(" ")[0]
                new_dict = eval(ClassName+"()")
                new_dict.save()
                print(new_dict.id)
            else:
                raise SyntaxError
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")


    def help_quit(self):
        '''HELP_quit'''
        print("Quit command to exit the program\n")

    def help_EOF(self):
        '''HELP_EOF'''
        print("Ctrl+D command to exit the program\n")

    def help_create(self):
        print("Create Command to create a new instance of <Model_name>\nExample:\n> create <Model_name>\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
