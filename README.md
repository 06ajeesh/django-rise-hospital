# Rise Hospital - Django Web Application

Rise Hospital is a modern web application built with Django and Bootstrap, designed to facilitate patient bookings, showcase doctor profiles, and provide detailed information about hospital departments. This web app is optimized for ease of use and a responsive design, ensuring a seamless experience across devices.

<img src="https://github.com/user-attachments/assets/6efff090-406c-441f-885e-eb63400f978e" width="85%" />

## Features

- **Patient Bookings:** A user-friendly interface to allow patients to book appointments with doctors.
- **Doctor Profiles:** Browse detailed profiles of doctors including their specialties, availability, and contact information.
- **Hospital Departments:** Information on various departments within the hospital.
- **Contact Page:** A simple contact form for inquiries and support.

## Screenshots

Here are some screenshots from the application:

- **Homepage & Navigation**  
  <img src="https://github.com/user-attachments/assets/6efff090-406c-441f-885e-eb63400f978e" width="75%" />

- **Department Profiles**  
  <img src="https://github.com/user-attachments/assets/9f2025db-59c8-4806-9844-55a02d92b1a0" width="75%" />

- **Doctor Profile**  
  <img src="https://github.com/user-attachments/assets/75be136f-05dd-4d95-b5be-9e97bb8099e4" width="75%" />

- **Patient Booking Page**  
  <img src="https://github.com/user-attachments/assets/c2c51a59-0f23-4539-87d1-8ada6b3de0a8" width="75%" />

- **About Page**  
  <img src="https://github.com/user-attachments/assets/d654f0b4-fcfa-4400-aae1-6257f25e9c06" width="75%" />

- **Contact Form**  
  <img src="https://github.com/user-attachments/assets/4ba588ca-3ed3-499b-8d4b-a85c5046219c" width="75%" />



## Technologies Used

- **Django:** The web framework used for backend development.
- **Bootstrap:** For responsive, mobile-first design.
- **SQLite:** The default database for storing application data.

## Installation

To set up the project locally, follow these steps:

### 1. Clone the Repository  
Run the following command in your terminal:  
  ```bash
  git clone https://github.com/06ajeesh/django-rise-hospital.git
  ```  



### 2. Create and Activate a Virtual Environment  
**For Windows:**  
```bash
python -m venv .venv
```
```bash
.venv\Scripts\activate
```

**For macOS/Linux:**  
```bash
python3 -m venv .venv
```
```bash
source .venv/bin/activate
```


### 3. Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4. Change Directory
```bash
cd django-rise-hospital
```

### 5. Apply Database Migrations  
```bash
python manage.py migrate
```

### 6. Run the Development Server  
```bash
python manage.py runserver
```

### 7. Open the Application in Your Browser  
```
http://127.0.0.1:8000/
```

Now, your **Django Rise Hospital** web application is up and running! 🚀
