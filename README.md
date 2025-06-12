```markdown
# SCPP Stablecoin Payment Platform

## Repository Structure

```

/
├── main.py
├── Tables.sql
├── components/
│   ├── Home.py
│   ├── wallet\_create.py
│   ├── Dashboard.py
│   └── Transaction\_History.py
└── images/
└── OIP.jpeg

````

## Description

Python Streamlit application for user registration, login, wallet management and stablecoin payments on an EVM‑compatible chain.  
Implements:  
- SQL Server backend via SQLAlchemy + pyodbc  
- Session state for user and wallet data  
- Registration and login screens  
- Profile page with user info and wallet status toggle  
- Wallet page for deposit, currency swap, fund transfer  
- Database schema in `Tables.sql`

## Prerequisites

- Python 3.9+  
- Streamlit  
- pandas  
- SQLAlchemy  
- pyodbc  
- ODBC Driver 17 for SQL Server  
- SQL Server instance  

## Installation

1. Clone repository  
   ```bash
   git clone https://github.com/kinola-IQ/SCPP-stablecoin-payment-platform.git
   cd SCPP-stablecoin-payment-platform
````

2. Create virtual environment and install packages

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install streamlit pandas sqlalchemy pyodbc
   ```
3. Modify ODBC connection in `main.py` get\_database\_connection()

## Database Setup

1. Open SQL Server Management Studio
2. Create database `stablecoin`
3. Run `Tables.sql` to create tables:

   * `users_registration` (user\_id, Full\_Name, email, Password, country)
   * `wallets` (wallet\_id, user\_id, email, wallet\_status, cNGN, USDx, EURx, GBP)

## Configuration

Update environment‑specific values in `main.py` ODBC string:

```python
odbc_str = (
  "DRIVER={ODBC Driver 17 for SQL Server};"
  "SERVER=<SERVER_ADDRESS>;"
  "DATABASE=stablecoin;"
  "Trusted_Connection=yes;"
)
```

## Usage

Run Streamlit server:

```bash
streamlit run main.py
```

Interact via browser at `http://localhost:8501`.

## Components

* **main.py**: entrypoint; login/register logic; navigation; session state
* **components/Home.py**: profile page; account info and settings tabs
* **components/wallet\_create.py**: deposit, swap, transfer UI; currency update functions
* **components/Dashboard.py**: placeholder under construction
* **components/Transaction\_History.py**: placeholder under construction
* **images/OIP.jpeg**: user profile image asset

```
```
