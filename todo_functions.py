import csv

def add_todo(file_name):
    print("Add todo")
    # ask the title of the todo
    todo_name = input("Enter a todo title: ")
    # open file - list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
    # insert - title = user entered
                    #  - completed = False
        writer.writerow([todo_name, "False"])


def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print("Mark todo")

def view_todo(file_name):
    print("View todo")

