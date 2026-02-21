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
⚙️ Setup & Run Locally
1️⃣ Clone repository
git clone https://github.com/<your-username>/address-book-api.git
cd address-book-api
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run application
uvicorn add_book.main:app --reload
