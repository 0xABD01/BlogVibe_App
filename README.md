# BlogVibe_App

**BlogVibe_App** is a simple and modern blogging application built with Django. It allows users to create, read, and manage blog posts with a clean and minimalistic design. The app supports user registration, login, and post creation, providing a platform to share ideas and insights.

## Features

- **User Authentication**: Register, log in, and log out functionality.
- **Post Management**: Create, edit, and delete blog posts.
- **Responsive Design**: Designed to be fully responsive across devices.
- **Minimalist UI**: Clean, intuitive, and easy-to-navigate interface.

## Installation

To get started with BlogVibe_App locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/0xABD01/BlogVibe_App.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd BlogVibe_App/myproject
    ```

3. **Create a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On MacOS/Linux:
        ```bash
        source venv/bin/activate
        ```

5. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Set up the database**:
    - Make migrations:
        ```bash
        python manage.py makemigrations
        ```
    - Apply migrations:
        ```bash
        python manage.py migrate
        ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

8. Open your browser and visit `http://127.0.0.1:8000/` to view the app.

## Contributing

We welcome contributions! To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to your forked repository (`git push origin feature-branch`).
6. Open a pull request to merge your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to reach out to me via GitHub or email.

---

Enjoy using **BlogVibe_App** and happy blogging! 😊
