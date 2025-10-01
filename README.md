# 📅 Event Management System

An Event Management System built with **Django** that allows users to view, register, and manage events.  
The system has a clean dashboard with sections for Home, Upcoming Events, Past Events, and Contact.  

---

## 🚀 Features
- 🏠 **Home Page** with welcoming message, background image, story, and core values.
- 🎉 **Upcoming Events** – List of all upcoming events with details.
- 🕰 **Past Events** – Archive of past events for reference.
- 📬 **Contact Section** – Contact information for inquiries and collaborations.
- 🎨 Modern responsive design with catchy hero banner and styled navigation.
- 🔎 Clean separation of sections (each section is displayed when clicked in the navbar).
- ⚡ Built with Django templating system and static files.

---

## 🛠️ Tech Stack
- **Backend:** Django 5.x
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (default, can be switched to PostgreSQL/MySQL)
- **Styling:** Custom CSS (no external frameworks)

---

## 📂 Project Structure
eventsite/ # Django project folder
│
├── events/ # Main app
│ ├── templates/events/ # HTML templates
│ ├── static/events/ # Static files (CSS, JS, images)
│ ├── models.py # Event and Registration models
│ ├── views.py # Views for handling requests
│ ├── urls.py # App-specific URLs
│
├── eventsite/ # Project settings and urls
├── manage.py

yaml
Copy code

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/event-management.git
   cd event-management
Create and activate virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate    # On Linux/Mac
venv\Scripts\activate       # On Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run migrations

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create superuser (for admin panel)

bash
Copy code
python manage.py createsuperuser
Run the server

bash
Copy code
python manage.py runserver
Access the site

cpp
Copy code
http://127.0.0.1:8000/
📸 Screenshots
(Add screenshots here of your Home, Upcoming Events, Past Events, and Contact pages)

📬 Contact
Developer: Basil Mutuku

Email: basil59mutuku@gmail.com

Phone: +254 768 378 553

📝 License
This project is licensed under the MIT License – feel free to use and modify it.
