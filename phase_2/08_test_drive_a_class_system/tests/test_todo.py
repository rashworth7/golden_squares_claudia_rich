from lib.todo import *

def test_mark_complete():
    todo = Todo("wash the floor")
    todo.mark_complete()
    assert todo.is_complete == True