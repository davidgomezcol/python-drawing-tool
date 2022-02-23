def validate_file_name(input_str):
    """Validates that the filename is correct"""

    ext = input_str.split('.')
    if '.' in input_str and len(ext[-1]) == 3 and len(input_str) >= 5:
        return True
    elif '.' in input_str and len(ext[-1]) >= 3:
        print('Enter filename in correct format. ie. "input.txt"')
        return False
    elif '.' in input_str and len(ext[-1]) < 3:
        print('Wrong extension "{}". ie "input.txt"'.format(ext[-1]))
        return False
    elif '.' not in input_str or input_str == "":
        print('File name or extension missing. ie. "input.txt"')
        return False


def validate_input_command(input_val):
    """Validates that the Command line includes
    numbers"""
    val = [input_val[0]]

    if input_val[0].upper() == 'B':
        for i in input_val[1:-1]:
            try:
                val.append(int(i))
            except ValueError:
                print('Parameters must be numeric')
                return []
        val.append(input_val[-1])
    else:
        for i in input_val[1:]:
            try:
                val.append(int(i))
            except ValueError:
                print('Parameters must be numeric')
                return []
    return val


def validate_command_string(input_str):
    """Validates that the command line includes the
    type of the geometry object"""
    val = input_str.split()

    if not val or (len(val[0]) > 1) or (not val[0].isalpha()):
        print('Wrong type format. Command must start with Type')
        return False

    return True


def validate_input_args(input_args):
    """Validates number of input values depending
        of the command type"""
    c_type = input_args[0].upper()

    if c_type == 'Q':
        num_args = 0
    elif c_type == 'C':
        num_args = 2
    elif c_type == 'L':
        num_args = 4
    elif c_type == 'R':
        num_args = 4
    elif c_type == 'B':
        num_args = 3
    else:
        print('Wrong geometry type "{}" was given. '
              'Please verify.'.format(c_type))
        return False

    if len(input_args[1:]) != num_args:
        print('Wrong number of arguments for {} command'.format(c_type))
        return False

    return True
