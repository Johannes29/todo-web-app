class Tasks:
    def __init__(self):
        self.tasks = []
        self.next_id = 0

    def add_task(self, name: str):
        new_task = {"name": name, "id": self._new_task_id()}
        self.next_id += 1
        self.tasks.append(new_task)
        return new_task["id"]

    def _new_task_id(self):
        return_id = self.next_id
        self.next_id += 1
        return return_id
