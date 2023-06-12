from lib.todo_list import *
from lib.todo import *

# test: add two items to list
def test_add_items_returns_list():
    todo_list = TodoList()
    task1 = Todo("take the bins out")
    task2 = Todo("water the plants")
    todo_list.add(task1)
    todo_list.add(task2)
    result = todo_list.task_list
    assert result == [task1, task2]

def test_incomplete():
    todo_list = TodoList()
    task1 = Todo("take the bins out")
    task2 = Todo("water the plants")
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    result = todo_list.incomplete()
    assert result == [task2]

def test_complete():
    todo_list = TodoList()
    task1 = Todo("take the bins out")
    task2 = Todo("water the plants")
    todo_list.add(task1)
    todo_list.add(task2)
    task1.mark_complete()
    result = todo_list.complete()
    assert result == [task1]


def test_complete():
    todo_list = TodoList()
    task1 = Todo("take the bins out")
    task2 = Todo("water the plants")
    todo_list.add(task1)
    todo_list.add(task2)
    todo_list.give_up()
    result = todo_list.complete()
    assert result == [task1, task2]