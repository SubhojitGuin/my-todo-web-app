# Todo App

This project is a simple to-do list application built using Streamlit, a Python library for creating web applications. The app allows users to add, manage, and complete tasks in a user-friendly interface.

## Features

- Add new tasks to the to-do list.
- Mark tasks as completed.
- Automatically update the list when tasks are completed.
- Store the to-do list in a text file (`todos.txt`).
- Display the list of tasks using checkboxes.

## Web App Implementation

The web app is implemented using Streamlit, a popular Python library for building interactive web applications. The `web.py` script contains the main code for the app. It loads the existing to-do list from the `todos.txt` file and displays it on the web page. Users can add new tasks by entering them in the text input box and pressing Enter. The app also includes checkboxes next to each task to mark them as completed. When a task is marked as completed, it is removed from the list and the `todos.txt` file is updated accordingly.

## File Structure

- `web.py`: This script contains the main application code and handles the Streamlit web app.
- `functions.py`: This script contains helper functions for reading and writing to the `todos.txt` file.

## Requirements

The project requires the following dependencies:

- Streamlit==1.23.1

You can install the required dependencies by running `pip install -r requirements.txt`.

## Usage

To use the to-do app:

1. Clone the repository or download the source code files.
2. Ensure that the `todos.txt` file exists in the same directory as the `web.py` and `functions.py` files.
3. Run the `web.py` script using Python: `streamlit run web.py`.
4. The web app will open in your default web browser.
5. Enter new tasks in the text input box and press Enter to add them to the list.
6. Use the checkboxes to mark tasks as completed. Completed tasks will be automatically removed from the list.
7. The `todos.txt` file will be updated with the latest to-do list.

## Customization

You can customize the app by modifying the code in the `web.py` and `functions.py` files. For example, you can change the layout, styling, or file path for storing the to-do list.

## Contributing

Contributions are welcome! If you have any suggestions, bug fixes, or new features to add, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

- [Streamlit](https://streamlit.io/) - A Python library for building web applications.

Feel free to customize the above template to include specific details about your to-do app, such as installation instructions, additional features, or any other relevant information.