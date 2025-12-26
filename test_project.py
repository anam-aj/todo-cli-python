from project import Task, ToDoList, menu, fetch_list, open_list, save_list


# Sample Tasks for Testing
task1 = Task("Buy Pen")
task2 = Task("Car Wash")

# Sample List for Testing
list1 = ToDoList()
list1.add_task(task1)
list1.add_task(task2)


def test_Task():
    assert task1.detail == "Buy Pen"
    assert task1.status == "Incomplete"
    assert task2.detail == "Car Wash"
    assert task2.status == "Incomplete"


def test_ToDolist():
    assert list1.task_list[0] == task1
    assert list1.task_list[1] == task2


def test_menu(capsys):
    menu()
    captured = capsys.readouterr()
    assert "Select the option number from below" in captured.out
    assert "1: View Tasks" in captured.out
    assert "5: Save list and Exit program" in captured.out


def test_fetch_list():
    task_list = fetch_list(list1)

    # Test 1st 'task_object'
    assert task_list[0][0] == 1
    assert task_list[0][1] == "Buy Pen"
    assert task_list[0][2] == "Incomplete"

    # Test 2nd 'task_object'
    assert task_list[1][0] == 2
    assert task_list[1][1] == "Car Wash"
    assert task_list[1][2] == "Incomplete"


def test_open_list():
    save_list(list1)
    result = open_list()
    assert isinstance(result, ToDoList)
