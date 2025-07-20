# ALX Travel App (Project 0x00)

This project is a Django-based travel application for listing and booking properties. This version (`alx_travel_app_0x00`) establishes the core database models, serializers for API data representation, and a management command to seed the database with initial sample data.

## Project Structure

- **`listings/models.py`**: Contains the database schema for `Listing`, `Booking`, and `Review`.
- **`listings/serializers.py`**: Contains serializers for the `Listing` and `Booking` models to facilitate API development.
- **`listings/management/commands/seed.py`**: A custom command to populate the database with sample listings.

## Setup and Installation

### Prerequisites
- Python 3.8+
- Django
- Django REST Framework

### Installation Steps
1.  **Clone the project:**
    ```bash
    git clone <your-repo-url> alx_travel_app_0x00
    ```
2.  **Navigate into the project directory:**
    ```bash
    cd alx_travel_app_0x00
    ```
3.  **Install dependencies:**
    *(It is recommended to use a virtual environment)*
    ```bash
    pip install Django djangorestframework
    ```
4.  **Add apps to `settings.py`:**
    Ensure you have `'rest_framework'` and `'listings'` in your `INSTALLED_APPS`.

## Database Management

1.  **Create and Apply Migrations:**
    After defining or modifying the models, you must create and apply migrations to update the database schema.
    ```bash
    python manage.py makemigrations listings
    python manage.py migrate
    ```

2.  **Seed the Database:**
    To populate the database with initial sample data (including a sample owner and several property listings), run the custom management command:
    ```bash
    python manage.py seed
    ```
    This command is safe to run multiple times; it will clear old data before adding new entries to prevent duplicates.

## How to Run
1.  Follow the setup and database management steps above.
2.  Create a superuser to access the Django admin panel:
    ```bash
    python manage.py createsuperuser
    ```
3.  Start the development server:
    ```bash
    python manage.py runserver
    ```
4.  Navigate to `http://127.0.0.1:8000/admin/` to view the seeded data in the Django admin interface.
