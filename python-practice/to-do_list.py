#!/usr/bin/python3

tasks = []


def add_task(task):
    tasks.append(task)
    print("task added succesfully")


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("task removed")
    else:
        print("task not found")


def show_tasks():
    print(tasks)


def main():
    while True:
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        if choice == "2":
            task = input("Enter task: ")
            remove_task(task)
        if choice == "3":
            show_tasks()


if __name__ == "__main__":
    main()
