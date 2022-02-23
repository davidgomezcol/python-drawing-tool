import os
import sys
from time import sleep
from components.canvas import Canvas
from components.line import Line
from components.rectangle import Rectangle
from components.bucket import Bucket
from helpers.InputCommandValidator import validate_input_args, \
    validate_input_command, validate_command_string, \
    validate_file_name


def app(l_val):
    """Main app that reads input.txt"""

    geometry_obj = None
    geometry_type = l_val[0].upper()

    if geometry_type == 'C':
        Canvas(l_val[1], l_val[2])
    elif geometry_type == 'L':
        geometry_obj = Line(l_val[1], l_val[2], l_val[3], l_val[4])
    elif geometry_type == 'R':
        geometry_obj = Rectangle(l_val[1], l_val[2], l_val[3], l_val[4])
    elif geometry_type == 'B':
        geometry_obj = Bucket(l_val[1], l_val[2], l_val[3])
    elif geometry_type == 'Q':
        return False
    else:
        print(
            'Geometry type "{}" not recognized. '
            'Please verify.'.format(geometry_type)
        )
        return True

    canvas = Canvas.get_instance()
    if not canvas:
        print('Canvas needs to be provided first.')
        return True

    if geometry_obj and geometry_obj.check_geometry_object_constraints():
        canvas.add_to_canvas(geometry_obj)

    canvas.print_to_file()

    return True


if __name__ == '__main__':
    """App initialization"""

    conditional_break = True
    working_dir = os.getcwd()
    term_width = os.get_terminal_size().columns
    os.system('clear')

    print('*** Welcome to the Drawing Tool ***'.center(term_width).upper())
    print('*** If you want to quit press "Q" ***'.center(term_width))

    while conditional_break:
        f_name = input('Enter Filename: ')
        if f_name.upper() == 'Q':
            conditional_break = app(f_name.upper())
            continue

        if not validate_file_name(f_name):
            continue

        try:
            with open(working_dir + "/files/" + f_name, 'r') as fp:
                for line in fp:
                    if not validate_command_string(line):
                        continue

                    l_val = validate_input_command(line.split())
                    if not l_val:
                        continue

                    if not validate_input_args(l_val):
                        continue

                    conditional_break = app(l_val)

                for i in range(4):
                    sys.stdout.write(".")
                    sleep(1)
                    sys.stdout.flush()
                os.system('clear')
        except FileNotFoundError as e:
            print('The file was not found. {}'.format(e))
