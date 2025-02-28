# Django Demo App

##  Overview
This is a simple Django demo application that includes three basic pages:  
- **Home Page** (`/`) – Displays a welcome message.  
- **About Page** (`/about/`) – Provides a brief description of the app.  
- **Contact Page** (`/contact/`) – Shows a contact email.  
This app is designed to run **without any HTML files** by directly returning responses from Django views.

##  Features
- Built using **Django** (No frontend framework needed).
- Uses **Django views** to return responses instead of HTML templates.
- Simple and lightweight structure.
- Easily extendable for future features.

##  Installation & Setup
1. **Clone the repository** (or create a new Django project manually):
     git clone https://github.com/your-repo/demo-django-app.git
     cd demo-django-app
2. Create a virtual environment (optional but recommended):
     python -m venv venv
     source venv/bin/activate  # On Windows use: venv\Scripts\activate
3. Install Django:
     pip install django
4. Run the development server:
     python manage.py runserver
5. Access the app in your browser:
- Home Page: http://127.0.0.1:8000/
- About Page: http://127.0.0.1:8000/about/
- Contact Page: http://127.0.0.1:8000/contact/

## Project Structure 
demo_project/
│-- demo_project/    # Main Django project
│   ├── settings.py  # Project settings
│   ├── urls.py      # URL configurations
│-- demo_app/        # Django app
│   ├── views.py     # View functions for Home, About, and Contact
│-- manage.py        # Django management script

## Future Enhancements
Add HTML templates instead of returning plain text.
Include a database and models for dynamic content.
Implement forms on the Contact page.
