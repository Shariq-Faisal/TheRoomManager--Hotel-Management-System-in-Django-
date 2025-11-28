# TheRoomManager 🏨

**TheRoomManager** is a professional **Hotel Management System** built using **Django** and **MySQL**.  
It provides hotel staff with an intuitive dashboard to manage **rooms, customers, bookings, payments**, and **invoices** efficiently. The UI is designed with **AdminLTE** for a modern and responsive interface.

---

## 🌟 Features

- **User Authentication**: Staff registration and login.  
- **Room Management**: Add, edit, delete, and view rooms.  
- **Customer Management**: Add, edit, delete, and view customers.  
- **Booking Management**: Create, update, checkout, and delete bookings.  
- **Payment Management**: Record payments and generate invoices.  
- **Dashboard**: Overview of total rooms, customers, bookings, and revenue.  
- **Invoice Generation**: Generate printable invoices for bookings.  
- **Responsive Design**: Works on desktop and mobile with AdminLTE.  

---

## 🛠 Technology Stack

- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, Bootstrap, AdminLTE  
- **Database**: MySQL  
- **Other**: Django ORM, Django Forms, Django Templates  

---

## 📂 Project Structure

```
TheRoomManager/
│
├─ accounts/          # Custom user authentication
├─ core/              # Main app (rooms, bookings, payments)
├─ templates/         # HTML templates
├─ static/            # CSS, JS, images
├─ manage.py
├─ requirements.txt
└─ README.md
```

---

## ⚡ Installation Guide

1. **Clone the repository**
```bash
git clone https://github.com/Shariq-Faisal/TheRoomManager-DjangoHotelManagement.git
cd TheRoomManager-DjangoHotelManagement
```

2. **Create a virtual environment**
```bash
python -m venv venv
```

3. **Activate the virtual environment**
- Windows: `venv\Scripts\activate`  
- Linux/Mac: `source venv/bin/activate`

4. **Install dependencies**
```bash
pip install -r requirements.txt
```

5. **Configure MySQL database**
- Update `settings.py` with your MySQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

6. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Run the development server**
```bash
python manage.py runserver
```

8. **Open in browser**
- Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 🎨 Screenshots

<img width="1919" height="1019" alt="Screenshot 2025-11-29 012531" src="https://github.com/user-attachments/assets/1fd7c576-c43b-4888-89f8-35c90062163e" />
<img width="1919" height="1020" alt="Screenshot 2025-11-29 012553" src="https://github.com/user-attachments/assets/671509d0-bddb-4c25-b3cc-db874761bef7" />
<img width="1899" height="1016" alt="Screenshot 2025-11-29 012636" src="https://github.com/user-attachments/assets/983e02bc-e252-40b8-98e5-451f2a7b193d" />

<img width="1892" height="968" alt="Screenshot 2025-11-29 012654" src="https://github.com/user-attachments/assets/ebc4f964-cf1c-42ee-98c2-327ce208c636" />
<img width="1860" height="864" alt="Screenshot 2025-11-29 012803" src="https://github.com/user-attachments/assets/b639611d-a33d-4f1e-9d29-6a2fd5396347" />
<img width="1864" height="912" alt="Screenshot 2025-11-29 012819" src="https://github.com/user-attachments/assets/425cb831-09a5-4ae6-b364-44e01ac1d3d3" />
<img width="1873" height="879" alt="Screenshot 2025-11-29 012833" src="https://github.com/user-attachments/assets/e49d0e36-00d7-47e4-9e25-a9ed3018c356" />
<img width="1857" height="797" alt="Screenshot 2025-11-29 012848" src="https://github.com/user-attachments/assets/51f7523b-8288-4569-8a99-6277e8593b1e" />
<img width="1844" height="914" alt="Screenshot 2025-11-29 012905" src="https://github.com/user-attachments/assets/39d64bb2-9de9-4f2a-a68c-00aa81f04c98" />



---

## 📌 Future Enhancements

- Dark/Light mode toggle  
- Email notifications for bookings and invoices  
- Role-based access control for staff  
- Advanced analytics and charts on dashboard  

---

## 📝 License

This project is **open source** and free to use.

