#!/usr/bin/python3
#console.py
import cmd
from models.base_model import BaseModel
from models import storage

classes = {
    'BaseModel': BaseModel
}

class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    prompt = "(hbnb) "
    def do_quit(self, args):
        """Quit command to exit the program"""
        print("Exiting the program...")
        return True
    
    def do_EOF(self, args):
        """To exit the program"""
        print("EOF")
        return True

    def emptyline(self):
        """Empty line + ENTER"""
        pass #just do nothing

    def do_create(self, name=''):
        """Creates a new instance of BaseModel"""
        if name=='':
            print("** class name missing **")
            return
        elif name != 'BaseModel':
            print("** class doesn't exist **")
            return
        #creates an instance of BaseModel
        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        #checks if there is a given argument
        if args == '':
            print("** class name missing **")
            return
        #split the given arguments using space.
        commands = args.split()
        #the first is a class name
        if commands[0] != 'BaseModel':
            print("** class doesn't exist **")
            return
        elif len(commands)<2:
            print("** instance id missing **")
            return
        else:
            # handls the case when there is given a class name and id
            obj_key = '{}.{}'.format(commands[0], commands[1])
            if storage.all().keys().__contains__(obj_key):
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")
        
    def do_destroy(self, args):
        """Delets an instance based on the class name and id"""
        #checks if there is a given argument which is class name and id
        if args == '':
            print("** class name missing **")
            return
        #split the given arguments using space.
        commands = args.split()
        #the first is a class name
        if commands[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(commands) < 2:
            print("** instance id missing **")
            return
        else:
            # handls the case when there is given a class name and id
            obj_key = '{}.{}'.format(commands[0], commands[1])
            if storage.all().keys().__contains__(obj_key):
                del storage.all()[obj_key] #delets an instance.
                storage.save()
            else:
                print("** no instance found **")

        # all command implementation
    def do_all(self, args):
        """Prints all String representation of all instances based or not on the class name"""
        if args == '':
            # when there is no class name specified
            print([str(value) for key, value in storage.all().items()])
        elif args  in classes:
            #for the case when the class name is given
            #todo filter...
            filtered_objs = []
            for key, value in storage.all().items():
                cl_name = key.split('.')
                if cl_name[0] == args:
                    filtered_objs.append(value)
            print(filtered_objs)
        else:
            print("** class doesn't exist **")
    
    def do_update(self, args):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if args == "":
            print("** class name missing **")
            return
        commands = args.split()
        if commands[0] not in classes:
            print("** class doesn't exist **")
            return
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            obj_key = '{}.{}'.format(commands[0], commands[1])
            if storage.all().keys().__contains__(obj_key):
                del storage.all()[obj_key] #delets an instance.
                storage.save()
            else:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()