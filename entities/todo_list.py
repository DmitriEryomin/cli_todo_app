from services.json_storage import JsonStorage


class TodoList:
    def __init__(self, file: str, auto_save=True):
        self.storage = JsonStorage(f'{file}')
        self.todo_list: list = self.storage.read()
        self.auto_save = auto_save

    def display_list(self):
        print("ToDo List ===================")
        for i in range(len(self.todo_list)):
            item = self.todo_list[i]
            print(f"{i + 1}: {'[x]' if item['done'] else '[ ]'} {item['title']}")
        print("================================\n")

    def add_item(self, title: str):
        self.todo_list.append({"title": title, "done": False})
        if self.auto_save:
            self.storage.write(self.todo_list)

    def set_item_done(self, index: int):
        try:
            self.todo_list[index]["done"] = True
            if self.auto_save:
                self.storage.write(self.todo_list)
        except IndexError:
            print("Item not found!")

    def remove_item(self, index: int):
        try:
            del self.todo_list[index]
            if self.auto_save:
                self.storage.write(self.todo_list)
        except IndexError:
            print("Item not found!")


