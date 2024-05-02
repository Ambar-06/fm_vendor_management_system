# Vendor Management System

## Description
This is a simple vendor management system that allows users to add, edit, delete and view vendors. It also allows users to add, edit, delete and view purchase orders and track vendors' performance. The system is built using Django and Django REST framework.


## Features
- Add, edit, delete and view vendors
- Add, edit, delete and view purchase orders

## Technologies
- Python
- Django
- Django REST framework
- SQLite

## Installation
1. Clone the repository
```bash
git clone
```
2. Create a virtual environment
```bash
python -m venv venv
```
3. Install the requirements
```bash
pip install -r requirements.txt
```
4. Run the migrations
```bash
python manage.py migrate
```
5. Create .env file and copy the variables given in the .env.example file
6. Run the server
```bash
python manage.py runserver
```

## API Endpoints
- ```/api/vendors/``` - GET, POST 
- ```/api/vendors/{id}/``` - GET, PUT, DELETE
- ```/api/purchase-orders/``` - GET, POST
- ```/api/purchase-orders/{id}/``` - GET, PUT, DELETE
- ```/api/vendors/{id}/performance``` - GET


## Project Structure
- vendors - Django app for related models
- purchase_orders - Django app for related models
- common - Django app for helper functions and boilerplate
- analytics - Django app for performance tracking models
- api - Django app for API views, serializers, urls and services

## Patterns Followed
- SRP (Single Responsibility Principle) - Each class and function has a single responsibility
- DRY (Don't Repeat Yourself) - Repeated code is refactored into helper functions
- KISS (Keep It Simple, Stupid) - Code is simple and easy to understand
- YAGNI (You Aren't Gonna Need It) - Only necessary features are implemented
- Beautiful is better than ugly - Code is clean and readable (ZEN of Python)
- Readability counts - Code is easy to read and understand (ZEN of Python)

## Authentication Method Used
- Custom token-based authentication : Token is generated when a user is created and is used to authenticate the user for all API requests (But for this MVP, the Token is generated using a Custom Random String stored in .env file and is used for all users)
