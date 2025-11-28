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

![alt text](<Screenshot 2025-11-29 012531.png>)

![alt text](<Screenshot 2025-11-29 012553.png>)


![alt text](<Screenshot 2025-11-29 012636.png>)

![alt text](<Screenshot 2025-11-29 012654.png>) 

![alt text](<Screenshot 2025-11-29 012803.png>)

![alt text](<Screenshot 2025-11-29 012819.png>)


![alt text](<Screenshot 2025-11-29 012833.png>)
   
![alt text](<Screenshot 2025-11-29 012848.png>)
![alt text](<Screenshot 2025-11-29 012905.png>) 

---

## 📌 Future Enhancements

- Dark/Light mode toggle  
- Email notifications for bookings and invoices  
- Role-based access control for staff  
- Advanced analytics and charts on dashboard  

---

## 📝 License

This project is **open source** and free to use.

