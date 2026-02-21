Address Book API

A minimal FastAPI application that allows users to create, update, delete, and search addresses based on geographic distance.
Features

  Create address with coordinates
  
  Update address
  
  Delete address
  
  List all addresses
  
  Search addresses within a given distance
  
  Input validation using Pydantic
  
  SQLite database
  
  Logging middleware
  

🛠️ Tech Stack

Python 3.12

FastAPI

SQLAlchemy

SQLite

Uvicorn


📁 Project Structure
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


Setup & Run Locally

step1.
git clone https://github.com/sreevishnukiran/address-book-api.git
cd address-book-api

step2.
Create virtual environment
python -m venv venv


step3.
  source venv/bin/activate   # Linux / Mac
  venv\Scripts\activate      # Windows


step4.
  Install dependencies
  pip install -r requirements.txt

step5.
 Run application
  uvicorn add_book.main:app --reload


step6
  check the apis
  the application is running in default 8000 port ..copy the below link and open in browser to access the apis
  http://127.0.0.1:8000/docs
