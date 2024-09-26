#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()




#  our project is an Restaurant E-commerce Site using Django 
# the name of the project is FeastNow and the restaurant name is FeastNow and is located in new delhi, india and is a indian family restaurant."FeastNow began its journey in the heart of Delhi's Connaught Place, seven years ago. Founded by my father, it started as a humble Indian family vegetarian restaurant, driven by a passion for authentic flavors and warm hospitality. Over the years, we've grown, serving delicious meals and creating memorable experiences for our patrons

# # First of all I am using Virtual environment for the project . and Sqlite database
# and There is templates folder which has all the html files and static folder which has all the css and js files and images and profile_pics folder which has all the profile pics of the users and products folder which has all the product images.
# # I have created a superuser for the project using the command python manage.py createsuperuser
# # I have created a model for the project which has the following fields:
# 1. Customer
# 2. Product
# 3. Orders
# 4. Feedback
# the name of the app is ecom and the name of the project is FeastNow ( which is the name of the restaurant)

#  the customer can signup and login and can view the products and can add the products to the cart and can view the cart and can remove the products from the cart and can add the address and can make the payment and can view the orders and can download the invoice of the orders and can view the profile and can edit the profile and can send the feedback can search the products and can view the about us and contact us page.

# the admin can login and can view the customers and can delete the customers and can update the customers and can view the products and can add the products and can delete the products and can update the products and can view the orders and can delete the orders and can update the orders and can view the feedbacks and can view the customers and can view the bookings and can delete the bookings and can update the bookings.

# there is a seperate login for the admin and the customer and the admin can view the admin dashboard and the customer can view the customer home page.

# there are many types of forms used in the project like:
# 1. CustomerUserForm
# 2. CustomerForm
# 3. ProductForm
# 4. AddressForm
# 5. FeedbackForm
# 6. OrderForm
# 7. ContactusForm

# there are many types of views , some of main views are:
# 1. home_view to view the home page
# 2. adminclick_view to check if the user is admin or not
# 3. is_customer to check if the user is customer or not
# 4. @login_required a decorator to check if the user is logged in or not

# # here we are taking address, email, mobile at time of order placement we are not taking it from customer account table because these thing can be changes


# Based on the provided information about the FeastNow project, here are some key features to consider, including the invoice feature:

# 1. **User Authentication and Authorization:**
#    - Allow users to sign up and log in securely.
#    - Implement role-based access control to differentiate between customers and administrators.

# 2. **Product Management:**
#    - Enable customers to view the available products with details such as name, description, price, and images.
#    - Implement search and filter functionalities to help users find products efficiently.

# 3. **Shopping Cart Functionality:**
#    - Provide users with the ability to add products to their shopping cart, view the cart contents, and modify quantities or remove items as needed.

# 4. **Order Placement and Management:**
#    - Allow users to proceed to checkout, where they can enter shipping details, select payment methods, and confirm their orders.
#    - Generate order invoices with itemized lists, quantities, prices, and total amounts for user reference and record-keeping.

# 5. **Profile Management:**
#    - Allow users to view and edit their profiles, including personal information such as name, email, and address.
#    - Provide options to update password and manage communication preferences.

# 6. **Feedback System:**
#    - Implement a feedback form where users can submit their thoughts, suggestions, or complaints about their experience with the platform or specific orders.

# 7. **About Us and Contact Us Pages:**
#    - Include dedicated pages with information about the restaurant, its history, mission, and contact details for inquiries or support.

# 8. **Admin Dashboard:**
#    - Provide administrators with a dashboard to manage customer accounts, products, orders, feedback, and bookings efficiently.
#    - Enable admins to view, add, edit, and delete records as needed, with proper validation and permissions.

# 9. **Invoice Generation:**
#    - Integrate functionality to automatically generate invoices for each completed order.
#    - Include details such as order number, date, customer information, product details, subtotal, taxes, shipping fees, and total amount.
#    - Allow users to download and print invoices for their records or reference.

# By incorporating these features into the FeastNow project, you can create a comprehensive and user-friendly restaurant e-commerce platform that meets the needs of both customers and administrators.

# https://chat.openai.com/share/53946740-654d-4d1a-a153-7c9d0e800468