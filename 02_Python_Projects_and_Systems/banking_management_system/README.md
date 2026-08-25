# 🏦 Enterprise Banking Management System

## 📌 Overview
A modular, production-grade console application built in Python and SQLite that simulates core banking workflows across four distinct user tiers: **Super Administrator**, **Branch Administrator**, **Bank Operations Staff**, and **Customer Account Holder**.

---

## 🏛️ System Architecture
The application follows standard software engineering design patterns:
```
banking_management_system/
├── database.py   # Database connection, automated table creation & seed data
├── models.py     # OOP domain logic, banking services, and transactional integrity
├── main.py       # Role-based interactive terminal user interface
└── README.md     # Project documentation
```

---

## 🔐 Multi-Tier Role Portals

| Role | Access Permissions & Operations |
| :--- | :--- |
| **👑 Super Admin** | Create and onboard Branch Administrators, list global admins, update master credentials. |
| **🏢 Branch Admin** | Establish new branches, register employees, transfer staff across branch network, view directory. |
| **💼 Bank Employee** | Open customer accounts, process cash deposits & withdrawals, evaluate & approve loan applications. |
| **👤 Customer** | Mobile/online deposits, withdrawals, real-time fund transfers, passbook statement, loan requests. |

---

## 🧪 Demo Credentials (Ready Out-of-the-Box)

Upon first run, the SQLite database auto-initializes with pre-populated credentials:

- **Super Admin**: `ID: super1` | `Password: admin123`
- **Branch Admin**: `ID: admin1` | `Password: admin123`
- **Bank Employee**: `ID: EMP001` | `Password: emp123`
- **Customer**: `ID: CUST001` | `Password: cust123` *(Account: ACC1001 with $5,000 opening balance)*

---

## ⚡ How to Run
```bash
python main.py
```
