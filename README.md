# TruBlu Sewlutions Hair: e-commerce project

A simple web interface that implements a simple and secure e-commerce using Python and Django.

# Overview

Human hair extensions for all ladies alike have never been in greater demand therefore i have decided to create my own hair extensions website for learning purposes.

# UX

Each user can register to the website by providing first name,  password and email address. Only a  registered user can access checkout and would also be able to leave a review and rate the products based on their experiences. Non registered users can only view products.
Once user is authenticated their session would expire within 2 minutes if they were to be inactive within that time period. If a user tries to perform any activity which requires user authentication after 2 minutes of inactivity, the operation must be discarded and the user redirected again to a login page. The user must be forced to use the HTTPS protocol for the authentication process and for all the operations that require user authentication.

All wireframes are manually drawn with a pencil and can be accessed in media folder in the main project.

# Screenshots.

![alt text](https://github.com/DollyGt/e-commerce-final-project/blob/master/media/screenshot1.png)

![alt text](https://github.com/DollyGt/e-commerce-final-project/blob/master/media/screenshot2.png)



# Features

* Home page

First page of the application. This page shows the store window with products, price, reviews, cart and categories.
The user can Log In if they are already registered or Sign Up by registering if they are not already registered.
Doing the Log In, the user will be redirected to the Store/home page.
If a User Session is open, all the requests for the Index page will be redirected to the Store/home page.

Dependencies:

index.html - Log In

* Account, User registration form

This module gets the user paramters from the Registration Form, performs the appropriate checks and writes the user data in the database.

Dependencies:

register.html - Register 

* products, categories

In this page the user can choose the products they want to buy. A lateral bar indicates the log status and the cart status.

Dependencies:

products.html - Add Items to the Cart - cart.html

products_detail.html - Show the Cart - cart.html

* cart

This module gets the cart parameters from the Add To Cart Form, performs the appropriate checks and write the cart data in the database 
At the end of all the operation, the module redirects the user to the Store/home page.

Dependencies:

cart.html - products.html

* cart, checkout

This page shows the Cart with products, quantity and total amount of chosen products.
The user can pay for the chosen products (putting the credit card parameters), empty the cart or go back to the store. In this page, the user has 2 options, either to click on continue shopping button or check out button. The continue shopping redirects the user to products. With the checkout, upon payment, the module gets the credit card parameters from the Payment Form, checks the chosen products and then simulates a payment transation. In case of successful transation, the module empties the cart.
Any unregistered users who attempts to make a payment will get an error message to let them know that they must first register before there could be allowed to proceed with their payment.

Dependencies:

Checkout.html - home page

# Features Left to Implement

I would like to add a feature that would allow registered customers to be informed of new arrivals and monthly offers without having to be logged on the website. Registered users would have to first agree with these terms and conditions then they can receive such information via email whenever such offers exists. This would ensure  that registered customers would be the first to know of any news regarding the products earlier than others. I would also like to add bidding feature that would allow registered customers to bid for products based on meeting a certain criteria in which only after they have spent so much in total within a particular period can they access the bidding platform. Bidding would ensure that at some point they would be likely to purchase an item at a mush lower price.

# Technologies Used

1.HTML5

2.CSS3

3.JavaScript/jQuery

4.Bootstrap/ fontawesome/google fonts

5.Python3

6.Django2

# Testing

All code has been tested to make sure that everything is working as expected. Automated tests were carried out with Travis-CI. All automated tests can be viewed in the tests.py files. Due to the nature of the technologies used for this project, you would have to view different tests from each app’s tests.py separately. For example: $ python3 accounts.py test  (accounts i.e app name) tests only for:

1.Login details

2.Registration form – by validating it

3.Registration email

4.User registration form 

Contact form, check out form, login form, register form were all tested to ensure that:

when the user attempts to submit the empty form an error message about the required fields appears

when the user attempts to submit the invalid email address error message appears

In the instance that all forms are filled correctly success message appears.

The website is user friendly, recognises  desktop browsers and it is also mobile compatible. Using webview/ chrome view and safari same website can be used as an Android App with zero changes.

# Deployment

1.You would have to go to the repository where your deployment is intended to be set

2.While on the repository page, go to settings at the top far right corner of the page

3.Navigate to GitHub pages section and then click and select master branch

4.Proceed to click on save

# Getting the code to run and install

1.You would have to first clone this repository by way of running the git clone

2.Then use the following commands to install what you would need to be installed:

 ```$ sudo pip3 install Django

    $ sudo pip3 install django-forms-bootstrap

    $ sudo pip3 install pillow

    $ sudo pip3 -r install requirements.txt
```
# Demo

This site is hosted in Heroku. Click [here](https://ecommercedolly.herokuapp.com/) to see a live version.

# Media

All images used were obtained from pexels website [here](https://www.pexels.com/).

# Acknowledgements

I got the inspiration of this website from sunlight hair extensions website and tried to replicate it using only the technologies mentioned above. Here is the [link](https://sunlighthumanhair.aliexpress.com/store/1019491?src=google&albch=search&acnt=479-062-3723&isdl=y&aff_short_key=UneMJZVf&albcp=266121556&albag=7593673036&slnk=&trgt=dsa-125690196044&plac=&crea=64152518716&netw=g&device=c&mtctp=b&memo1=1t1&albbt=Google_7_search&aff_platform=google&gclid=EAIaIQobChMIoqX7r_eP3QIVz7_tCh1N4gOUEAAYASAAEgKeR_D_BwE) to their website.


