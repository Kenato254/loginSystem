## BASIC LOGIN SYSTEM Built with Django
### Intro ##
### This is a simple authenication app developed using Django framework. It's a part of topics I covered during #100DaysOfCode challenge. My motivation to build this project was to put into practise what I learned during the above mentioned challenge as well as to tighten up my Django skills. This mini-app can be easily integrated into a bigger system project that needs an email and a password to authenticate a user. ###

### Features ###
* Register new user.
* Login old users using an Email and a Password. 
* Delete/Deactive old users (Sets is_active=False).
* Change/Reset password and email backend configured to display emails in console.
### Install Python ###
* Python 3.xx
### Install Virtualenv ###
* python3 -m venv /path/to/new/virtual/environment
### Activate Virtualenv ###
* source venv/bin/activate -- Linux Users
### Install Requirements ###
* pip install -r requirements.txt 
### Create and Populate DB ###
* python manage.py makemigrations
* python manage.py migrate
### Start Tailwind CSS ###
python manage.py tailwind start
### Runserver ###
* python manage.py runserver