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

<img width="1857" height="797" alt="Screenshot 2025-11-29 012848" src="https://github.com/user-attachments/assets/1a185832-68cb-40b2-baad-90a21fbac841" />
<img width="1873" height="879" alt="Screenshot 2025-11-29 012833" src="https://github.com/user-attachments/assets/7aa642dc-aebb-40ec-86d8-4b11e7a681a1" />
<img width="1864" height="912" alt="Screenshot 2025-11-29 012819" src="https://github.com/user-attachments/assets/bc0c6af0-2742-4379-bb82-7b51fe0fd33b" />
<img width="1860" height="864" alt="Screenshot 2025-11-29 012803" src="https://github.com/user-attachments/assets/4d048207-663f-45be-ac22-4f46cee88d67" />
<img width="1892" height="968" alt="Screenshot 2025-11-29 012654" src="https://github.com/user-attachments/assets/124151fc-0c4e-49a0-bed4-0dc7500d111a" />
<img width="1899" height="1016" alt="Screenshot 2025-11-29 012636" src="https://github.com/user-attachments/assets/ff71ea8b-5be8-41cd-9632-03d9310759cc" />
<img width="1919" height="1020" alt="Screenshot 2025-11-29 012553" src="https://github.com/user-attachments/assets/4bac1d4f-0233-407a-94ec-a2b1a7e99a3a" />
<img width="1919" height="1019" alt="Screenshot 2025-11-29 012531" src="https://github.com/user-attachments/assets/13b949dc-e91b-45fc-8eeb-1511474ee588" />
<img width="1844" height="914" alt="Screenshot 2025-11-29 012905" src="https://github.com/user-attachments/assets/93f1f17b-0549-47c8-8797-90bf0d4c8440" />

---

## 📌 Future Enhancements

- Dark/Light mode toggle  
- Email notifications for bookings and invoices  
- Role-based access control for staff  
- Advanced analytics and charts on dashboard  

---

## 📝 License

This project is **open source** and free to use.

