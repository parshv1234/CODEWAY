## To-Do List Management System

### Overview
The To-Do List Management System is a Python script that enables users to manage tasks interactively through a command-line interface. The script uses a MySQL database to store task-related information, and users can perform various actions such as adding tasks, viewing tasks, marking tasks as completed, updating task details, and deleting tasks.

### Features
1. **Database Integration:** The script uses MySQL to store and manage task data. It establishes a connection to a MySQL database (in this case, a database named "todolist").

2. **Task Operations:**
   - **Add Task:** Users can add a new task to the to-do list, providing a task name and description.
   - **View Tasks:** Users can view all tasks in the database, including their status (completed or not completed).
   - **Mark Task as Completed:** Users can mark a task as completed, changing its status to "completed."
   - **Update Task Details:** Users can update the name and description of a task.
   - **Delete Task:** Users can delete a task from the to-do list.

3. **Interactive User Interface:** The script provides a simple command-line interface with a menu-driven system for users to interact with the to-do list.

4. **Database Initialization:** The script includes a function to initialize the database, resetting the task ID auto-increment counter.

### Integrated Libraries and APIs
- **MySQL Connector:** Utilized for connecting to and interacting with a MySQL database.
- **Python `datetime` Module:** Used to capture the current date and time for logging purposes.

### IDE and API
- **IDE:** The code is designed to be run in a Python-friendly Integrated Development Environment (IDE), such as Visual Studio Code, PyCharm, or Jupyter Notebook.

- **APIs:** The script uses the MySQL Connector library to interact with the MySQL database.

### How to Use
1. **MySQL Database Setup:**
   - Ensure you have a MySQL server running and create a database named "todolist."
   - Update the script with your MySQL server credentials (host, user, password).

2. **Run the Script:**
   - Execute the script by running the `todo_list.py` file in a Python environment.

3. **Interact with the To-Do List:**
   - Follow the on-screen prompts to add, view, mark as completed, update, or delete tasks.
   - Choose the "Exit" option to end the program.

### License
This script is open-source and available under the [MIT License](LICENSE.md).

Feel free to contribute, report issues, or suggest improvements!
