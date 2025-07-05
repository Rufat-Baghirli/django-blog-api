Django Blog REST API
This is a backend API for a fully-featured blog platform, built with Django and Django REST Framework. This project is designed to showcase the core principles of a professional web application, including authentication, permissions, and a clean code architecture.

Key Features
Full CRUD Operations for Posts: Complete functionality to Create, Read, Update, and Delete blog posts.

Secure Authentication: User authentication and authorization handled with JWT (JSON Web Tokens).

Custom Permissions: Custom permission classes ensure that only the author of a post can edit or delete it.

Automatic Unique Slugs: Unique, human-readable slugs are automatically generated from the post title, with logic to prevent duplicates.

Clean Architecture: A logical separation of concerns with distinct modules for models, views, serializers, and URLs.

Technology Stack
Backend: Python, Django, Django REST Framework

Authentication: DRF Simple JWT (JSON Web Token)

Database: SQLite3 (for development), PostgreSQL (planned for production)

A## API Endpoints

The main API endpoints for this project are listed below:

| Method | Endpoint                  | Description                        | Auth Required?    |
|--------|---------------------------|------------------------------------|-------------------|
| `GET`  | `/posts/`                 | Returns a list of all posts.       | No                |
| `POST` | `/posts/`                 | Creates a new post.                | Yes               |
| `GET`  | `/posts/{slug}/`          | Retrieves a specific post.         | No                |
| `PUT`  | `/posts/{slug}/`          | Fully updates a post.              | Yes (Owner only)  |
| `PATCH`| `/posts/{slug}/`          | Partially updates a post.          | Yes (Owner only)  |
| `DELETE`| `/posts/{slug}/`         | Deletes a post.                    | Yes (Owner only)  |
| `POST` | `/api/token/`             | Obtains a new token pair.          | No                |
| `POST` | `/api/token/refresh/`     | Refreshes an access token.         | No                |

Local Setup and Installation
To run this project on your local machine, follow these steps:

Clone the repository:

Bash

git clone https://github.com/your-username/django-blog-api.git
cd django-blog-api
Create and activate a virtual environment:

Bash

# For Windows:
python -m venv venv
.\venv\Scripts\Activate.ps1

# For macOS/Linux:
python3 -m venv venv
source venv/bin/activate
Install the required packages:

Bash

pip install -r requirements.txt
Apply the database migrations:

Bash

python manage.py migrate
Run the development server:

Bash

python manage.py runserver
The project is now running at http://127.0.0.1:8000/.

License
This project is licensed under the MIT License.