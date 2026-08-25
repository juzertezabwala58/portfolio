"""
Banking Management System - Database Layer
Provides SQLite database initialization, automated schema management, and seed data.
"""

import sqlite3
import datetime
from pathlib import Path

DB_FILE = Path(__file__).parent / "bank_system.db"

def get_connection():
    """Establish and return SQLite database connection."""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables and populate seed data if not present."""
    conn = get_connection()
    cursor = conn.cursor()

    # 1. Super Admin Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS superadmin (
            sid TEXT PRIMARY KEY,
            spwd TEXT NOT NULL,
            name TEXT NOT NULL
        )
    """)

    # 2. Branch Admin Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin (
            aid TEXT PRIMARY KEY,
            apwd TEXT NOT NULL,
            name TEXT NOT NULL,
            sid TEXT,
            FOREIGN KEY (sid) REFERENCES superadmin (sid)
        )
    """)

    # 3. Branches Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS branches (
            bid TEXT PRIMARY KEY,
            bname TEXT NOT NULL,
            city TEXT NOT NULL,
            contact TEXT,
            email TEXT,
            adminid TEXT,
            FOREIGN KEY (adminid) REFERENCES admin (aid)
        )
    """)

    # 4. Employees Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            eid TEXT PRIMARY KEY,
            epwd TEXT NOT NULL,
            name TEXT NOT NULL,
            bid TEXT NOT NULL,
            role TEXT DEFAULT 'Associate',
            salary REAL DEFAULT 35000.0,
            FOREIGN KEY (bid) REFERENCES branches (bid)
        )
    """)

    # 5. Customers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            cid TEXT PRIMARY KEY,
            cpwd TEXT NOT NULL,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            address TEXT,
            bid TEXT,
            FOREIGN KEY (bid) REFERENCES branches (bid)
        )
    """)

    # 6. Accounts Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            acc_no TEXT PRIMARY KEY,
            cid TEXT NOT NULL,
            acc_type TEXT DEFAULT 'Savings',
            balance REAL DEFAULT 0.0,
            created_at TEXT NOT NULL,
            FOREIGN KEY (cid) REFERENCES customers (cid)
        )
    """)

    # 7. Transactions Ledger
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
            acc_no TEXT NOT NULL,
            tx_type TEXT NOT NULL,
            amount REAL NOT NULL,
            balance_after REAL NOT NULL,
            details TEXT,
            timestamp TEXT NOT NULL,
            FOREIGN KEY (acc_no) REFERENCES accounts (acc_no)
        )
    """)

    # 8. Loan Applications
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            loan_id INTEGER PRIMARY KEY AUTOINCREMENT,
            cid TEXT NOT NULL,
            amount REAL NOT NULL,
            status TEXT DEFAULT 'Pending',
            purpose TEXT,
            applied_at TEXT NOT NULL,
            FOREIGN KEY (cid) REFERENCES customers (cid)
        )
    """)

    # Seed Default Data if empty
    cursor.execute("SELECT COUNT(*) as count FROM superadmin")
    if cursor.fetchone()["count"] == 0:
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Superadmin
        cursor.execute("INSERT INTO superadmin VALUES (?, ?, ?)", ("super1", "admin123", "Chief Administrator"))

        # Admin
        cursor.execute("INSERT INTO admin VALUES (?, ?, ?, ?)", ("admin1", "admin123", "Regional Manager", "super1"))

        # Branch
        cursor.execute("INSERT INTO branches VALUES (?, ?, ?, ?, ?, ?)", 
                       ("B001", "Downtown Corporate Branch", "Mumbai", "+91 22 5550199", "mumbai.branch@nexbank.com", "admin1"))

        # Employee
        cursor.execute("INSERT INTO employees VALUES (?, ?, ?, ?, ?, ?)", 
                       ("EMP001", "emp123", "Juzer Tezabwala", "B001", "Senior Operations Executive", 65000.0))

        # Customer
        cursor.execute("INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?)", 
                       ("CUST001", "cust123", "Ali Asgar", "aliasgar@example.com", "+91 9876543210", "42 Heritage Road", "B001"))

        # Account ($5,000 opening balance)
        cursor.execute("INSERT INTO accounts VALUES (?, ?, ?, ?, ?)", 
                       ("ACC1001", "CUST001", "Savings", 5000.0, now))

        # Initial Transaction
        cursor.execute("INSERT INTO transactions (acc_no, tx_type, amount, balance_after, details, timestamp) VALUES (?, ?, ?, ?, ?, ?)",
                       ("ACC1001", "DEPOSIT", 5000.0, 5000.0, "Initial Account Opening Deposit", now))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully at:", DB_FILE)
