🏥 Ultimate Django Hospital Management System

A comprehensive hospital management system built with Django that provides an end-to-end solution for managing patients, doctors, staff, appointments, billing, and medical reports. This project is designed to streamline hospital workflows with role-based access, a responsive UI, and secure data management.

🚀 Features
🔐 Authentication & Roles

Secure login & signup system

Role-based dashboards for:

Admin – Manage doctors, patients, appointments, billing & reports

Doctor – View/manage assigned patients, approve/reject appointments, upload medical reports

Patient – Book appointments, view medical history, download bills & reports

Staff – Register patients, manage appointments & generate bills

👩‍⚕️ Patient Management

Register new patients with personal & medical details

Search, update, and manage patient records

Maintain patient medical history

👨‍⚕️ Doctor Management

Add/update doctors with specialization, schedule, and availability

Assign patients to doctors

Manage consultation fees and schedules

📅 Appointment System

Patients can book appointments online

Doctors approve/reject/view their schedules

Admin/Staff manage time slots and availability

💳 Billing & Payments

Generate bills for consultations, medicines, and room charges

Track payments (paid/unpaid)

Patients can view/download invoices

📑 Reports Management

Doctors can upload patient medical reports

Patients can view/download reports securely

Admin can generate hospital revenue & performance reports

📊 Additional Features (Optional / Advanced)

Email/SMS notifications for appointment reminders

Dashboard with charts (appointments per day, revenue stats)

Online payment gateway integration (Stripe/Razorpay)

🛠️ Tech Stack

Backend: Django, Django ORM

Frontend: Django Templates, HTML, CSS, Bootstrap

Database: SQLite (default), can be switched to MySQL/PostgreSQL

Authentication: Django’s built-in auth system with a custom user model

Deployment: Django Admin for management, local server (Heroku/Render compatible)

📂 Project Structure
hospital_management/
│── hospital_management/     # Project settings, URLs, WSGI
│── core/                    # Custom user model & authentication
│── patients/                # Patient-related models & views
│── doctors/                 # Doctor-related models & views
│── appointments/            # Appointment management
│── billing/                 # Billing system
│── reports/                 # Medical reports
│── templates/               # HTML templates
│── static/                  # CSS, JS, images
│── media/                   # Uploaded files (reports, docs)
│── manage.py

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/yourusername/hospital-management-system.git
cd hospital-management-system


Create & activate virtual environment

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py makemigrations
python manage.py migrate


Create a superuser (Admin account)

python manage.py createsuperuser


Run the server

python manage.py runserver


Access the app at: 👉 http://127.0.0.1:8000/

🖥️ Screenshots (Optional)

(Add images/gifs of your UI — patient registration, doctor dashboard, billing page, etc.)

🔮 Future Enhancements

Integration with Razorpay/Stripe for online payments

Advanced analytics dashboard with Chart.js/Recharts

Appointment reminders via Email/SMS

Docker support for containerized deployment
