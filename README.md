# To-Do List Application

This repository contains two versions of a command-line To-Do List application implemented in Python. Both versions allow you to manage tasks, but they differ in their features, code structure, and level of enhancement.

## Projects Overview

### 1. Basic To-Do List Application

**Description:**

A fundamental command-line To-Do List application that allows you to add, view, remove, mark as complete, edit, filter, save, and load tasks. This version provides a basic implementation of the core features.

**Key Features:**

*   Add tasks with descriptions, categories, priorities, and due dates.
*   View current tasks.
*   Remove tasks.
*   Mark tasks as completed.
*   View completed tasks.
*   Edit task details.
*   Filter tasks by category.
*   Save tasks to a JSON file.
*   Load tasks from a JSON file.

**How to Run:**

1.  Ensure you have Python 3.x installed.
2.  Install any required libraries (in this case, none besides standard libraries).
3.  Run the application:

    ```
    python To-do-list-App.py
    ```

### 2. Enhanced To-Do List Application

**Description:**

An enhanced version of the To-Do List application with improved code structure, type hints, and detailed docstrings. This version builds upon the basic app by adding features that improve code readability, maintainability, and user experience.

**Key Features:**

*   Includes all features of the basic version.
*   Robust input validation to prevent empty or invalid entries.
*   Detailed docstrings and type hints for better code understanding.
*   Better error handling for file operations and user inputs.
*   Clearer prompts and user feedback.

**How to Run:**

1.  Ensure you have Python 3.x installed.
2.  Install any required libraries (in this case, none besides standard libraries).
3.  Run the application:

    ```
    python To_do_list_enhanced_Application.py
    ```

## Differences Between the Projects

*   **Code Structure:**
    *   `To-do-list-App.py`: A more basic implementation with less emphasis on modularity and type hinting.
    *   `To_do_list_enhanced_Application.py`: A more structured implementation with extensive use of type hints and docstrings for better readability and maintainability.  Includes better input validation and error handling.

*   **Code Style:**
    *   The enhanced version adopts a more modern Python coding style, utilizing type hints and detailed docstrings throughout the code.
    *   The basic version provides a functional application but lacks the advanced code enhancements found in the enhanced version.

*   **User Experience:**
    *   The enhanced version provides more robust input validation and error messages to guide the user.
    *   The basic version has fewer checks and may be less user-friendly in some cases.

## How to Use

Both applications provide a command-line interface with the following menu options:

1.  **Add a task:** Add a new task with details like category, priority, and due date.
2.  **View tasks:** Display the current list of incomplete tasks.
3.  **Remove a task:** Remove a task from the list by its number.
4.  **Mark a task as completed:** Mark a task as completed by its number.
5.  **View completed tasks:** Display the list of completed tasks.
6.  **Edit a task:** Edit the details of a task by its number.
7.  **Filter tasks by category:** Display tasks belonging to a specific category.
8.  **Save tasks:** Save the current list of tasks to a JSON file (`tasks.json`).
9.  **Load tasks:** Load tasks from the JSON file.
10. **Exit:** Exit the application.

Follow the prompts in the application to navigate through the menu options and manage your to-do list.

## Contributing

Contributions, issues, and feature requests are welcome! Please check the [issues page](#) if you wish to contribute.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
