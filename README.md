# Django Database Integration

I am trying to stretch and further myself in learning and coding. There is always somthing to learn. In trying to learn Django I am advancing on the path to be a better programmer and software engineer. 

The web app that I wrote is a simple app that allows you to access a login table in a database. I built the table using a template and it switches between webpages by using calls to other templates. To build the web app I used the default webserver provided by Django and the default SQL light database aslo provided by Django. To start the webserver I first ran Django in a Windows virtual enviorment using the env -m command in the command line. Then I created the web app using the Django startproject command. I next created some content in a .html file and a path to that file in the url.py file. To start the webserver you then call on the manage.py file and tell it to runserver. Then you can brows to http://127.0.0.1:8000/warehouse_login/ which is a call to the localhost on port 8000 with the project name specified. This shows the content of the .html file that you created.

My purpose for writing this software is to learn python more in depth and come to understand Django.

#Video Demonstration of Code
[Software Demo Video](https://youtu.be/GF_IEpYT4No)

# Web Pages

There are three webpages that are created from the templates. The first one show a table of users in the database, by first name, last name, and their password. It also has a button to delete the user, update the user, and there is a button at the bottom that lets you add a new user. The other two pages are forms for updating the user or adding a new user.

# Development Environment

To build this web app I used:
Command Prompt - Is Microsoft Windows Command Line Interface also know as cmd. It allows you to interface with the system.
Django - Is a back end server side frame work used in conjunction with the Python coding language.
Python - Is a Object Oriented Programing (OPP) language. It is popular for its simple syntax.
Visual Studio Code - Is an Integrated Development Enviorment, It works with many different coding languages and provides debugging, syntax highlighting, intelligent code completion, snippets, code refactoring, and embedded Git. 
Git / GitHub - Is a web repository used for traking changes on documents and also provides collaberation with version control.


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [W3Schools Django Tutorial](https://www.w3schools.com/django/index.php)
* [Programming with Mosh Django Course](https://www.youtube.com/watch?v=rHux0gMZ3Eg)

# Future Work

* Add a login screen.
* Add an inventory screen.
* Code the login to go to different places based upon login.
