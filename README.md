# 🏥 Clinic Appointment Booking API

## 📄 Overview

Bu loyiha bemorlar va doktorlar uchun **clinic appointment booking system** yaratadi.
Foydalanuvchilar:

* **Admin** – barcha ma’lumotlarni boshqaradi
* **Doctor** – o‘z ish jadvalini yaratadi va appointment statusini boshqaradi
* **Patient** – doctor qabuliga yoziladi va appointmentlarni bekor qilishi mumkin

API RESTful va Django + DRF + JWT asosida ishlaydi.

---

## 🛠 Technologies

* Python 3.x
* Django 4.x
* Django REST Framework (DRF)
* PostgreSQL
* JWT Authentication (`djangorestframework-simplejwt`)
* Swagger / Redoc (`drf-spectacular`)
* `.env` (environment variables)
* Git + GitHub

---

## 📂 Project Structure

```
clinic_api/
├── apps/
│   ├── users/
│   ├── doctors/
│   ├── timeslots/
│   ├── appointments/
├── core/
│   ├── settings.py
│   ├── urls.py
├── .env.example
├── requirements.txt
├── README.md
```

---

## 🔐 Authentication

### Endpoints

| Method | Endpoint                 | Description                     | Access |
| ------ | ------------------------ | ------------------------------- | ------ |
| POST   | /api/auth/register/      | Yangi user ro‘yxatdan o‘tkazish | Public |
| POST   | /api/auth/login/         | JWT token olish                 | Public |
| POST   | /api/auth/token/refresh/ | Access tokenni yangilash        | Auth   |
| GET    | /api/auth/me/            | Joriy user ma’lumotlari         | Auth   |

---

## 👤 Users (Admin)

| Method | Endpoint         | Description      | Access |
| ------ | ---------------- | ---------------- | ------ |
| GET    | /api/users/      | Barcha userlar   | Admin  |
| GET    | /api/users/{id}/ | User detail      | Admin  |
| PATCH  | /api/users/{id}/ | Userni yangilash | Admin  |
| DELETE | /api/users/{id}/ | Userni o‘chirish | Admin  |

---

## 👨‍⚕️ Doctors

| Method | Endpoint                     | Description                   | Access         |
| ------ | ---------------------------- | ----------------------------- | -------------- |
| GET    | /api/doctors/                | Doctorlar ro‘yxati            | Patient, Admin |
| GET    | /api/doctors/{id}/           | Doctor detail                 | Patient, Admin |
| GET    | /api/doctors/{id}/timeslots/ | Doctorning bo‘sh TimeSlotlari | Patient, Admin |

🔍 Search & filter:

```
/api/doctors/?search=cardio
```

---

## ⏰ TimeSlots (Doctor Schedule)

| Method | Endpoint             | Description          | Access |
| ------ | -------------------- | -------------------- | ------ |
| POST   | /api/timeslots/      | TimeSlot yaratish    | Doctor |
| GET    | /api/timeslots/      | O‘z TimeSlotlari     | Doctor |
| GET    | /api/timeslots/{id}/ | TimeSlot detail      | Doctor |
| DELETE | /api/timeslots/{id}/ | TimeSlotni o‘chirish | Doctor |

**Qoidalar:**

* Faqat o‘z TimeSlotlari
* Band qilingan TimeSlot o‘chirilmaydi

---

## 📅 Appointments

| Method | Endpoint                       | Description                | Access          |
| ------ | ------------------------------ | -------------------------- | --------------- |
| POST   | /api/appointments/             | Appointment bron qilish    | Patient         |
| GET    | /api/appointments/me/          | Mening appointmentlarim    | Doctor, Patient |
| GET    | /api/appointments/             | Barcha appointmentlar      | Admin           |
| GET    | /api/appointments/{id}/        | Appointment detail         | Owner, Admin    |
| PATCH  | /api/appointments/{id}/status/ | Statusni o‘zgartirish      | Doctor, Admin   |
| DELETE | /api/appointments/{id}/        | Appointmentni bekor qilish | Patient, Admin  |

**Filter & query params:**

```
/api/appointments/me/?status=pending
/api/appointments/me/?date=2026-01-10
/api/appointments/?doctor=1
```

---

## ✅ Business Logic

* Doctor TimeSlot’lari bir-birini qoplamasligi kerak
* Bitta TimeSlot faqat 1 ta appointment bilan bog‘lanadi
* O‘tmishdagi vaqtga appointment yoki timeslot yaratib bo‘lmaydi
* Cancelled appointment → TimeSlot yana `is_available=True`
* Doctor o‘ziga appointment bron qila olmaydi

---

## 🛡 Permissions

* `IsAdmin` – Admin faqat
* `IsDoctor` – Doctor faqat
* `IsPatient` – Patient faqat
* `IsOwner` – Faqat o‘zi yoki Admin

---

## ⚡ Quick Start

1. **Clone repo**

```bash
git clone <repo_url>
cd clinic_api
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup environment variables**

```bash
cp .env.example .env
# Update DB and secret key in .env
```

5. **Run migrations & create superuser**

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

6. **Run server**

```bash
python manage.py runserver
```

7. **Access API**

* Swagger: `http://127.0.0.1:8000/api/schema/swagger-ui/`
* Redoc: `http://127.0.0.1:8000/api/schema/redoc/`
