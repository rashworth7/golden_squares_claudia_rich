class TodoList:
    def __init__(self):
        self.task_list = []


    def add(self, todo):
        self.task_list.append(todo)
      
    def incomplete(self):
        incomplete_list = []
        for task in self.task_list:
            if task.is_complete == False:
                incomplete_list.append(task)
        return incomplete_list

    def complete(self):
        complete_list = []
        for task in self.task_list:
            if task.is_complete == True:
                complete_list.append(task)
        return complete_list

    def give_up(self):
        for task in self.task_list:
            task.is_complete = True
        

