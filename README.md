
# Feastnow

**Feastnow** is an e-commerce platform for ordering food online, built using Django. This application allows users to browse, order food , manage their orders, and update their profiles.

## Features

- User Authentication (Login/Signup)
- Browse Dishes
- Add to Cart and Checkout
- Order History Management
- User Profile with Profile Picture
- Admin Panel for Managing Orders, Dishes, and Feedback

## Prerequisites

- Python 3.x
- Django
- Virtualenv 
## Installation

Follow these steps to set up the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/RaghavOG/Feastnow.git
cd Feastnow
```

### 2. Create a Virtual Environment 

Using `virtualenv` is a good practice to manage dependencies and avoid conflicts.

#### Install `virtualenv` (if not already installed)

```bash
pip install virtualenv
```

#### Create and activate the virtual environment

For macOS/Linux:
```bash
virtualenv venv
source venv/bin/activate
```

For Windows:
```bash
virtualenv venv
venv\Scripts\activate
```

### 3. Install Dependencies

Once the virtual environment is active, install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run the following command to apply migrations and set up the database:

```bash
python manage.py migrate
```

### 5. Create a Superuser

To access the admin dashboard, you'll need a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to create a username, email, and password.

### 6. Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000`.

## Admin Panel

The admin panel allows the administrator to manage customers, orders, dishes, and feedback. To log in as an admin, use superuser to make admin credentials :

- Admin login: `http://127.0.0.1:8000/adminlogin`
  
Admins can:
- View and manage customer orders
- Add new dishes
- View feedback from customers

## User Profile

Users can view and update their profile information, including:
- Changing profile picture
- Updating personal details

## Usage

- Navigate to the homepage to browse available restaurants and food items.
- Add items to your cart, proceed to checkout, and manage orders.
- Admins can log in to `/adminlogin` for managing orders and content.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
