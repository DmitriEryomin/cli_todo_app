from entities.user import User

print("===ToDo console application===\n")


def show_help():
    commands = [
        '"d" for display ToDo list',
        '"c:{item_number}" for complete item. e.g. "c:1"',
        '"a:{item_name}" add item to your ToDo list. e.g. "a:Buy Milk"',
        '"h" show help',
        '"r:{item_number}" for removing item. e.g. "r:2"',
        '"q" for quit program',
    ]
    print('\n')
    for cmd in commands:
        print(cmd)


user_name = input('Enter username: ')

if not user_name:
    raise Exception("Username is not provided")

command = ''
user = User(user_name)
show_help()

while True:
    value = ''
    command = input("Command: ")

    if ':' in command:
        [command, value] = command.split(':')

    if command == 'd':
        user.todo_list.display_list()
        continue

    if command == 'h':
        show_help()
        continue

    if command == 'q':
        break

    # commands with values
    if value == '':
        print("No value provided!")
        continue

    if command == 'r':
        index = int(value) - 1
        user.todo_list.remove_item(index)

    if command == 'a':
        user.todo_list.add_item(value)

    if command == 'c':
        index = int(value) - 1
        user.todo_list.set_item_done(index)
