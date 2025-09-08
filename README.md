# Bookmarks API - Flask Edition
=============================

A robust RESTful API built with Flask and Python for managing user bookmarks. This project features user authentication with JWT, secure password handling, and complete CRUD (Create, Read, Update, Delete) functionality for bookmarks, all documented with Swagger UI.

✨ Features
----------

-   **JWT Authentication**: Secure user registration and login using Flask-JWT-Extended.

-   **Password Hashing**: Utilizes `passlib` with `scrypt` for state-of-the-art password security.

-   **CRUD for Bookmarks**: Full functionality to create, retrieve, update, and delete personal bookmarks.

-   **Database Integration**: Uses Flask-SQLAlchemy for seamless interaction with a SQLite database.

-   **API Documentation**: Integrated Swagger UI with Flasgger for interactive API testing and documentation.

-   **Pagination**: Paginated responses for retrieving lists of bookmarks.

-   **URL Validation**: Ensures that submitted bookmarks are valid URLs.

* * * * *

🚀 Getting Started
------------------

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### **Prerequisites**

-   Python 3.9+

-   `pip` package manager

* * * * *

### **Installation**

1.  **Clone the repository:**

    Bash

    ```
    git clone https://github.com/yadavankush2404/Flask_API.git
    cd Flask_API

    ```

2.  **Create and activate a virtual environment:**

    -   **On macOS/Linux:**

        Bash

        ```
        python3 -m venv env
        source env/bin/activate

        ```

    -   **On Windows:**

        Bash

        ```
        python -m venv env
        .\env\Scripts\activate

        ```

3.  **Install the required dependencies:**

    Bash

    ```
    pip install -r requirements.txt

    ```

4.  **Set up environment variables:** Create a file named `.env` in the root directory and add the following variables.

    Ini, TOML

    ```
    # .env
    FLASK_APP=src
    FLASK_ENV=development

    # Use a long, random string for the JWT secret key
    JWT_SECRET_KEY=your-super-secret-and-long-random-string

    # Database URI
    SQLALCHEMY_DATABASE_URI=sqlite:///bookmarks.db

    ```

5.  **Initialize the database:** Open a Python shell in your activated environment and create the database tables.

    Bash

    ```
    flask shell

    ```

    Then, inside the shell:

    Python

    ```
    >>> from src.database import db
    >>> db.create_all()
    >>> exit()

    ```

* * * * *

### **Running the Application**

Start the Flask development server with the following command:

Bash

```
flask run

```

The API will be available at `http://127.0.0.1:5000`.

* * * * *

📖 API Documentation
--------------------

Once the application is running, you can access the interactive Swagger UI documentation in your browser at:

**`http://127.0.0.1:5000/apidocs`**

This interface allows you to view all available endpoints and test them directly.

* * * * *

Endpoints
---------

All endpoints are prefixed with `/api/v1`.

| Method | Endpoint | Description | Auth Required |
| --- | --- | --- | --- |
| `POST` | `/auth/register` | Registers a new user. | No |
| `POST` | `/auth/login` | Logs in a user and returns a JWT. | No |
| `GET` | `/bookmarks` | Gets a paginated list of bookmarks. | **Yes** |
| `POST` | `/bookmarks` | Creates a new bookmark. | **Yes** |
| `GET` | `/bookmarks/<id>` | Retrieves a single bookmark by ID. | **Yes** |
| `PUT` | `/bookmarks/<id>` | Updates a bookmark by ID. | **Yes** |
| `DELETE` | `/bookmarks/<id>` | Deletes a bookmark by ID. | **Yes** |
| `GET` | `/bookmarks/stats` | Gets visit statistics for bookmarks. | **Yes** |

Export to Sheets

* * * * *

📜 License
----------

This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.