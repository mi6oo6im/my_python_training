from collections import defaultdict


def user_is_available(force_dict: dict, force_user: str):
    for user in force_dict.values():
        if force_user in user:
            return True
    return False


def remove_user(force_dict: dict, force_user: str):
    for k, v in force_dict.items():
        if force_user in v:
            v.remove(force_user)


def force_user_join(force_dict: dict, force_side: str, force_user: str):
    if not user_is_available(force_dict, force_user):
        force_dict[force_side].append(force_user)
    return force_dict


def force_user_switch(force_dict: dict, force_side: str, force_user: str):
    if user_is_available(force_dict, force_user):
        remove_user(force_dict, force_user)
    force_dict[force_side].append(force_user)
    print(f'{force_user} joins the {force_side} side!')
    return force_dict


def get_force_book_data(force_dict: dict):
    res = '\n'.join([f'Side: {k}, Members: {len(v)}\n' + '\n'.join([f'! {force_user}' for force_user in v]) for k, v in
                     force_dict.items() if len(v) > 0])
    return res


force_side_dict = defaultdict(list)
command_line = input()
while command_line != 'Lumpawaroo':
    if '|' in command_line:
        force_side_name, username = command_line.split(' | ')
        force_side_dict = force_user_join(force_side_dict, force_side_name, username)
    elif '->' in command_line:
        username, force_side_name = command_line.split(' -> ')
        force_side_dict = force_user_switch(force_side_dict, force_side_name, username)
    command_line = input()

print(get_force_book_data(force_side_dict))
