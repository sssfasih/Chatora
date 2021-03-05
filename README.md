
### Course Name

[CS50’s Web Programming with Python and JavaScript](https://cs50.harvard.edu/web/2020/).


### Requirements

The final project is your opportunity to design and implement a dynamic website of your own. So long as your final project draws upon this course’s lessons, the nature of your website will be up to you, subject to some constraints as indicated below.
In this project, you are asked to build a web application of your own. The nature of the application is up to you, subject to a few requirements:

-   Your web application must be sufficiently distinct from the other projects in this course (and, in addition, may not be based on the  [old CS50W Pizza project](https://docs.cs50.net/web/2020/x/projects/3/project3.html)), and more complex than those.
    -   A project that appears to be a social network is  _a priori_  deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected.
    -   A project that appears to be an e-commerce site is  _strongly suspected_  to be indistinct from Project 2, and your  `README.md`  file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected.
-   Your web application must utilize Django (including at least one model) on the back-end and JavaScript on the front-end.
-   Your web application must be mobile-responsive.
-      
    In a  `README.md`  in your project’s main directory, include a writeup describing your project, and specifically:
    -   Why you believe your project satisfies the distinctiveness and complexity requirements, mentioned above.
    -   What’s contained in each file you created.
    -   How to run your application.
    -   Any other additional information the staff should know about your project.
-   If you’ve added any Python packages that need to be installed in order to run your web application, be sure to add them to a  `requirements.txt`  file!

Beyond these requirements, the design, look, and feel of the website are up to you!

### Chatora - A Chatting Web Application

Chatora is a web-application where users can chat with each other. 

The project is built in Django. Front end processing and DOM Manipulation is done using Javascript (Plain Vanilla JS). Bootstrap is used for CSS. 

Every webpage in this project is Mobile Responsive.

#### Installation

-   Install project dependencies by running  `pip install -r requirements.txt`.
-   Make and apply migrations by running  `python manage.py makemigrations`  and  `python manage.py migrate`.
-   Create superuser with  `python manage.py createsuperuser`. This step is optional.
-   Go to website address and register an account.

#### Files and directories

-   `chatora`  - Main Project directory.
- `chat` - Application directory
    -   `static/chat`  contains all static js files for chat application.
        -   `getcsrf.js`  - contains a function that extracts csrf token from cookies. Taken from Django official documentation.
        -   `send.js`  - it is script responsible for sending text messages from client to server and update the DOM.
        -   `updates.js`  - script responsible to update the DOM.
    -   `templates/chat`  contains all application templates.
        -   `base.html`  - Provides base to `messages.html`, `about.html` and `new_msg.html`.
        -   `layout.html`  - provides base to `login.html` and `register.html`.
        -   `about.html`  - contains my brief introduction.
        -   `login.html`  - contains login page.
        -   `messages.html`  - contains the main page where texts are sent and received.
        -   `new_msg.html`  - contains send a new message page.
        -   `register.html`  - contains sign up page.
      
    -   `admin.py`  - Contains models that are administrate-able in the Admin panel by super user.
    -   `models.py`  contains three models I used in the project.  `User`  model extends the standard `AbstractUser` model,  `Message`  model is for Text Message, and  `Conversation`  represents conversations b/w users.
    -   `urls.py`  - contains all URLs in the application.
    -   `views.py`  - contains all views of the application.
-   `requirements.txt`  - Contains list of Project dependencies. It includes Django and basic utilities that are installed with Django.

### Video Demonstration
 [https://youtu.be/9dTOT5UC_EA](https://youtu.be/9dTOT5UC_EA   )