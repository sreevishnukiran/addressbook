# Address Book API

A minimal FastAPI application that allows users to create, update, delete, and search addresses based on geographic distance.

---

## 🚀 Features

* Create address with coordinates
* Update address
* Delete address
* List all addresses
* Search addresses within a given distance
* Input validation using Pydantic
* SQLite database
* Logging middleware

---

## 🛠️ Tech Stack

* Python 3.12
* FastAPI
* SQLAlchemy
* SQLite
* Uvicorn

---

## 📁 Project Structure

```
add_book/
├── main.py
├── db.py
├── models.py
├── schemas.py
├── routes/
│   └── address.py
├── utils.py
├── logging_config.py

requirements.txt
README.md
```

---

## ⚙️ Setup & Run Locally

### 1️⃣ Clone repository

```
git clone https://github.com/sreevishnukiran/addressbook.git


````
cd addressbook/
```

### 2️⃣ Create virtual environment

```
python -m venv venv
```

### 3️⃣ Activate environment

**Linux / Mac**

```
source venv/bin/activate
```

**Windows**

```
venv\Scripts\activate
```

### 4️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 5️⃣ Run application

```
uvicorn add_book.main:app --reload
```

---

## 📚 API Documentation

The application runs on the default port **8000**.

Open the following URL in your browser to access Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 🔍 Example Endpoints

### ➤ Create Address

`POST /addresses`

### ➤ Get All Addresses

`GET /addresses`

### ➤ Search Nearby Addresses

`GET /addresses/nearby?lat=<latitude>&lon=<longitude>&distance_km=<distance>`

### ➤ Update Address

`PUT /addresses/{id}`

### ➤ Delete Address

`DELETE /addresses/{id}`

---

## 🧠 Design Decisions

* Used SQLite for simplicity and quick setup
* Implemented Haversine formula for distance calculation
* Structured code into routes, models, schemas, and utilities
* Added validation for latitude and longitude ranges
* Included logging middleware for request tracing

---

## 📌 Future Improvements

* Pagination support
* Authentication

---

## 👨‍💻 Author

**Sree Vishnu Kiran**
Backend Developer | Python | FastAPI
