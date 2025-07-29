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


## Docker Setup for Inventory Management Tool

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed  
- [Docker Compose](https://docs.docker.com/compose/install/) installed  
- [Make](https://www.gnu.org/software/make/) installed (optional but recommended)  
- Basic familiarity with Docker and Docker Compose commands  

---

### Building and Running the Application

1. **Clone the repository** (if you haven't already):  
   ```bash
   git clone https://github.com/your-username/inventory-management-tool.git
   cd inventory-management-tool
   ```

2. **Build and start the containers (Makefile shortcut):**  
   ```bash
   make start
   ```
   or using Docker directly:  
   ```bash
   docker-compose up --build
   ```

3. **Run database migrations:**  
   ```bash
   make migrate
   ```
   or:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a superuser:**  
   ```bash
   make superuser
   ```
   or:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. **Access the application:**  
   - **Django App:** [http://localhost:8000](http://localhost:8000)  
   - **Admin Panel:** [http://localhost:8000/admin](http://localhost:8000/admin)  

6. **Stop the containers:**  
   ```bash
   make stop
   ```
   or:
   ```bash
   docker-compose down
   ```

---

### Makefile Example (Optional but Recommended)

Create a file named **`Makefile`** in your project root with this content:  
```makefile
start:
	docker-compose up --build

stop:
	docker-compose down

migrate:
	docker-compose exec web python manage.py migrate

superuser:
	docker-compose exec web python manage.py createsuperuser

shell:
	docker-compose exec web python manage.py shell

logs:
	docker-compose logs -f
```

---

### Docker Compose Overview

- **Services:**
  - **web** → Django application (Python 3.11 slim image)  
  - **db** → PostgreSQL database (Postgres 15)  

- **Volumes:**
  - **postgres_data** → Persists PostgreSQL data  

- **Environment variables:**
  - Set in **`docker-compose.yml`** under the **web** and **db** services for DB connection and secrets.  

---

### Troubleshooting

- **Postgres connection errors:**  
  Ensure **`DB_HOST=db`** in your `.env` or `docker-compose.yml` (not `localhost`).

- **Password authentication failed:**  
  Reset database by removing the volume:  
  ```bash
  docker-compose down -v
  ```

- **`relation "auth_user" does not exist` or migrations missing:**  
  ```bash
  make migrate
  ```

- **Collect static files (if needed):**  
  ```bash
  docker-compose exec web python manage.py collectstatic --noinput
  ```

---

### Notes

- This setup is for **development** using Django’s built-in server.  
- For production, use **Gunicorn** or another WSGI server and update the Dockerfile.  
- Keep sensitive data in **`.env`** files, not in `docker-compose.yml`.  

---

## 🐳 Dockerized Setup

This project is fully containerized with **Docker** and **Docker Compose**, allowing you to spin up the backend with:
```bash
make start
```
or:
```bash
docker-compose up --build
```

📘 API Documentation
    You can explore and test all APIs through:

    Swagger UI:
    URL: http://localhost:8080/swagger/

    Redoc:
    URL: http://localhost:8080/redoc/


🧪 Testing the API
You can test the complete API workflow using the provided script:

Steps:
Edit the base URL:
1. Open test_api.py and set your local server:
    ```bash
      BASE_URL = "http://localhost:8080"

2. Run the script:
    ```bash
      python test_api.py

##Tests Included:

    User registration
    
    User login
    
    Add a product
    
    Update product quantity
    
    Fetch products list

Make sure your server is running before executing the test script.


**API Endpoints:**

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
