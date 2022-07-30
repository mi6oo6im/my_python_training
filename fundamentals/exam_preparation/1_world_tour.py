def add_stop_func(_route: str, _index: int, _stop: str):
    if 0 <= _index < len(_route):
        route_list = list(_route)
        route_list.insert(_index, _stop)
        _route = ''.join(route_list)
    return _route


def remove_stop_func(_route: str, _start_index: int, _end_index: int):
    if _start_index >= 0 and _end_index < len(_route):
        string_to_remove = _route[_start_index:_end_index + 1]
        _route = _route.replace(string_to_remove, '')
    return _route


def switch_func(_route: str, _old_stop: str, _new_stop: str):
    if _old_stop in _route:
        _route = _route.replace(_old_stop, _new_stop)
    return _route


destinations_string = input()

command_line = input()
while command_line != 'Travel':
    if 'Add Stop' in command_line:
        command, index, new_stop = command_line.split(':')
        destinations_string = add_stop_func(destinations_string, int(index), new_stop)
    elif 'Remove Stop' in command_line:
        command, start_index, end_index = command_line.split(':')
        destinations_string = remove_stop_func(destinations_string, int(start_index), int(end_index))
    elif 'Switch' in command_line:
        command, old_stop, new_stop = command_line.split(':')
        destinations_string = switch_func(destinations_string, old_stop, new_stop)
    print(destinations_string)
    command_line = input()
print(f'Ready for world tour! Planned stops: {destinations_string}')
