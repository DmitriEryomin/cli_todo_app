from entities.todo_list import TodoList


class User:
    def __init__(self, user_name: str):
        self.user_name = user_name
        self.todo_list = TodoList(f'{user_name}_todo')
