#!/usr/bin/python3
'''console file'''
import cmd


class HBNBCommand(cmd.Cmd):
    '''Class HBNB Command'''
    prompt = "(hbnb) "

    def emptyline(self):
        '''emptyline'''
        pass

    def do_quit(self, line):
        '''quit'''
        return True

    def help_quit(self):
        '''HELP_quit'''
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        '''EOF'''
        return True

    def help_EOF(self):
        '''HELP_EOF'''
        print("CTRL+D command to exit the program\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
