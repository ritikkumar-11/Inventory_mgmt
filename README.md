Inventory Management System (Backend - Django Rest Framework)

This project is a backend application for managing inventory, built using Django Rest Framework (DRF). It provides RESTful APIs for user authentication and product management.

Features Implemented:

User Authentication (Registration & Login with JWT)

Add New Products

Update Product Quantity

Get List of Products (with pagination)

Stretch Goals Attempted:

Basic Admin Portal: Utilized Django's built-in admin interface for managing data.

Technologies Used:

Language/Framework: Python, Django Rest Framework (DRF)
Database: PostgreSQL

Authentication: Simple JWT (djangorestframework-simplejwt)

API Documentation: Django REST Swagger or DRF-Spectacular

Other Libraries: djangorestframework-simplejwt

Database Schema:
Users Table: Managed by Django's default User model.
Products Table: Custom model storing product details (name, type, sku, image_url, description, quantity, price).


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
