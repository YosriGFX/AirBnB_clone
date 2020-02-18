#!/usr/bin/python3
'''console file'''
import cmd
from models import *


class HBNBCommand(cmd.Cmd):
    '''Class HBNB Command'''
    prompt = "(hbnb) "
    class_dic = [
                    "BaseModel",
    ]

    def emptyline(self):
        '''emptyline'''
        pass

    def do_quit(self, line):
        '''quit'''
        return True

    def do_EOF(self, line):
        '''EOF'''
        return True

    def do_create(self, line):
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

    def do_show(self, line):
        '''show instances'''
        try:
            if line:
                arg_line = line.split(" ")
                ClassName = arg_line[0]
                if ClassName in self.class_dic:
                    if len(arg_line) > 1:
                        current_id = arg_line[1]
                        all_objs = storage.all()
                        full_id = "{}.{}".format(ClassName, current_id)
                        if full_id in all_objs:
                            print(all_objs[full_id])
                        else:
                            raise KeyError
                    else:
                        raise IndexError
                else:
                    raise NameError
            else:
                raise SyntaxError
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        '''show instances'''
        try:
            if line:
                arg_line = line.split(" ")
                ClassName = arg_line[0]
                if ClassName in self.class_dic:
                    if len(arg_line) > 1:
                        current_id = arg_line[1]
                        all_objs = storage.all()
                        full_id = "{}.{}".format(ClassName, current_id)
                        if full_id in all_objs:
                            del all_objs[full_id]
                            storage.save()
                        else:
                            raise KeyError
                    else:
                        raise IndexError
                else:
                    raise NameError
            else:
                raise SyntaxError
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def help_quit(self):
        '''HELP_quit'''
        print("Quit command to exit the program\n")

    def help_EOF(self):
        '''HELP_EOF'''
        print("Ctrl+D command to exit the program\n")

    def help_create(self):
        print(
                "Create Command to create a new instance of <Model_name>\
                \nExample:\
                \n> create <Model_name>\
                \n"
        )

    def help_show(self):
        print(
                "Show Command to prints the string representation of an\
                \ninstance based on the <Model_name> and <id>\
                \nExample:\
                \n> show <Model_name> <id>\
                \n"
        )

    def help_destroy(self):
        print(
                "destroy Command to deletes an instance and save changes\
                \nbased on the <Model_name> and <id>\
                \nExample:\
                \n> destroy <Model_name> <id>\
                \n"
        )

if __name__ == '__main__':
    HBNBCommand().cmdloop()
