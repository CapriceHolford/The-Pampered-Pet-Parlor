
The Pampered Pet Parlor

This is my final project with CodeInstitute, it involves the development of a full-stack web application using the Django Web framework, following Agile methodologies for planning and execution. The application aims to provide an intuitive platform for managing pet grooming services, allowing users to book appointments, manage their profiles, and view posts about past grooms. The website integrates a responsive front-end with custom models to handle user authentication, pet profiles, and booking data, while ensuring accessibility and usability. The project includes database development, CRUD functionality, role-based access control, and notifications, culminating in the deployment of the application to Heroku (a cloud based platform) with a focus on security and performance.



## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [Font Awesome](https://fontawesome.com/)
- [Free Pik](https://www.freepik.com/)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)
- [Pexels](https://www.pexels.com/)
- [Pixabay](https://pixabay.com/)

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#5cc8ff](https://via.placeholder.com/10/5cc8ff?text=+) #5cc8ff |
| Example Color | ![#ead5e6](https://via.placeholder.com/10/ead5e6?text=+) #ead5e6 |
| Example Color | ![#d81e5b](https://via.placeholder.com/10/d81e5b?text=+) #d81e5b |
| Example Color | ![#0c2e10](https://via.placeholder.com/10/0c2e10?text=+) #oc2e10 |


![Logo](staticfiles/images/logo1-fotor-2025010215655.png)
- I created this logo using [chatgpt](https://chatgpt.com/)


## Features

### Core Features 
- Blog Section
- Booking System
- Cross platform
- CRUD Functionality
- Database Management
- Deployment 
- Live previews
- Notifications
- Responsive Design
- Role-Based Access Control
- User Registration and Authentication

### Additional Features 
- Light/dark mode toggle
- Pet Grooming History
- User Profile Management







## Tech Stack

**Frontend:** HTML, CSS (Bootstrap), JavaScript, FontAwesome

**Backend:** Django (Python), Django ORM, SQLite (development)

**Version Control:** Git, GitHub

**Deployment:** Heroku, Whitenoise

**Authentication:** Django Allauth


## FAQ

#### How do I run the project locally?

- Clone the repository: git clone https://github.com/yourusername/yourproject.git
- Install dependencies: pip install -r requirements.txt
- Apply database migrations: python manage.py migrate
- Run the development server: python manage.py runserver
- Visit http://127.0.0.1:8000 in your web browser.


#### How do I add or modify content (like blog posts or services)?

- Blog posts: Blog posts are created by the groomer/admin in the admin panel. Only authorized users with admin privileges can access the blog section to add or edit posts.
- Services: Services can be added or edited through the admin panel as well. Users with admin privileges can define the grooming services available for booking.

#### How does user authentication work?
Users can register, log in, and manage their profiles using the Django Allauth authentication system. Once logged in, users can access features like booking appointments, viewing their profiles, and editing their pet profiles. Groomers and admins have access to additional features such as managing blog posts and services.

#### How can I change my profile information?
Users can edit their profile information, including their email, username, and password, from the profile page. If the user has a pet profile, they can also add, edit, or delete pet profiles from their account settings.

#### How can I book an appointment?
Users can book an appointment by visiting the Booking page. They will need to provide their pet’s details and choose the service they want. The appointment will be stored in the database, and users will receive confirmation.

#### Can users with different roles access different sections?
Yes, the application supports role-based access. Regular users can manage their profiles and book appointments, while groomers and admins have additional privileges such as managing blog posts, editing services, and handling user data.

#### How can I test the application?
You can run the application locally and manually test all the features such as registration, login, profile management, booking an appointment, and editing pet profiles. Additionally, automated tests can be written for Django models, views, and forms to ensure the correct functionality of the application.





# Lessons Learned During the Project

## 1. Full-Stack Development with Django
Through this project, I learned how to effectively create a full-stack web application using the Django web framework. I gained a deeper understanding of Django's MVC architecture, working with models, views, and templates, and managing databases using Django's ORM.

## 2. Front-End Design and Responsiveness
I worked with HTML, CSS, and Bootstrap to create responsive, user-friendly designs. This involved using Flexbox and Grid for layout, applying CSS media queries for mobile responsiveness, and ensuring accessibility by following Web Content Accessibility Guidelines (WCAG).

## 3. Working with Django Models and the ORM
I designed and implemented custom models for various features of the website, such as user profiles, bookings, and pet profiles. I learned how to create relationships between models using Foreign Keys and ManyToMany fields and how to manage database migrations efficiently.

## 4. CRUD Functionality
I implemented the ability for users to create, read, update, and delete records, such as adding and editing pet profiles and bookings. I used Django’s ModelForms and validated user inputs to ensure secure and error-free data management.

## 5. User Authentication and Authorization
I learned how to implement user authentication using Django Allauth, allowing users to register, log in, and manage their accounts. Additionally, I incorporated role-based access control to restrict certain content, such as pet profiles and bookings, to authenticated users only.

## 6. Agile Methodology for Project Management
I applied Agile principles by using tools like Trello and GitHub Projects to plan, track, and manage tasks. This included breaking down features into user stories, prioritizing tasks, and using sprints to meet deadlines.

## 8. Testing and Debugging
I practiced testing in Django, including writing unit tests for views, models, and forms. I learned how to use Django’s built-in testing framework and `pytest` to ensure the functionality and security of my application.

## 8. Deployment to Heroku
I successfully deployed the application to Heroku, ensuring that it was configured for a production environment. This included setting up environment variables for secret keys, using Whitenoise for static file handling, and ensuring the application was secure by turning off DEBUG mode.

## 9. Code Quality and Version Control
Throughout the project, I followed best practices for code readability, such as consistent naming conventions, proper indentation, and meaningful comments. I also used Git for version control, making regular commits with detailed messages to track progress.

