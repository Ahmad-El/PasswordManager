# PasswordManager
This Python project is a Password Manager with a graphical user interface (GUI) created using Tkinter. It allows users to generate passwords, save passwords along with corresponding logins, search for passwords based on login, and copy passwords if they exist. Passwords are saved to a JSON file for persistent storage.

## Features

- GUI implemented with Tkinter for easy interaction.
- Password generation feature for creating strong passwords.
- Save passwords with corresponding logins.
- Search for passwords based on login.
- Copy passwords to clipboard if they exist.
- Passwords are securely saved to a JSON file for persistent storage.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- JSON module (usually comes built-in with Python)

## Installation

1. **Clone the repository:**

    ```
    https://github.com/Ahmad-El/PasswordManager.git
    ```

2. **Navigate to the project directory:**

    ```
    cd PasswordManager/src
    ```
3. **Install requirements**

4. **Run the application:**

    ```
    python main.py
    ```

## Usage

- Launch the application by running `main.py`.
- Use the GUI to generate, save, search, and copy passwords as needed.
- Passwords are saved to `data.json` in the project directory.

## Project Structure
```
password-manager/
│
├── main.py # Main Python script containing the GUI implementation
├── password_generator.py # Password generator script 
├── data.json # JSON file to store passwords
└── README.md # Project documentation
```