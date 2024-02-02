# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 13:14:17 2024

@author: Parshv
"""

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shivyog@0614",
    database="todolist"
)

if mydb.is_connected():
    print("Connection successful.................")

def initialize_database():
    try:
        cursor = mydb.cursor()
        sql="ALTER TABLE tasks AUTO_INCREMENT = 1"
        cursor.execute(sql)
            
        mydb.commit()
        cursor.close()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Error during database initialization: {e}")

def add_task(task_name, description):
    cursor = mydb.cursor()
    sql = "INSERT INTO tasks (task_name, description) VALUES (%s, %s)"
    val = (task_name, description)
    cursor.execute(sql, val)
    mydb.commit()
    print("Task added successfully!")

def view_tasks():
    cursor = mydb.cursor()
    sql = "SELECT * FROM tasks"
    cursor.execute(sql)
    tasks = cursor.fetchall()
    if tasks:
        for task in tasks:
            task_id, task_name, description, is_completed = task
            if is_completed:
                print(f"Task ID: {task_id}, Task Name: {task_name}, Description: {description}, Completed: [Striked Out]")
            else:
                print(f"Task ID: {task_id}, Task Name: {task_name}, Description: {description}, Completed: [Not Completed]")
    else:
        print("No tasks in the database")

def mark_completed(task_id):
    cursor = mydb.cursor()
    sql = "UPDATE tasks SET is_completed = 1 WHERE id = %s"
    val = (task_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Task marked as completed!")

def update_task(task_id, task_name, description):
    cursor = mydb.cursor()
    sql = "UPDATE tasks SET task_name = %s, description = %s WHERE id = %s"
    val = (task_name, description, task_id)
    cursor.execute(sql, val)
    mydb.commit()
    print("Task details updated successfully!")

def delete_task(task_id):
    cursor = mydb.cursor()
    sql = "DELETE FROM tasks WHERE id = %s"
    val = (task_id,)
    cursor.execute(sql, val)
    mydb.commit()
    print("Task deleted successfully!")

if __name__ == "__main__":

    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task Details")
        print("5. Delete Task")
        print("6. Exit")
        print("7. Reset")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            task_name = input("Enter the task name: ")
            description = input("Enter the task description: ")
            add_task(task_name, description)

        elif choice == 2:
            print("\n--- Tasks ---")
            view_tasks()

        elif choice == 3:
            cursor = mydb.cursor()
            cursor.execute("SELECT COUNT(*) FROM tasks")
            task_count = cursor.fetchone()[0]
            if task_count > 0:
                task_id = int(input("Enter the task ID to mark as completed: "))
                mark_completed(task_id)
            else:
                print("No tasks available to mark as completed.")

        elif choice == 4:
            cursor = mydb.cursor()
            cursor.execute("SELECT COUNT(*) FROM tasks")
            task_count = cursor.fetchone()[0]
            if task_count > 0:
                task_id = int(input("Enter the task ID to update: "))
                task_name = input("Enter the new task name: ")
                description = input("Enter the new task description: ")
                update_task(task_id, task_name, description)
            else:
                print("No tasks available for update.")

        elif choice == 5:
            cursor = mydb.cursor()
            cursor.execute("SELECT COUNT(*) FROM tasks")
            task_count = cursor.fetchone()[0]
            if task_count > 0:
                task_id = int(input("Enter the task ID to delete: "))
                delete_task(task_id)
            else:
                print("No tasks available for deletion.")

        elif choice == 6:
            print("Goodbye!")
            break
        elif choice == 7:
            initialize_database()

        else:
            print("Invalid choice. Please try again.")
