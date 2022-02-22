def validate_input_command(input_val):
    """Validates that the Command line includes
    numbers"""
    val = [input_val[0]]

    if input_val[0].upper() == 'B':
        for i in input_val[1:-1]:
            try:
                val.append(int(i))
            except AssertionError:
                print('Parameter must be numeric')
                return []
        val.append(input_val[-1])
    else:
        for i in input_val[1:]:
            try:
                val.append(int(i))
            except AssertionError:
                print('Parameter must be numeric')
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


def validate_input_values(input_val):
    """Validates number of input values depending
        of the command type"""
    c_type = input_val[0].upper()

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
        print('Wrong geometry type was given. Please verify.')
        return False

    if len(input_val[1:]) != num_args:
        print('Wrong number of arguments for {} command').format(c_type)
        return False

    return True
