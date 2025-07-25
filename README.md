# 📦 **Inventory Management System** (Backend - Django Rest Framework)

This is a **backend application** for managing inventory, built using **Django Rest Framework (DRF)**. It provides **RESTful APIs** for **user authentication** and **product management**.

---

## ✅ **Features Implemented**

- 🔐 **User Authentication** (Registration & Login with **JWT**)
- ➕ **Add New Products**
- 🔄 **Update Product Quantity**
- 📄 **Get List of Products** (with **Pagination**)

---

## 🚀 **Stretch Goals Attempted**

- 🛠️ **Basic Admin Portal**: Utilized Django's built-in **admin interface** for managing data

---

## 🛠️ **Technologies Used**

- **Language/Framework**: Python, Django Rest Framework (DRF)
- **Database**: PostgreSQL
- **Authentication**: Simple JWT (`djangorestframework-simplejwt`)
- **API Documentation**: Swagger (drf-yasg) or DRF Spectacular
- **Other Libraries**:
  - `djangorestframework`
  - `djangorestframework-simplejwt`

---

## 🗃️ **Database Schema**

- **Users Table**: Managed by Django's default `User` model
- **Products Table**:
  - `name`
  - `type`
  - `sku`
  - `image_url`
  - `description`
  - `quantity`
  - `price`

---

## ⚙️ **Setup & Run Project**

Follow the steps below to run the project locally:

### 🔧 **Prerequisites**

- Python 3.8+
- PostgreSQL
- pip (Python package manager)
- Virtualenv (optional but recommended)

---

### 📥 **Installation Steps**

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/inventory-system.git
   cd inventory-system

### 📥 **Installation Steps**

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
### 📥 **Installation Steps**

1.  **Clone the repository**
    ```bash
    git clone https://github.com/<your-username>/<your-repo-name>.git
    cd <your-repo-name>
    ```

2.  **Create and activate virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up your `.env` file**
    Create a `.env` file in the project root and add your configuration:
    ```ini
    SECRET_KEY=your_secret_key
    DEBUG=True
    DATABASE_URL=postgres://username:password@localhost:5432/your_db_name
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=password_of_database
    DB_PORT=port number
    DB_HOST=localhost
    ```

5.  **Apply migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (admin)**
    ```bash
    python manage.py createsuperuser
    ```
    *Follow the prompts to set a username, email, and password.*

7.  **Run the development server**
    ```bash
    python manage.py runserver
    ```
    *The server will start, typically at `http://127.0.0.1:8000/`.*
   


API Endpoints:

Detailed API documentation might be available via a tool like Swagger UI:

POST /api/register/: Register a new user.
<img width="1737" height="831" alt="Screenshot from 2025-07-25 19-32-42" src="https://github.com/user-attachments/assets/b1e02c40-0c21-44b0-b894-58e30c131771" />

GET /api/products/: Retrieve a list of products (paginated, requires authentication).
<img width="1737" height="831" alt="Screenshot from 2025-07-25 19-33-20" src="https://github.com/user-attachments/assets/6da271a1-684c-48f9-a1fd-462c5920d07b" />


POST /api/login/: Authenticate a user and receive a JWT token.
<img width="1737" height="831" alt="Screenshot from 2025-07-25 19-32-54" src="https://github.com/user-attachments/assets/dc4e2481-fa5f-432b-847d-ffd9f6667749" />

POST /api/products/: Add a new product (requires authentication).
<img width="1737" height="831" alt="Screenshot from 2025-07-25 19-34-23" src="https://github.com/user-attachments/assets/6829f12c-3277-4573-a24f-40bdad8a5675" />

PUT /api/products/{id}/quantity/: Update the quantity of an existing product (requires authentication).
<img width="1737" height="831" alt="Screenshot from 2025-07-25 19-51-11" src="https://github.com/user-attachments/assets/edc8b84e-5bba-4565-8afe-d8f2fa5e2d15" />
