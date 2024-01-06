import os
FILEPATH = "ToDo.txt"


def get_todos(filepath=FILEPATH):
    if not os.path.exists("ToDo.txt"):
        with open("ToDo.txt", "w") as file:
            pass
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello from functions!")
    print(get_todos())