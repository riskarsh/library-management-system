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
(make sure to update the `USER` `PASSWORD` to match your mysql credentials and make sure the database name "library" exists )
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

The library contains 2 applications, **books and accounts**.

### Books    
Books has views to **CREATE, UPDATE, LIST** and **DELETE** books in the system.
Only library admins are allowed to create update and delete books, Students can only view the books in read-only mode.

#### Data model
Books are stored in `books_book` table in the provided database.
Each book is stored in a row and has the following properties:
- Name(string)
- Author(string)
- ISBN(integer)
- Pages(integer)
- Published Year(integer) 

### Accounts
Accounts has views to **Signup, Signin** and **Signout**  the admin.
It includes a custom user model for Django, `LibraryAdmin`, which provides email as an indentifier with unique contraints such that no two admins can have the same email address. 


## 3. User guide.
    
### As an Admin
#### How to signup:
- Click on the "Sign up" button in the home page
- Fill in your email address and password
- Click on "Signup" button

#### How to signin:
- Click on the "Sign in" button in the home page in top right.
- Fill in your email address and password
- Click on "Signin" button


#### How to Add a book:
- First signin as library admin
- Click on "Add book" button in the top bar
- Fill in details of the book
- Click on "Add" button


#### How to Update a book:
- First signin as library admin
- Click on the "Edit" button for the book you want to edit
- Update the required fields
- Click on "Update" button 


#### How to Delete a book:
- First signin as library admin
- Click on the "Delete" button for the book you want to Delete
- On the confirmation page, click on "Delete" button


### As a student
#### How to view all books:
- Open http://127.0.0.1:8000/books/ in the browser and it will show all avaliable books.












