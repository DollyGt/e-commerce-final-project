# TruBlu Sewlutions Hair: e-commerce project

A simple web interface that implements a simple and secure e-commerce using Python and Django.

# Overview

Each user can register to the website by providing first name,  password and email address. Only a  registered user can access checkout and would also be able to leave a review and rate the products based on their experiences. Non registered users can only view products.
Once user is authenticated their session would expire within 2 minutes if they were to be inactive within that time period. If a user tries to perform any activity which requires user authentication after 2 minutes of inactivity, the operation must be discarded and the user redirected again to a login page. The user must be forced to use the HTTPS protocol for the authentication process and for all the operations that require user authentication.

REMEMBER TO EDIT

# UX

Use this section to provide insight into your UX process, focusing on who this website is for, what it is that they want to achieve and how your project is the best way to help them achieve these things.

In particular, as part of this section we recommend that you provide a list of User Stories, with the following general structure:


This section is also where you would share links to any wireframes, mockups, diagrams etc. that you created as part of the design process. These files should themselves either be included in the project itself (in an separate directory), or just hosted elsewhere online and can be in any format that is viewable inside the browser.

# Features

Home page

First page of the application. This page shows the store window with products, price, reviews, cart and categories.
The user can Log In if they are already registered or Sign Up by registering if they are not already registered.
Doing the Log In, the user will be redirected to the Store/home page.
If a User Session is open, all the requests for the Index page will be redirected to the Store/home page.

Dependencies:

index.html - Log In

Account, registration

User Registration From. 

This module gets the user paramters from the Registration Form, performs the appropriate checks and writes the user data in the database.

Dependencies:

register.html - Register 

products, categories

In this page the user can choose the products they want to buy. A lateral bar indicates the log status and the cart status.

Dependencies:

products.html - Add Items to the Cart - cart.html

products_detail.html - Show the Cart - cart.html

cart

This module gets the cart parameters from the Add To Cart Form, performs the appropriate checks and write the cart data in the database 
At the end of all the operation, the module redirects the user to the Store/home page.

Dependencies:

cart.html - products.html

cart, checkout

This page shows the Cart with products, quantity and total amount of chosen products.
The user can pay for the chosen products (putting the credit card parameters), empty the cart or go back to the store. In this page, the user has 2 options, either to click on continue shopping button or check out button. The continue shopping redirects the user to products. With the checkout, upon payment, the module gets the credit card parameters from the Payment Form, checks the chosen products and then simulates a payment transation. In case of successful transation, the module empties the cart.
Any unregistered users who attempts to make a payment will get an error message to let them know that they must first register before there could be allowed to proceed with their payment.

Dependencies:

Checkout.html - home page

# Features Left to Implement

I would like to add a feature that would allow registered customers to be informed of new arrivals and monthly offers without having to be logged on the website. Registered users would have to first agree with these terms and conditions then they can receive such information via email whenever such offers exists. This would ensure  that registered customers would be the first to know of any news regarding the products earlier than others. I would also like to add bidding feature that would allow registered customers to bid for products based on meeting a certain criteria in which only after they have spent so much in total within a particular period can they access the bidding platform. Bidding would ensure that at some point they would be likely to purchase an item at a mush lower price.

# Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

JQuery
The project uses JQuery to simplify DOM manipulation.

1.HTML5

2.CSS3

3.JavaScript/jQuery

4.Bootstrap/ fontawesome/google fonts

5.Python3

6.Django2

REMEMBER TO EDIT

# Testing

All code has been tested to make sure that everything is working as expected. Automated tests were carried out with Travis-CI. All automated tests can be viewed in the tests.py files. Due to the nature of the technologies used for this project, you would have to view different tests from each app’s tests.py separately. For example: $ python3 accounts.py test  (accounts i.e app name) tests only for:

1.Login details

2.Registration form – by validating it

3.Registration email

4.User registration form etc..

The website is user friendly, recognises  desktop browsers and it is also mobile compatible. Using webview/ chrome view and safari same website can be used as an Android App with zero changes.

Below is an overview of how the site looks with different screen sizes.
    *****____________________******

Contact form:

Go to the "Contact Us" page
Try to submit the empty form and verify that an error message about the required fields appears
Try to submit the form with an invalid email address and verify that a relevant error message appears
Try to submit the form with all inputs valid and verify that a success message appears.
In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

# Deployment

This site is hosted in Heroku. Click here to see a live version.

1.You would have to go to the repository where your deployment is intended to be set

2.While on the repository page, go to settings at the top far right corner of the page

3.Navigate to GitHub pages section and then click and select master branch

4.Proceed to click on save

# Getting the code to run and install

1.You would have to first clone this repository by way of running the git clone

2.Then use the following commands to install what you would need to be installed:

	$ sudo pip3 install Django

	$ sudo pip3 install django-forms-bootstrap

	$ sudo pip3 install pillow 

	$ sudo pip3 -r install requirements.txt

# Content

The text for section Y was copied from the Wikipedia article Z

# Media

All images used are obtained from pexels website

# Acknowledgements

I got the inspiration of this website from sunlight hair extensions website and tried to replicate it using only the technologies mentioned above. Here is the link to their website.

REMEMBER TO EDIT------------------
