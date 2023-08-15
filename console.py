#!/usr/bin/python3
# console.py
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage
"""The command Interpreter representaion"""

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'Place': Place,
    'City': City,
    'Amenity': Amenity,
    'Review': Review,
    'State': State,
}


class HBNBCommand(cmd.Cmd):
    """command interpreter class"""
    intro = 'Welcome to Command interpreter.    Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    # ----- basic commands -----
    # quit command implementation
    def do_quit(self, args):
        """Quit command to exit the program"""
        print("Exiting the program...")
        return True

    # end of line implementation
    def do_EOF(self, args):
        """To exit the program"""
        print("EOF")
        return True

    # empty line implementation
    def emptyline(self):
        """Empty line + ENTER"""
        return False  # just do nothing

    # create comman implementation
    def do_create(self, name=''):
        """Creates a new instance of BaseModel"""
        if name == '':
            print("** class name missing **")
            return
        elif name not in classes:
            print("** class doesn't exist **")
            return
        # creates an instance of BaseModel
        obj = classes[name]()
        obj.save()
        print(obj.id)

    # show command implementation.
    def do_show(self, args):
        """Prints the String representation of an instance based on the class name and id"""
        # checks if there is a given argument
        if args == '':
            print("** class name missing **")
            return
        # split the given arguments using space.
        commands = args.split()
        # the first is a class name
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
                print(storage.all()[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Delets an instance based on the class name and id"""
        # checks if there is a given argument which is class name and id
        if args == '':
            print("** class name missing **")
            return
        # split the given arguments using space.
        commands = args.split()
        # the first is a class name
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
                del storage.all()[obj_key]  # delets an instance.
                storage.save()
            else:
                print("** no instance found **")

    # all command implementation
    def do_all(self, args):
        """Prints all String representation of all instances based or not on the class name"""
        if args == '':
            # when there is no class name specified
            print([str(value) for key, value in storage.all().items()])
        elif args in classes:
            # for the case when the class name is given
            filtered_objs = []
            for key, value in storage.all().items():
                cl_name = key.split('.')
                if cl_name[0] == args:
                    filtered_objs.append(str(value))
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
            return
        else:
            new_str = f"{commands[0]}.{commands[1]}"
            if new_str not in storage.all().keys():
                print("** no instance found **")
                return
            elif len(commands) < 3:
                print("** attribute name missing **")
                return
            elif len(commands) < 4:
                # by assuming id , created_at and updated_at attributes can't be passed
                print("** value missing **")
                return
            else:
                setattr(storage.all()[new_str], commands[2], commands[3])
                storage.save()

    def do_update2(self, cmd):
        """Updates an instance based on the class name and id by taking the dictionary of attributes and values"""
        print('******************')
        args = cmd.split()
        print(args)
        if args[0] == "":
            print("** class name missing **")
            return

    def do_count(self, args):
        """Returns the count of an instances of a given class"""
        if args == '':
            print("** class name missing **")

        elif args in classes:
            # for the case when the class name is given
            count = 0
            for key, value in storage.all().items():
                cl_name = key.split('.')
                if cl_name[0] == args:
                    count += 1
            print(count)
        else:
            print("** class doesn't exist **")

    def default(self, line):
        if line is None:
            return

        cmdPattern = "^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        paramsPattern = """^"([^"]+)"(?:,\s*(?:"([^"]+)"|(\{[^}]+\}))(?:,\s*(?:("?[^"]+"?)))?)?"""
        m = re.match(cmdPattern, line)
        if not m:
            super().default(line)
            return
        mName, method, params = m.groups()
        m = re.match(paramsPattern, params)
        params = [item for item in m.groups() if item] if m else []

        cmd = " ".join([mName] + params)

        if method == 'all':
            return self.do_all(cmd)

        if method == 'count':
            return self.do_count(cmd)

        if method == 'show':
            return self.do_show(cmd)

        if method == 'destroy':
            return self.do_destroy(cmd)

        if method == 'update':
            return self.do_update(cmd)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
