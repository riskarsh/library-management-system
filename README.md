# Library Management System

## 1. How to run this application?

Clone this project with git clone.
```
git clone https://github.com/riskarsh/library-management-system.git
```
    
Create a virtual environment
```
python3 -m venv venv 
source venv/bin/activate
```

Install the dependencies which is given in requirements.txt
```
pip install -r requirements.txt
```

Update database information in ***library/settigs.py*** under DATABASES
(make sure to update the `USER` `PASSOWORD` to match your mysql credentials and make sure the database name "library" exists )
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "library",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        }
    }
``` 
Create the table and set-up the database in mysql.
```
python manage.py migrate
```
Run the Django application
```
python manage.py runserver
```


## 2. Components in the application.

The library contains 2 applications,
* Books
* Accounts
        
Books has views to **CREATE, UPDATE, LIST** and **DELETE** books in the system.

Accounts has views to **Signup, Signin** and **Signout**  the admin


## 3. User guide.
    
### As an Admin
#### How to signup:
- Click on the "Sign up" button in the home page.
- Fill in your email address and password
- Click on "Signup"

#### How to signin:
- Click on the "Sign in" button in the home page in top right.
- Fill in your email address and password
- Click on "Signin"










